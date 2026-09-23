# Lands of Glory – Weiterentwicklung der App

**Stand:** 31.08.2026  
**Basis:** Ausschließlich die in diesem Chat besprochenen Überlegungen zur technischen Weiterentwicklung der bestehenden App.

---

## 1. Ausgangslage

Die bestehende Anwendung ist ein browserbasierter Prototyp von **Lands of Glory** mit:

- TypeScript
- Vite
- PixiJS
- `@lands-of-glory/game-core`
- Startscreen
- Army Builder
- Spielfeld-Rendering
- GameController
- Bewegungslogik
- Kampf
- Würfel-/Kampfanimationen
- Banner
- Siegbedingungen
- Undo/History
- Debug-/UI-Funktionen

Die bestehende Trennung in `game-core`, Renderer, Controller und UI ist grundsätzlich eine gute Basis für den Umbau auf eine Online-Web-App.

---

## 2. Zielbild

Die Anwendung soll zu einer Web-App werden, in der:

1. Spieler die Webseite aufrufen.
2. Spieler sich anmelden oder optional als Gast spielen.
3. Ein Spieler einen Raum erstellt.
4. Andere Spieler über Raumcode oder Link beitreten.
5. Alle Spieler in einer Lobby sichtbar sind.
6. Spieler ihre Armeen zusammenstellen.
7. Der Host bzw. das System das Spiel startet.
8. Alle Spieler denselben GameState sehen.
9. Züge und Kämpfe serverseitig validiert werden.
10. Alle Clients synchron aktualisiert werden.
11. Spieler nach Verbindungsabbrüchen wieder einsteigen können.
12. Die Anwendung auf PC und Handy funktioniert.

---

## 3. Wichtigste Architekturentscheidung

Die wichtigste Änderung ist:

> Der Server wird die autoritative Instanz für den GameState.

Heute liegt der GameState im Browser bzw. im `GameController`.

Für Multiplayer sollte der Browser nur noch Aktionen anfordern.

```text
Client
  │
  │ MOVE_COMMANDER
  ▼
Server
  │
  ├─ Ist der Spieler am Zug?
  ├─ Gehört ihm der Commander?
  ├─ Ist der Zug erlaubt?
  ├─ Ist das Ziel gültig?
  └─ game-core validiert die Regel
        │
        ▼
   GameState ändern
        │
        ▼
   Broadcast an alle Clients
```

Der Client entscheidet also nicht selbst, ob eine Aktion gültig ist.

---

## 4. Warum server-authoritative?

Das verhindert unter anderem:

- manipulierte Browserzustände
- manipulierte Bewegung
- manipulierte Würfelergebnisse
- unterschiedliche GameStates zwischen Spielern
- Regelabweichungen zwischen Clients

Der Server ist die einzige Quelle der Wahrheit.

---

## 5. Empfohlene Projektstruktur

```text
lands-of-glory/
│
├── packages/
│   └── game-core/
│       ├── rules/
│       ├── movement/
│       ├── combat/
│       ├── state/
│       └── scoring/
│
├── apps/
│   ├── web/
│   │   ├── PixiJS
│   │   ├── Startscreen
│   │   ├── Army Builder
│   │   ├── Lobby
│   │   ├── Game UI
│   │   └── Responsive UI
│   │
│   └── game-server/
│       ├── REST API
│       ├── WebSocket
│       ├── RoomManager
│       ├── GameSession
│       ├── Auth
│       └── Persistence
│
└── infrastructure/
    ├── docker-compose.yml
    ├── Caddyfile
    └── deployment/
```

---

## 6. Rolle von `game-core`

Der bestehende `@lands-of-glory/game-core` sollte möglichst erhalten bleiben.

Er sollte die reine Spiellogik enthalten:

```text
game-core
├── GameState
├── Bewegung
├── Kampf
├── Regelprüfung
├── Siegbedingungen
├── Scoring
└── Zufallslogik / RNG
```

Wichtig: `game-core` sollte möglichst keine DOM-, PixiJS-, UI- oder Netzwerkabhängigkeiten enthalten.

---

## 7. Web-Client

Der bestehende Prototype würde im Wesentlichen zum Web-Client werden.

Verantwortung des Clients:

- Darstellung
- PixiJS
- Animationen
- Benutzereingaben
- Auswahl von Commandern
- Touch-/Mauseingaben
- Lobby
- Army Builder
- Anzeigen von GameState
- Anzeigen von Serverfehlern
- WebSocket-Verbindung

Nicht mehr verantwortlich:

- endgültige Regelentscheidung
- Würfelergebnis
- endgültiger GameState
- Berechtigung eines Spielzuges

---

## 8. Game Server

Der neue Server ist die zentrale Multiplayer-Komponente.

Empfohlene Technologien:

```text
Node.js
TypeScript
Fastify oder NestJS
WebSocket oder Socket.IO
PostgreSQL
```

Für die erste Version wäre z. B. ausreichend:

```text
Node.js
TypeScript
Fastify
WebSocket
PostgreSQL
```

---

## 9. REST vs. WebSocket

### REST

REST eignet sich für:

- Login
- Benutzerprofil
- Raum erstellen
- Raum suchen
- Spielhistorie
- Statistiken
- Ergebnisse
- allgemeine Metadaten

### WebSocket

WebSockets eignen sich für:

- Join/Leave
- Ready-Status
- Spielstart
- Bewegung
- Angriff
- Kampfresultat
- Turn-Ende
- GameState-Updates
- Reconnect
- Live-Synchronisation

Für das eigentliche Spiel sollte WebSocket verwendet werden.

---

## 10. Raum-System

Ein Raum könnte ungefähr so modelliert werden:

```ts
interface GameRoom {
  id: string;

  status:
    | 'waiting'
    | 'army-building'
    | 'playing'
    | 'finished';

  hostUserId: string;

  players: RoomPlayer[];

  gameState?: GameState;

  createdAt: Date;
}
```

---

## 11. Raum-Ablauf

```text
1. Spieler öffnet landsofglory.de
2. Login oder Gast
3. "Raum erstellen"
4. Server erzeugt Raumcode
5. Beispiel: AB12CD
6. Link: landsofglory.de/game/AB12CD
7. Andere Spieler treten bei
8. Lobby zeigt Spieler + Ready-Status
9. Spieler konfigurieren ihre Armeen
10. Spiel starten
11. Server erzeugt GameState
12. Clients erhalten GameState
13. Aktionen laufen über WebSocket
```

---

## 12. Beispiel für eine Bewegung

Client sendet:

```json
{
  "type": "MOVE_COMMANDER",
  "gameId": "game-4711",
  "commanderId": "commander-4",
  "target": {
    "x": 12,
    "y": 8
  }
}
```

Server prüft:

```text
Ist der Spieler am Zug?
        ↓
Gehört ihm der Commander?
        ↓
Hat der Commander bereits gehandelt?
        ↓
Ist das Ziel erreichbar?
        ↓
Ist das Feld frei?
        ↓
Ist der Zug regelkonform?
        ↓
GameState aktualisieren
```

Danach informiert der Server alle Spieler.

---

## 13. State-Synchronisation

Serverantwort z. B.:

```json
{
  "type": "GAME_STATE_UPDATED",
  "version": 174,
  "state": {}
}
```

Optional sollte jeder GameState eine Versionsnummer erhalten, damit Clients erkennen können, ob Updates fehlen.

---

## 14. Kampf

Die Kampfentscheidung muss auf dem Server stattfinden.

Nicht:

```text
Browser würfelt
      ↓
meldet Ergebnis an Server
```

Sondern:

```text
Client:
ATTACK
   ↓
Server:
canAttack()
resolveCombat()
applyCombatResult()
   ↓
CombatResult
   ↓
Clients
   ↓
CombatDiceAnimation.play()
```

Die bestehende Kampfanimation kann weiterverwendet werden. Der Client animiert nur das serverseitig berechnete Ergebnis.

---

## 15. Zufall / RNG

Auch Zufall sollte serverseitig erzeugt werden.

```text
Server
  ↓
createRNG()
  ↓
resolveCombat()
  ↓
CombatResult
```

Damit kann kein Client eigene Würfelwerte manipulieren.

---

## 16. GameSession

Eine zentrale neue Serverklasse könnte sein:

```text
GameSession
├── GameState
├── PlayerSessions
├── GameRules
├── EventLog
├── Version
└── Persistence
```

Beispiel:

```ts
class GameSession {
  gameId: string;
  state: GameState;
  version: number;

  moveCommander(...)
  attack(...)
  endTurn(...)
  reconnect(...)
}
```

---

## 17. Umbau des aktuellen GameControllers

Heute:

```text
GameController
├── GameState
├── Bewegung
├── Angriff
├── Kampf
├── History
├── Renderer
└── UI
```

Ziel:

```text
GameClientController
├── Selection
├── Renderer
├── UI
└── NetworkClient
```

Server:

```text
GameSession
├── GameState
├── Rules
├── Movement
├── Combat
├── Turn Management
└── Persistence
```

---

## 18. NetworkClient

Im Web-Client sollte eine eigene Netzwerkkomponente entstehen:

```text
NetworkClient
├── connect()
├── disconnect()
├── joinRoom()
├── sendAction()
├── receiveState()
├── reconnect()
└── error handling
```

Dadurch bleibt Netzwerkcode aus Renderer und UI heraus.

---

## 19. Reconnect

Reconnect sollte von Anfang an berücksichtigt werden.

```text
Spieler spielt
     ↓
WLAN bricht ab
     ↓
WebSocket getrennt
     ↓
Browser verbindet sich neu
     ↓
Server authentifiziert Spieler
     ↓
aktueller GameState
     ↓
Spiel geht weiter
```

Der Server muss dafür Spieler, Spiel und Session wieder zuordnen können.

---

## 20. Persistenz

Für eine robuste Version sollte PostgreSQL verwendet werden.

Mögliche Tabellen:

```text
users
rooms
games
game_players
game_events
game_results
```

---

## 21. Event Log

Eine wichtige Erweiterung wäre ein `game_events`-Log.

Beispiel:

```text
001 GAME_CREATED
002 PLAYER_JOINED
003 GAME_STARTED
004 COMMANDER_MOVED
005 ATTACK_STARTED
006 COMBAT_RESOLVED
007 TURN_ENDED
```

Vorteile:

- Debugging
- Replays
- Spielhistorie
- Reconnect
- Statistiken
- Fehleranalyse
- spätere Cheat-Erkennung

---

## 22. Mobile und Desktop

Es sollte zunächst keine separate Handy-App entwickelt werden.

Die erste Version sollte eine responsive Web-App sein.

Technik:

```text
TypeScript
Vite
PixiJS
HTML/CSS
Responsive Layout
```

Erforderlich:

- Touch statt Rechtsklick
- Tap
- Drag
- Pinch-to-Zoom
- größere Buttons
- größere Touch-Flächen
- einklappbare Panels
- Landscape-Unterstützung
- Portrait-Unterstützung
- kein zwingendes Hover
- Safe Areas berücksichtigen

---

## 23. PWA

Die App könnte zusätzlich als Progressive Web App umgesetzt werden.

```text
Browser
   ↓
landsofglory.de
   ↓
"Zum Startbildschirm hinzufügen"
   ↓
Lands of Glory
```

Damit kann dieselbe Codebasis auf Android, iPhone/iPad, Windows, macOS und Linux verwendet werden.

Eine native App wäre zunächst nicht erforderlich.

---

## 24. Deployment

Für die erste Version ist keine komplexe Cloud-Infrastruktur notwendig.

Empfohlen:

```text
VPS
│
├── Caddy
├── Web Frontend
├── Game Server
└── PostgreSQL
```

oder per Docker Compose:

```text
docker-compose
│
├── web
├── backend
├── postgres
└── caddy
```

Öffentlich:

```text
Internet
   ↓
Cloudflare / DNS
   ↓
HTTPS
   ↓
Caddy
   │
   ├── Web Frontend
   └── Backend
       ├── REST
       └── WebSocket
              │
              ▼
         PostgreSQL
```

---

## 25. Was zunächst NICHT benötigt wird

Für den ersten Multiplayer-MVP nicht notwendig:

- Kubernetes
- Microservices
- Redis
- mehrere Serverinstanzen
- Load Balancer
- Matchmaking
- komplexe Cloud-Infrastruktur
- native Android-App
- native iOS-App

Redis wird erst interessant, wenn mehrere Backend-Instanzen oder sehr viele parallele Räume benötigt werden.

---

## 26. Wichtigster erster Multiplayer-Meilenstein

Nicht sofort Login, Datenbank und ELO bauen.

Der erste technische Meilenstein sollte sein:

> Zwei Browser öffnen dieselbe Spielsession, sehen dasselbe Spielfeld und können abwechselnd einen Commander bewegen.

```text
Browser A ──┐
            ├── WebSocket ── GameServer ── GameState
Browser B ──┘
```

Funktionen:

```text
✓ Raum erstellen
✓ Raum beitreten
✓ Spiel starten
✓ Commander bewegen
✓ Bewegung erscheint bei beiden Spielern
```

Wenn das stabil funktioniert, ist die Multiplayer-Grundarchitektur bewiesen.

---

## 27. Empfohlene Entwicklungsreihenfolge

### Phase 1 – Core vorbereiten

- `game-core` prüfen
- UI-Abhängigkeiten entfernen
- Serverfähigkeit sicherstellen
- GameState serialisierbar machen
- RNG prüfen

### Phase 2 – Server-Grundgerüst

- `apps/game-server`
- Node.js
- TypeScript
- Fastify
- Health Endpoint
- WebSocket

### Phase 3 – RoomManager

Implementieren:

```text
createRoom()
joinRoom()
leaveRoom()
getRoom()
```

### Phase 4 – GameSession

- GameState auf Server
- `startGame()`
- Player Mapping
- State Version

### Phase 5 – Bewegung

- `MOVE_COMMANDER`
- serverseitige Validierung
- Broadcast
- Client aktualisieren

### Phase 6 – Kampf

- `ATTACK`
- Server-RNG
- `resolveCombat`
- `applyCombatResult`
- CombatResult senden
- Client animieren

### Phase 7 – Turn Management

- End Turn
- aktiver Spieler
- serverseitige Prüfung

### Phase 8 – Reconnect

- Session-Wiederherstellung
- State erneut laden
- WebSocket-Reconnect

### Phase 9 – Lobby

- Ready
- Player List
- Host
- Spielstart

### Phase 10 – Persistenz

- PostgreSQL
- Games
- Players
- Results
- Events

### Phase 11 – Login

- Benutzer
- Auth
- Sessions

### Phase 12 – Mobile UI

- responsive Layout
- Touch
- Zoom
- mobile Panels

### Phase 13 – spätere Funktionen

- ELO
- Statistiken
- Match History
- Replays
- Spectator
- Matchmaking

---

## 28. Aufwand

Grobe Einschätzung aus diesem Chat:

### Technischer Multiplayer-Prototyp

Ohne starke KI-Unterstützung:

```text
ca. 7–15 Entwicklungstage
```

Mit effizientem Copilot/Codex/KI-Workflow:

```text
ca. 3–7 Entwicklungstage
```

Enthalten:

- 2 Spieler
- ein Raum
- synchroner GameState
- Bewegung
- Kampf
- Turn-Wechsel

### Solider MVP

Ohne starke KI-Unterstützung:

```text
ca. 15–30 Entwicklungstage
```

Mit gutem KI-Workflow:

```text
ca. 7–15 Entwicklungstage
```

Enthalten:

- Lobby
- 2–4 Spieler
- serverseitige Regeln
- WebSockets
- Reconnect
- Spiel speichern
- Mobile + Desktop
- Ergebnisse
- grundlegendes Deployment

### Öffentliche Version

Ohne starke KI-Unterstützung:

```text
ca. 40–80+ Entwicklungstage
```

Mit KI:

```text
ca. 20–45+ Entwicklungstage
```

Je nach Umfang:

- Accounts
- Passwort-Reset
- ELO
- Statistiken
- Match History
- Replays
- Spectator
- AFK/Timeout
- Monitoring
- Backups
- Security
- Rate Limiting
- CI/CD

---

## 29. Wo KI besonders Zeit spart

Gut automatisierbar:

- Backend-Boilerplate
- REST-Endpunkte
- WebSocket-Events
- DTOs
- TypeScript Types
- Tests
- Docker
- CI
- Refactoring
- Dokumentation
- Buildfehler
- Standard-CRUD

Weniger stark automatisierbar:

- Multiplayer-Architektur
- Race Conditions
- State-Synchronisation
- Reconnect
- Cheat-Schutz
- Security
- schwer reproduzierbare Bugs
- Mobile-Touch-Probleme
- komplexe UI-Probleme

---

## 30. Empfohlener KI-Entwicklungsprozess

Nicht:

```text
"Mach Lands of Glory multiplayerfähig."
```

Sondern:

```text
Issue
  ↓
kleiner Scope
  ↓
Branch
  ↓
KI-Agent
  ↓
Code
  ↓
Tests
  ↓
Build
  ↓
Git Diff
  ↓
Pull Request
```

---

## 31. Beispiel für erstes Multiplayer-Issue

```text
Titel:
Multiplayer RoomManager

Ziel:
Spieler können einen Raum erstellen und beitreten.

Implementieren:
- createRoom()
- joinRoom()
- leaveRoom()
- getRoom()

Noch nicht:
- Login
- PostgreSQL
- Kampf
- ELO
- Matchmaking

Akzeptanzkriterien:
- Raum erhält eindeutige ID
- mindestens zwei Clients können beitreten
- Spieler werden korrekt gelistet
- Disconnect entfernt oder markiert Spieler
- Unit Tests vorhanden
```

---

## 32. Empfohlener Technologie-Stack

### Frontend

```text
TypeScript
Vite
PixiJS
HTML
CSS
```

### Shared Logic

```text
@lands-of-glory/game-core
```

### Backend

```text
Node.js
TypeScript
Fastify
WebSocket
```

Optional:

```text
Socket.IO
NestJS
```

### Datenbank

```text
PostgreSQL
```

### Deployment

```text
Docker Compose
Caddy
VPS
```

### Später

```text
Redis
Monitoring
CI/CD
Object Storage
```

---

## 33. Kernaussage

Der bestehende Prototyp muss nicht vollständig neu gebaut werden.

Voraussichtlich weiterverwendbar:

- `game-core`
- PixiJS Renderer
- Startscreen
- Army Builder
- Kampfanimation
- UI-Grundlagen

Deutlich umzubauen:

- GameController
- GameState-Verantwortung
- Zugverarbeitung
- Kampfverarbeitung
- Netzwerk
- Lobby
- Persistenz
- Responsive/Touch UI

Die zentrale technische Veränderung lautet:

```text
Heute:

Browser
  ↓
GameController
  ↓
GameState


Ziel:

Browser
  ↓
NetworkClient
  ↓
GameServer
  ↓
GameSession
  ↓
game-core
  ↓
GameState
```

Damit entsteht eine saubere Grundlage für:

- Online-Multiplayer
- PC
- Handy
- Reconnect
- Persistenz
- ELO
- Statistiken
- Replays
- spätere Skalierung
