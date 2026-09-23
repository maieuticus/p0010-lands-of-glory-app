# template-spec-kit

**[Aktueller Arbeitsstand →](docs/DV_KONZEPT.md#aktueller-arbeitsstand)**

Zuletzt erledigt · Aktuell in Arbeit · Nächste Schritte · Blockaden

Technologieoffenes Projektgrundgerüst für Spec-Driven Development. Ein gemeinsamer
Kern wird mit einem Technologieprofil und den benötigten Diensten kombiniert.

**Projektziel, Architektur, Entwicklung und Betrieb stehen zusammen im
[DV-Konzept](docs/DV_KONZEPT.md).**

## Einstieg mit Spec Kit und Codex

Der Start erfolgt in dieser Reihenfolge: **Projekt erzeugen → Spec Kit für
Codex initialisieren → Projektziel und Constitution konkretisieren → erstes
Feature spezifizieren und umsetzen.** Die verbindlichen Details stehen im
[DV-Konzept – Einrichtung](docs/DV_KONZEPT.md#einrichtung).

### 1. Voraussetzungen bereitstellen

- Git und Python ab 3.11 für das Template.
- Für die unten gezeigte Codex-Installation: Node.js mit npm und ein Codex-Zugang.
- Für den Devcontainer zusätzlich Docker mit Compose und VS Code Dev Containers.
  Alternativ kannst du direkt unter Windows mit PowerShell arbeiten.

Installiere die Werkzeuge in der Umgebung, in der du Codex ausführen wirst.
Eine Windows-Installation steht im Linux-Devcontainer nicht automatisch bereit.

### 2. Ein eigenes Projekt erzeugen

Öffne dieses Repository lokal und führe im Template-Verzeichnis aus:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/create_project.py --name mein-projekt --stack python --output ../mein-projekt
```

Alternativ ein API-Projekt einschließlich PostgreSQL:

```sh
python scripts/create_project.py --name meine-api --recipe api-service --output ../meine-api
```

Das Ziel muss leer sein oder noch nicht existieren. `--dry-run` zeigt die
vorgesehenen Dateien, ohne ein Projekt anzulegen. Rohmaterialien dieses
Repositories, der Bausteinkatalog, lokale Einstellungen und Secrets werden
nicht in neue Projekte übernommen.

Auch eine über GitHubs **Use this template → Create a new repository** angelegte
und anschließend geklonte Kopie dient zunächst als Generator. Erzeuge daraus
dein Anwendungsprojekt in einem leeren Ziel; siehe
[Projekterzeugung](docs/DV_KONZEPT.md#neues-projekt-erzeugen).

Das Template enthält die Branches `main` und `development`. Beim Erzeugen über
die GitHub-Oberfläche **Include all branches** aktivieren, damit beide Branches
in der neuen Repository-Kopie angelegt werden. Mit der GitHub CLI:

```sh
gh repo create mein-projekt --template maieuticus/template-spec-kit --private --include-all-branches
```

Ohne diese Option übernimmt GitHub nur den Default-Branch `main`.

Wechsle anschließend in das erzeugte Projekt (beim API-Beispiel in `../meine-api`):

```sh
cd ../mein-projekt
git init
git status
```

Der Generator legt kein Git-Repository an. Öffne jetzt den **erzeugten Ordner**
im Editor und installiere die Abhängigkeiten aus dessen DV-Konzept, Abschnitt
„Einrichtung“. Prüfe die erzeugten Dateien und sichere den Ausgangsstand mit
einem lokalen Commit, bevor du Spec Kit initialisierst.

### 3. Codex installieren und Spec Kit initialisieren

**Windows/PowerShell ohne Container:** Installiere die CLIs, sofern sie noch
nicht in der benötigten Version vorhanden sind:

```powershell
python -m pip install specify-cli==1.0.7
npm.cmd install -g @openai/codex
specify version
codex.cmd --version
```

`1.0.7` ist die in [config/project.yaml](config/project.yaml) festgelegte
Spec-Kit-Version. Mit vorhandenem `uv` ist alternativ
`uv tool install specify-cli==1.0.7` möglich. Falls `specify` nach einer
pip-Installation fehlt, den Python-Scripts-Ordner in den Benutzer-`PATH`
aufnehmen und das Terminal neu öffnen. Die `.cmd`-Aufrufe vermeiden unter
PowerShell die Ausführung der npm-/Codex-`.ps1`-Starter.

**Jetzt Spec Kit einmalig im Root-Verzeichnis des erzeugten Projekts
initialisieren.** Der Generator und `git init` erledigen diesen Schritt nicht.
Führe den folgenden Block zusammenhängend in PowerShell aus; er ruft
`specify init` auf und erhält dabei die vorhandene Constitution:

```powershell
if (Test-Path -LiteralPath .specify/integration.json) {
    throw 'Bereits initialisiert; die Integrationsverwaltung verwenden.'
}
$constitutionPath = (Resolve-Path -LiteralPath .specify/memory/constitution.md).Path
$constitutionBytes = [System.IO.File]::ReadAllBytes($constitutionPath)
try {
    specify init --here --force --integration codex --script ps
    if ($LASTEXITCODE -ne 0) { throw 'Spec-Kit-Initialisierung fehlgeschlagen.' }
}
finally {
    [System.IO.File]::WriteAllBytes($constitutionPath, $constitutionBytes)
}
```

`--here` wählt das aktuelle Verzeichnis, `--force` erlaubt den bereits gefüllten
Projektordner, `--integration codex` richtet die Codex-Skills ein und
`--script ps` wählt PowerShell-Skripte. Bei einem Fehler den Zwischenstand
prüfen, bevor du fortfährst. Details stehen im
[PowerShell-Ablauf](docs/DV_KONZEPT.md#codex-mit-windows-powershell-initialisieren).

**Linux-Devcontainer:** Folge der
[Containereinrichtung](docs/DV_KONZEPT.md#lokaler-container-und-referenz-repositories)
und öffne das erzeugte Projekt mit „Reopen in Container“. Spec Kit ist dort
bereits installiert. Stelle Codex gemäß
[Codex-Einrichtung](docs/DV_KONZEPT.md#codex-installieren) auch im Container
bereit und führe in dessen Terminal aus:

```sh
python scripts/init_speckit.py --integration codex
```

Das vorhandene Init-Skript prüft die Spec-Kit-Version, erhält die Constitution
und ruft intern `specify init --here --integration codex --script sh --force`
auf. Verwende es für die Arbeit im Linux-Container. Für native PowerShell gilt
der obige Block mit `--script ps`. Wähle einen der beiden Wege.

Nach erfolgreicher Initialisierung im Projekt-Terminal prüfen:

```sh
specify integration list
git status
git diff
```

Codex muss als installiert erscheinen; unter `.agents/skills/` müssen die
`speckit-*`-Skills mit ihren `SKILL.md`-Dateien liegen. Prüfe auch die neuen,
noch unversionierten Dateien, die `git diff` allein nicht zeigt. Bei bereits
initialisierten Projekten gilt die
[Integrationsverwaltung](docs/DV_KONZEPT.md#bestehende-integrationen).

### 4. Codex starten und die Projektgrundlage konkretisieren

Starte nach erfolgreicher Initialisierung im Root-Verzeichnis des erzeugten
Projekts unter Windows:

```powershell
codex.cmd
```

Im Linux-Container lautet der Aufruf `codex`. Folge beim ersten Start dem
Anmeldedialog.

**Die folgenden `$speckit-*`-Aufrufe gehören in den Codex-Chat.** Sende sie
einzeln und prüfe jeweils das Ergebnis. Beginne einmalig mit:

```text
$speckit-constitution
Lies AGENTS.md, README.md, docs/DV_KONZEPT.md und die vorhandene
.specify/memory/constitution.md sowie die Projektstruktur und Tests.
Kläre mit mir Projektziel und offene Grundsatzentscheidungen. Konkretisiere
das DV-Konzept und passe die bestehende Constitution nur begründet und
versioniert an das Projekt an. Erhalte die Template-Prinzipien und benenne
Konflikte. Implementiere in diesem Schritt noch kein Feature.
```

Die mitgelieferte Constitution ist bereits die Grundlage. Eine zusätzliche
Vorlage unter `docs/templates/CONSTITUTION.md` wird hier nicht benötigt.

### 5. Das erste kleine Feature bearbeiten

Beschreibe zunächst Verhalten und Akzeptanzkriterien, zum Beispiel:

```text
$speckit-specify
Benutzer sollen über die Kommandozeile eine kurze Notiz lokal speichern können.
Akzeptanzkriterien: Eine nicht leere Notiz erhält eine ID; nach einem Neustart
kann sie über diese ID wieder gelesen werden; leere Eingaben werden mit einer
verständlichen Meldung abgewiesen.
Berücksichtige das DV-Konzept, vorhandenen Code, Datenmodelle und Tests.
```

Führe anschließend die passenden Schritte einzeln in Codex aus:

```text
$speckit-clarify
$speckit-plan
$speckit-checklist
$speckit-tasks
$speckit-analyze
$speckit-implement
$speckit-converge
```

Zweck und Ergebnisse der Schritte beschreibt der
[Feature-Ablauf im DV-Konzept](docs/DV_KONZEPT.md#manueller-ablauf-mit-codex).
Die Artefakte gehören nach `specs/<nummer>-<name>/`. Prüfe das Ergebnis gegen
die Akzeptanzkriterien und führe im Projekt-Terminal `python scripts/check.py`
sowie die relevanten Feature-Tests aus. Offene Aufgaben aus `converge`
nacharbeiten und erneut prüfen; anschließend Diff und neue Dateien durchsehen.

Beim nächsten Arbeitsstart öffnest du dasselbe Projekt, startest Codex und
arbeitest am bestehenden Feature weiter oder beginnst mit `$speckit-specify`
ein neues. Installation, Initialisierung und Constitution sind keine Schritte,
die du bei jedem Feature wiederholst. Wenn Skills fehlen, prüfe
`specify integration list` und `.agents/skills/` und starte Codex neu.

## Orientierung

| Thema | Einstieg |
| --- | --- |
| Einrichtung und täglicher Start | [Quickstart](QUICKSTART.md) |
| Template, Spec Kit und Agent erklärt | [Zusammenspiel](docs/DV_KONZEPT.md#zusammenspiel-von-template-spec-kit-und-agent) |
| Befehle verstehen und Probleme eingrenzen | [Befehle und Aufruforte](docs/DV_KONZEPT.md#befehle-und-aufruforte) |
| Copilot und andere Agenten | [Integrationen und Chat-Aufrufe](docs/DV_KONZEPT.md#agent-integration-und-chat-aufrufe) |
| Verbindliche Projektbeschreibung | [DV-Konzept](docs/DV_KONZEPT.md) |
| Entwicklungsmethodik | [Constitution](.specify/memory/constitution.md) |
| Feature-Spezifikationen | [Feature-Übersicht](specs/README.md) |
| Technologien, Dienste und API-Rezept | [Bausteinkatalog](templates/README.md) |
| Arbeitsregeln für Agenten | [AGENTS.md](AGENTS.md) |
| Referenz-Repositories und Beiträge | [DV-Konzept: Wissensaustausch](docs/DV_KONZEPT.md#wissensaustausch) |

## Prüfen

```sh
python scripts/check.py
```

Dies prüft Dokumentlinks, Dateisyntax und die Template-Tests. Die
[CI](.github/workflows/ci.yml) prüft zusätzlich erzeugte Projekte und Compose.
