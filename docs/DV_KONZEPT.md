# DV-Konzept: template-spec-kit

**Stand:** 23.09.2026
**Status:** Projektgrundgerüst mit optionalen Technologie- und Dienstbausteinen

Dieses Dokument ist die verbindliche Beschreibung von Projektziel, Architektur,
Entwicklung und Betrieb. README, Quickstart und Verzeichnisübersichten verlinken
hierher. Getrennte Dateien für Vision, Architektur, Entwicklung oder Betrieb
werden nicht gepflegt.

## Aktueller Arbeitsstand

**Stand:** 2026-09-23

**Aktives Feature:** Kein neues Feature; Dokumentationspflege zu Spec Kit abgeschlossen.

### Zuletzt erledigt

- Projektübersicht mit README-Einstieg, Statusbefehl und Agentenregeln umgesetzt;
  [Aufgaben von Feature 002](../specs/002-projektstatus/tasks.md).
- Zwei allgemeine Spec-Kit-Quickstarts und die allgemeinen Anteile des
  historischen Boardgame-Quickstarts gesichtet; Befehle mit Spec Kit 1.0.7 abgeglichen.
- Befehlerklärungen, Agentenaufrufe und den Umgang mit vorhandenen Unterlagen
  in dieses Konzept und die Projektvorlagen übernommen; zwei überholte
  Spec-Kit-Rohdateien entfernt. [Auswertung und Verbleib](raw-materials/README.md#auswertung-der-spec-kit-unterlagen-am-23092026).

### Aktuell in Arbeit

- Keine laufende Umsetzung. Die manuelle Startprüfung aus Feature 002 bleibt offen.

### Nächste Schritte

1. In VS Code automatische Aufgaben für den vertrauenswürdigen Workspace erlauben.
2. Beim erneuten Öffnen die Startanzeige prüfen, zusätzlich „Projektstatus anzeigen“
   manuell ausführen und das Ergebnis in [T006](../specs/002-projektstatus/tasks.md) festhalten.

### Blockaden und Prüfstatus

- `python scripts/check.py`: Dokumentlinks, Dateisyntax und alle 14 Tests nach
  Übernahme der Erklärungen erfolgreich; auch erzeugte Projekte geprüft.
- Spec-Kit-Befehle anhand der Referenz für 1.0.7 abgeglichen;
  Initialisierung und Agenten-Chat nicht erneut ausgeführt.
- Keine Blockade; interaktive Startanzeige aus Feature 002 weiterhin ungeprüft.
- Frühere Ergebnisse und offene Laufzeitprüfungen stehen im [Prüfstatus](#prüfstatus).

## Inhalt

- [Aktueller Arbeitsstand](#aktueller-arbeitsstand)
- [Projektziel](#projektziel)
- [Architektur](#architektur)
- [Einrichtung](#einrichtung)
- [Entwicklung](#entwicklung)
- [Betrieb](#betrieb)
- [Wissensaustausch](#wissensaustausch)
- [Weiterentwicklung und Versionen](#weiterentwicklung-und-versionen)
- [Prüfstatus](#prüfstatus)
- [Quellen](#quellen)

## Projektziel

Das Repository liefert einen wiederverwendbaren Grundaufbau für unterschiedliche
Softwareprojekte. Der gemeinsame Kern umfasst Spec-Driven Development,
Dokumentation, Arbeitsregeln, einen Devcontainer und Prüfungen. Technologien
und Infrastruktur werden nach Bedarf ergänzt.

Zielgruppe sind Entwickler und Coding-Agenten, die Projekte nachvollziehbar von
der Anforderung bis zur geprüften Implementierung bearbeiten und Erfahrungen
anschließend an Template und Knowledge Base zurückgeben.

Der Generator unterstützt einen neutralen Kern, Python, TypeScript und
Java/Maven. PostgreSQL, Keycloak und Observability sind unabhängig auswählbar.
Das API-Rezept kombiniert Python, FastAPI und PostgreSQL. Fachliche Funktionen,
produktive Zugangsdaten und ein fertiges Produktionsdeployment sind nicht Teil
des Grundgerüsts.

Mobile Frameworks können als weitere Profile ergänzt werden. Native
Plattformwerkzeuge bleiben eine zusätzliche Voraussetzung; iOS benötigt
insbesondere die Apple-Entwicklungsumgebung.

### Zusammenspiel von Template, Spec Kit und Agent

| Baustein | Aufgabe |
| --- | --- |
| Dieses Template | Erzeugt Projektstruktur, Technologieprofil, Konfiguration, DV-Konzept, Arbeitsregeln und gemeinsame Prüfungen. |
| Spec Kit / Specify CLI | Richtet die gewählte Agent-Integration und die Werkzeuge für Spezifikation, Planung und Umsetzung ein. |
| Coding-Agent, etwa Codex oder Copilot | Bearbeitet die Feature-Schritte im Projekt anhand der Anforderungen und Regeln. |
| Entwickler | Klärt Ziele, prüft Ergebnisse und entscheidet über Veröffentlichung. |

Ein erzeugtes Grundgerüst besitzt bereits eine Constitution, aber noch keine
initialisierte Spec-Kit-Integration. Installation des Werkzeugs, Initialisierung
des Projekts und Bearbeitung einzelner Features sind getrennte Schritte.

## Architektur

```text
.devcontainer/   Entwicklungsumgebung und lokale Dienstzusammenschaltung
.github/         GitHub Actions, Issue-/PR-Vorlagen und gewählte Integration
.specify/        Constitution, Vorlagenanpassungen und Entwicklungsworkflow
.vscode/         Gemeinsame Editor-Einstellungen und Prüfaufgabe
config/          Projektmetadaten, Referenz-Repos und Dienstkonfiguration
docs/            DV-Konzept, ursprüngliche Unterlagen und Entscheidungen
specs/           Spezifikation, Plan und Aufgaben je Feature
scripts/         Erzeugung, Einrichtung, Prüfungen und Beitragsvorbereitung
templates/       Technologieprofile, Dienste und zusammengesetzte Rezepte
tests/           Tests des Template-Generators und seiner Zugriffsregeln
```

### Zuständigkeiten und maßgebliche Dateien

| Inhalt | Ablage |
| --- | --- |
| Gemeinsame Prinzipien | `.specify/memory/constitution.md` |
| Projektbeschreibung | Dieses Dokument |
| Arbeitsstand und nächste Schritte | [Aktueller Arbeitsstand](#aktueller-arbeitsstand) in diesem Dokument |
| Konkrete Feature-Anforderung | `specs/<nummer>-<name>/spec.md` |
| Technischer Feature-Plan und Aufgaben | `plan.md` und `tasks.md` im Feature |
| Rohmaterialien | `docs/raw-materials/` |
| Aktive Konfiguration | `config/` und die ausgewählten Werkzeugdateien |
| Lokale Secrets | Ignorierte `.env`, niemals Git |
| Versions- und Profilnachweis | `config/project.yaml` |

Das Template veröffentlicht `main` als stabilen Ausgangspunkt und `development`
als gemeinsamen Entwicklungszweig. GitHub übernimmt bei „Use this template“
standardmäßig nur den Default-Branch. In der Weboberfläche deshalb
**Include all branches** auswählen; mit der CLI `gh repo create ... --template
maieuticus/template-spec-kit --include-all-branches` verwenden. Erst dann
enthält das neue Repository beide Branches. Die aus einer Vorlage erzeugten
Branches haben unabhängige Historien und dienen als getrennte Startzweige.

`config/project.yaml` und `config/repositories.yaml` sind Konventionen dieses
Templates. Spec Kit wertet sie nicht selbst aus. Die Integrationsmetadaten
unter `.specify/integration.json` und `.specify/integrations/` erzeugt dagegen
die Specify CLI bei der Initialisierung. Sie werden nicht von Hand erfunden.

### Bausteine

Der Generator kopiert einen ausdrücklich festgelegten Kern und ausgewählte
`files/`-Verzeichnisse. `module.yaml` ergänzt Prüfkommandos, Laufzeiten,
Umgebungsvariablen und Ports. Dienstbausteine liefern Compose-Fragmente.
`.template`-Dateien werden beim Kopieren umbenannt und Platzhalter ersetzt.

Das Ziel muss leer sein. Der Generator überschreibt keine bestehenden
Projektdateien und führt weder Installation noch Git-Initialisierung, Push,
Issue-Erstellung oder Spec-Kit-Initialisierung aus.

Der Anwendungscode folgt dem Profil: Python `src/app/` und `tests/`,
TypeScript `src/` und `tests/`, Maven `src/main/java/` und `src/test/java/`.
`.mvn/` und Maven Wrapper werden erst bei Bedarf im Java-Projekt ergänzt.
Ein Monorepo kann stattdessen `apps/` und `packages/` verwenden.

### Devcontainer und Dienste

Der Container startet über `.devcontainer/compose.yaml`. Das Python-Basisimage
stellt die gemeinsamen Werkzeuge bereit; Features ergänzen Node oder Java nur
im gewählten Profil. Die Specify CLI ist auf 1.0.7 festgelegt.

PostgreSQL, Keycloak, Prometheus und Grafana laufen bei Auswahl als separate
Container. Die ausgewählten Services stehen ausdrücklich in `runServices`.
Persistente Daten liegen in benannten Volumes. Entwicklungsdienste veröffentlichen
keine Host-Ports; benötigte Oberflächen werden über VS Code weitergeleitet.

Keycloak verwendet ausschließlich den Entwicklungsmodus. Das mitgelieferte
Realm enthält noch keine Anwendungsclients oder Benutzer. Das Grafana-Dashboard
zeigt zunächst die Erreichbarkeit der Prometheus-Ziele; Anwendungsmetriken
werden bei einem entsprechenden Feature ergänzt.

Grafana-Dashboards und Provisionierung liegen im erzeugten Projekt unter
`config/observability/`. Anwendungsmigrationen gehören nach `db/migrations/`,
Produktionsartefakte nach `deploy/`.

## Einrichtung

### Voraussetzungen

- Python ab 3.11 für Generator und gemeinsame Prüfungen.
- Git; für GitHub-Aktionen zusätzlich die GitHub CLI und eine Anmeldung.
- Für Container: Docker mit Compose und eine Dev-Containers-fähige Umgebung.
- Für lokale Referenzen: ein vorhandenes Verzeichnis mit den anderen Repositories.

Im Template-Verzeichnis:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/create_project.py --help
```

### Befehle und Aufruforte

Terminalbefehle im Root des jeweiligen Projekts ausführen. Unter PowerShell
zeigt `Get-Location` den Ordner, unter Bash `pwd`. `python --version` muss
mindestens Python 3.11 anzeigen; falls die Umgebung nur `python3` bereitstellt,
diesen Interpreter entsprechend verwenden. Werkzeuge und Abhängigkeiten
müssen in der tatsächlich verwendeten Umgebung installiert sein.

| Terminalbefehl | Aussage und Zweck |
| --- | --- |
| `git status` | Branch sowie vorgemerkte, nicht vorgemerkte und unversionierte Änderungen ansehen. |
| `specify version` | Installierte CLI-Version und Laufzeitumgebung anzeigen; mit `speckit_version` in `config/project.yaml` vergleichen. |
| `specify check` | Verfügbarkeit unterstützter Agent-CLI-Werkzeuge prüfen; IDE-Integrationen werden übersprungen. |
| `specify integration list` | Verfügbare und installierte Integrationen sowie die Standardintegration ansehen. |
| `specify integration status` | Im initialisierten Projekt verwaltete Integrationsdateien und gemeinsame Spec-Kit-Struktur diagnostizieren. |
| `python scripts/status.py` | Den dokumentierten Arbeitsstand anzeigen. |
| `python scripts/check.py` | Dokumentlinks, Syntax und konfigurierte Projektprüfungen ausführen. |
| `git diff` / `git diff --cached` | Noch nicht vorgemerkte / bereits vorgemerkte Änderungen prüfen; neue unversionierte Dateien zusätzlich lesen. |

`specify check` ist ein Werkzeugcheck; die Projektprüfungen laufen über
`scripts/check.py` und die zusätzlichen Feature-Tests. Eine erfolgreiche
Versionsausgabe bestätigt noch keine eingerichtete Integration.
Die Unterscheidung folgt der [CLI-Referenz für 1.0.7](https://github.com/github/spec-kit/blob/v1.0.7/docs/reference/core.md)
und der [Integrationsreferenz für 1.0.7](https://github.com/github/spec-kit/blob/v1.0.7/docs/reference/integrations.md).

`uv` ist optional. Auch bei Installation über `uv tool install` die festgelegte
Version wählen, etwa `uv tool install specify-cli==1.0.7`. Die Profilanleitung
bestimmt Installation und Tests der Anwendung. `uv sync` und `uv run pytest`
sind hier keine profilübergreifenden Standardbefehle.

### Neues Projekt erzeugen

```sh
python scripts/create_project.py --name mein-projekt --stack python --output ../mein-projekt
python scripts/create_project.py --name meine-api --recipe api-service --service observability --output ../meine-api
```

Weitere Profile: `--stack typescript`, `--stack java-maven` oder `--stack none`.
Dienste werden mit wiederholtem `--service postgres`, `--service keycloak` und
`--service observability` ausgewählt. `--dry-run` zeigt die geplanten Dateien.

Das erzeugte Projekt enthält seinen eigenen Einstieg und sein DV-Konzept.
Template-Katalog, Generator-Tests und hiesige Rohmaterialien werden nicht
übernommen. So fließt das Sport-App-Konzept nicht in fachfremde Projekte ein.

Bei Verwendung von GitHubs „Use this template“ zunächst die neue Kopie als
Generator öffnen und das ausgewählte Projekt in ein leeres Ziel ausgeben.
**Include all branches** aktivieren, wenn `main` und `development` übernommen
werden sollen.
Ein Umbau eines bereits gefüllten Arbeitsverzeichnisses wird bewusst nicht
automatisch durchgeführt.

### Lokaler Container und Referenz-Repositories

Im zu öffnenden Projekt unter Windows:

```powershell
python scripts/container_init.py --references-root C:\Git
```

Unter Linux/macOS entsprechend:

```sh
python scripts/container_init.py --references-root /pfad/zu/repos
```

Danach „Reopen in Container“ in VS Code ausführen. Das Startskript erstellt
`.env` nur, wenn sie fehlt, und ersetzt `__GENERATE__` durch zufällige lokale
Passwörter. Bestehende Werte werden erhalten.

`.devcontainer/local.json` merkt sich den Hostpfad; das ignorierte
`compose.local.yaml` bindet ihn unter `/references/repos` mit `read_only: true`
ein. Alternativ setzt der Host `REFERENCE_REPOS_ROOT`. Keine Zugangsdaten in
diese Pfadkonfiguration schreiben.

Das aktuelle Projekt ist separat unter `/workspaces/project` schreibbar.
Der Referenz-Mount schützt die anderen Hostdateien vor Änderungen. Er erlaubt
weiterhin Lesen: Für einen bereinigten Kontext kann statt des gesamten
Arbeitsverzeichnisses eine Sammlung von Referenzklonen ohne lokale Secrets
eingebunden werden.

Der Container erhält keinen Host-Docker-Socket. Compose-Start und Verwaltung
der Nachbardienste erfolgen auf dem Host.

### Codespaces

Codespaces kann `C:\Git` nicht mounten. Dort keinen lokalen Referenzpfad setzen.
Die Konfiguration fordert für `maieuticus/*` nur `contents: read` und
`issues: write` an. Das aktuelle Arbeitsrepository hat seine eigenen Rechte.
Beim Wechsel des GitHub-Owners sowohl `config/repositories.yaml` als auch
`customizations.codespaces.repositories` anpassen.

Andere Repositories können im Codespace über `gh repo view OWNER/REPO` gelesen
oder in ein separates Referenzverzeichnis geklont werden. Der Token beschränkt
Schreibzugriffe auf die Remotes; solche lokalen Klone sind dadurch noch kein
schreibgeschützter Dateisystem-Mount. Für lokale Devcontainer müssen GitHub-
Zugangsdaten separat mit entsprechend begrenztem Umfang eingerichtet werden;
die Codespaces-Einstellungen beschränken keine weitergereichten Host-Tokens.

### Spec Kit initialisieren

Die Initialisierung erfolgt im Root-Verzeichnis des erzeugten Projekts.
Vorher dessen Abhängigkeiten installieren, die Dateien prüfen und den
Ausgangsstand in Git sichern. Der Generator führt kein `git init` aus.
Die vorhandene `.specify/memory/constitution.md` ist die mitgelieferte Grundlage;
eine zweite Constitution-Vorlage wird nicht gepflegt.

Im Container ist die festgelegte CLI installiert. Außerhalb kann `uvx` verwendet
oder `python -m pip install specify-cli==1.0.7` ausgeführt werden.

```sh
python scripts/init_speckit.py --integration codex
```

Das Skript initialisiert die gewählte Integration, lässt die Constitution
unverändert und verwendet die Bash-Skripte für die Arbeit im Linux-Container.
Andere unterstützte Integrationen können über `--integration` ausgewählt werden.
Die konkreten Agent-Dateien und Manifeste erzeugt Spec Kit.
Für Copilot beispielsweise `--integration copilot` verwenden; ohne Angabe
verwendet das Skript weiterhin Copilot.

Die lokalen Vorlagenanpassungen bleiben unter `.specify/templates/overrides/`.
Bei bereits initialisierten Projekten das Updateverfahren verwenden, nicht
erneut blind initialisieren.

#### Agent-Integration und Chat-Aufrufe

Mit `--integration` genau die gewünschte Integration wählen: `codex`,
`copilot` oder beispielsweise `cursor-agent`. Im Container nutzt das Init-Skript
Bash; für native PowerShell den unten beschriebenen Ablauf mit `--script ps`
verwenden. Der Agent muss in dieser Umgebung nutzbar sein.

Die folgenden Beispiele gehören in den **Agenten-Chat**, nicht ins Terminal:

| Integration in Spec Kit 1.0.7 | Beispiel | Installierte Dateien |
| --- | --- | --- |
| Codex | `$speckit-specify` | `.agents/skills/speckit-*/SKILL.md` |
| GitHub Copilot im Standardmodus | `/speckit-specify` | `.github/skills/speckit-*/SKILL.md` |

Bei anderen Agenten oder abweichenden Installationsmodi die tatsächlich
angebotenen Aufrufe verwenden. Die punktierte Schreibweise `/speckit.specify`
aus älteren Anleitungen und Referenztexten gilt nicht pauschal für jede
Integration. Die Schritte des [Feature-Ablaufs](#ablauf-je-feature) bleiben gleich.

#### Codex installieren

Codex muss in derselben Umgebung verfügbar sein, in der die Integration und
die Features ausgeführt werden. Der Devcontainer enthält Spec Kit, aber weder
Codex noch in jedem Technologieprofil Node.js. Für eine npm-Installation
Node.js mit npm in dieser Umgebung bereitstellen; alternativ einen zur
Plattform passenden Installer aus der
[offiziellen Codex-CLI-Anleitung](https://developers.openai.com/codex/cli) nutzen.

Unter Windows/PowerShell:

```powershell
npm.cmd install -g @openai/codex
codex.cmd --version
```

Unter Linux mit vorhandenem Node.js/npm entsprechend:

```sh
npm install -g @openai/codex
codex --version
```

Im Projektverzeichnis `codex.cmd` (Windows) beziehungsweise `codex` (Linux)
starten und beim ersten Start anmelden. Die `.cmd`-Starter funktionieren
unter PowerShell auch dann, wenn die Ausführung der `.ps1`-Starter durch die
Execution Policy blockiert ist.

#### Codex mit Windows PowerShell initialisieren

Für die Arbeit direkt unter Windows werden PowerShell-Skripte benötigt.
`scripts/init_speckit.py` unterstützt keinen `--script`-Parameter und wählt
immer `sh`. Für ein noch nicht initialisiertes Projekt deshalb den folgenden
Ablauf **im Root-Verzeichnis des erzeugten Projekts** verwenden. Git, Codex,
die Projektabhängigkeiten und `specify-cli==1.0.7` müssen installiert sein.

Zuerst Arbeitsverzeichnis, Version und Ausgangsstand prüfen:

```powershell
Get-Location
specify version
git status
```

Die CLI-Version muss zu `speckit_version` in `config/project.yaml` passen.
Den geprüften Ausgangsstand einschließlich Constitution vorher committen.
Anschließend diesen Block zusammenhängend in PowerShell ausführen:

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

`--here` wählt das aktuelle Projekt; `--force` erlaubt das bereits gefüllte
Verzeichnis. Der Block erhält die vorhandene Constitution auch bei einem
Fehler. Die übrigen erzeugten Änderungen danach mit `git status`, `git diff`
und durch Lesen neuer Dateien prüfen, insbesondere die lokalen Anpassungen
unter `.specify/templates/overrides/`. Bei einem Fehler den Zwischenstand
prüfen, bevor ein weiterer Initialisierungsversuch erfolgt.

Mit `specify integration list` die Installation kontrollieren. Die
[Codex-Integration von Spec Kit](https://github.com/github/spec-kit/blob/v1.0.7/docs/reference/integrations.md)
legt Skills unter `.agents/skills/speckit-*/SKILL.md` ab. Diese werden im
Codex-Chat als `$speckit-<name>` aufgerufen. Werden sie nicht erkannt, den
Projektordner und die installierte Integration prüfen und Codex neu starten;
siehe [Skill-Erkennung in Codex](https://developers.openai.com/codex/skills).

#### Bestehende Integrationen

`specify integration list` zeigt installierte Integrationen. Fehlt Codex in
einem bereits initialisierten Projekt, kann es mit
`specify integration install codex --script ps` ergänzt und mit
`specify integration use codex` als Standard gewählt werden. Im Linux-Container
stattdessen `--script sh` verwenden. Einen Austausch der bisherigen Integration
mit `specify integration switch codex` bewusst vornehmen.

Nach einem geplanten Versionsupdate werden die verwalteten Dateien mit
`specify integration upgrade codex` aktualisiert. Dabei den festgehaltenen
Versionsstand und das [Updateverfahren](#weiterentwicklung-und-versionen)
beachten. Ein erneutes `specify init --force` ist kein regulärer Updateweg.

## Entwicklung

### Wiedereinstieg und Pflege des Arbeitsstands

Der Link direkt unter dem README-Titel führt zum [aktuellen Arbeitsstand](#aktueller-arbeitsstand).
Im Projekt-Terminal zeigt derselbe Einstieg den gespeicherten Abschnitt an:

```sh
python scripts/status.py
```

Der Befehl liest ausschließlich das DV-Konzept und benötigt nur Python ab 3.11.
Er funktioniert auch vor der Git-Initialisierung und ohne Profilabhängigkeiten.
Der angegebene Stand ist eine gepflegte Zusammenfassung; die Anzeige führt
keinen Git-Abgleich und keine Tests aus. Fehlende oder leere Abschnitte werden
mit einer Fehlermeldung gemeldet.

In VS Code zeigt die Aufgabe „Projektstatus anzeigen“ den Abschnitt beim
Ordneröffnen im Terminal. Dafür dem Workspace vertrauen und in der
Befehlspalette über „Tasks: Manage Automatic Tasks“ automatische Aufgaben für
diesen Workspace erlauben. Über „Tasks: Run Task“ ist sie auch manuell
ausführbar. Python muss in der geöffneten Umgebung verfügbar sein.

Agenten gleichen den Arbeitsstand zu Beginn einer neuen Arbeitssitzung mit
Git und den relevanten Feature-Aufgaben ab und zeigen den Überblick in ihrer
ersten inhaltlichen Antwort. Das bloße Öffnen eines Ordners startet keinen
Codex-Chat. Nach wesentlichen beauftragten Änderungen und vor einer Übergabe
werden Datum, aktives Feature, Erledigtes, laufende Arbeit, priorisierte nächste
Schritte, Blockaden und tatsächlich ausgeführte Prüfungen hier aktualisiert.
Details bleiben in den verlinkten Feature-Aufgaben und Prüfergebnissen.

Neue Projekte erhalten diese Einstiege und einen eigenen Anfangsstand mit
Erzeugungsdatum. Bestehende Projekte übernehmen die Änderungen gezielt nach
dem [Updateverfahren](#weiterentwicklung-und-versionen).

### Ablauf je Feature

1. Rohmaterial und relevantes Wissen lesen; Projektziel im DV-Konzept klären.
2. Ein abgegrenztes Feature mit Akzeptanzkriterien spezifizieren.
3. Unklare Anforderungen klären und die technische Umsetzung planen.
4. Aufgaben aus Plan und Spec ableiten; Konsistenz prüfen.
5. Implementieren und relevante Tests ausführen.
6. Ergebnis gegen die Akzeptanzkriterien prüfen; Lücken nacharbeiten.
7. Betroffene Abschnitte dieses Konzepts aktualisieren und den Diff prüfen.

#### Vorhandene Unterlagen in kleine Features überführen

Rohmaterialien zuerst auf Quelle, Stand, Widersprüche und konkreten Nutzen
prüfen. Abgestimmte Projektziele und Grundsatzentscheidungen hierher übernehmen;
einzelne Anforderungen in `specs/<nummer>-<name>/spec.md` überführen.
Beispiele aus fremden Projekten legen weder Technologie noch Ordnerstruktur
des neuen Projekts fest.

Die erste Spezifikation beschreibt Nutzerziel, beobachtbares Verhalten,
Akzeptanzkriterien und ausdrücklich ausgeschlossenen Umfang. Bestehende
technische Randbedingungen berücksichtigen; neue Implementierungsentscheidungen
im anschließenden `plan.md` begründen. Aus einem großen Konzept zunächst einen
kleinen, unabhängig prüfbaren Funktionsumfang auswählen. Zusätzliche Dienste,
Verzeichnisse und spätere Ausbaustufen erst bei einem konkreten Bedarf ergänzen.

Vor der Spec-Kit-Initialisierung den geprüften Ausgangsstand lokal sichern;
die anschließend erzeugten Integrationsdateien separat prüfen und committen.
So bleiben Projektgrundlage und Werkzeugeinrichtung in Git nachvollziehbar.
Zum Abschluss eines Features die vorgesehenen Dateien gezielt mit
`git add -- <geprüfte-dateien>` vormerken (Platzhalter ersetzen), mit
`git diff --cached` prüfen und lokal committen. Ein Push ist ein eigener
Veröffentlichungsschritt im beauftragten Umfang.

#### Manueller Ablauf mit Codex

Zu Projektbeginn einmal `$speckit-constitution` im Codex-Chat aufrufen.
Der Agent liest zuerst `AGENTS.md`, README, dieses DV-Konzept, die bestehende
Constitution sowie Code und Tests. Projektziel und Grundsatzentscheidungen
werden hier konkretisiert; notwendige Änderungen der Constitution werden
begründet und versioniert. Die Constitution enthält dauerhafte Regeln,
einzelne Feature-Anforderungen gehören in die jeweilige Spezifikation.

Für jedes abgegrenzte Feature die folgenden Skills einzeln im Codex-Chat
aufrufen und ihre Ergebnisse vor dem nächsten Schritt prüfen:

| Schritt | Zweck und Ergebnis |
| --- | --- |
| `$speckit-specify` | Gewünschtes Verhalten, Nutzen und überprüfbare Akzeptanzkriterien in `specs/<nummer>-<name>/spec.md` festhalten; bestehenden Projektkontext berücksichtigen. |
| `$speckit-clarify` | Offene Anforderungen, Randfälle und Widersprüche vor der Planung klären. |
| `$speckit-plan` | Technische Umsetzung in `plan.md` beschreiben; gewähltes Profil, vorhandene Architektur, Verträge, Migrationen und relevante Tests berücksichtigen. |
| `$speckit-checklist` | Qualität, Eindeutigkeit und Vollständigkeit der Anforderungen prüfen; ersetzt keinen Test der Implementierung. |
| `$speckit-tasks` | Ausführbare Aufgaben in `tasks.md` aus Spezifikation und Plan ableiten. |
| `$speckit-analyze` | Constitution, Spezifikation, Plan und Aufgaben auf Konsistenz prüfen; wesentliche Befunde vor der Implementierung beheben. |
| `$speckit-implement` | Geplante Aufgaben einschließlich Code und relevanter Tests umsetzen. |
| `$speckit-converge` | Umsetzung und Artefakte gegen die Anforderungen prüfen; verbleibende Lücken in Aufgaben überführen. |

Clarify und Checklist werden nach Bedarf eingesetzt; vor größeren Umsetzungen
gehört Analyze dazu. Bestehende APIs, Datenmodelle, Tests und Build-/Deployment-
Konfigurationen beim Spezifizieren und Planen berücksichtigen. Zusätzliche
Abhängigkeiten und Architekturänderungen begründen, Breaking Changes benennen.

Zum Abschluss `python scripts/check.py` und die im Feature geplanten Prüfungen
ausführen, die Akzeptanzkriterien abgleichen und tatsächliche Prüfergebnisse
festhalten. Offene Aufgaben aus `converge` umsetzen, erneut testen und abgleichen.
Vor einem Commit auch neue Dateien prüfen; `git diff` zeigt unversionierte
Dateien nicht. Kleine Korrekturen brauchen nur einen angemessenen Prozess.

#### Automatisierter Workflow

Der lokale Workflow liegt unter
`.specify/workflows/project-sdd/workflow.yml`:

```sh
specify workflow run .specify/workflows/project-sdd/workflow.yml -i spec="Ein abgegrenztes Feature"
```

Vor dem automatisierten Lauf müssen fachliche Unklarheiten geklärt sein.
`converge` kann weitere Aufgaben erzeugen. Der abschließende Review prüft diese
Aufgaben; ein durchgelaufener Workflow allein bedeutet keine fachliche Abnahme.
Bei Lücken Implementierung, Prüfungen und Abgleich wiederholen.

### Gemeinsame Prüfungen

```sh
python scripts/check.py
python scripts/check.py --static-only
```

Das Skript prüft lokale Dokumentlinks, Anker, Python-/JSON-/YAML-Syntax und
unzulässige parallele Konzeptdokumente. Danach führt es die Argumentlisten aus
`config/project.yaml` ohne Shell aus. Im Template sind das die Generator-Tests,
im erzeugten Projekt die jeweiligen Anwendungstests.

Die CI prüft zusätzlich generierte Python-, TypeScript-, Maven- und API-Projekte,
Compose-Konfigurationen sowie den Bau der Entwicklungsimages. API-CI verwendet
eine wegwerfbare PostgreSQL-Datenbank und übernimmt ihre Werte aus genau einer
`.env.test.example`. Ein nicht ausgeführter Containerstart darf nicht als
erfolgreich geprüft dokumentiert werden.

### API-Rezept

Das Rezept enthält eine minimale `/health`-Route, einen eingecheckten OpenAPI-
Vertrag und Tests für Vertrag/Implementierung und interne Referenzen.
`/health` ist ein Liveness-Check, kein Nachweis der Datenbankbereitschaft.
Ein eigener Datenbanktest läuft mit `RUN_DATABASE_TESTS=1`; sonst wird er
sichtbar übersprungen.

API-Änderungen planen Vertrag, Verbraucher, Validierung und Fehlerfälle.
Datenänderungen planen Migration, Backup und Rückweg. Nach dem ersten
Abhängigkeitsabgleich einen geeigneten Lock-/Constraint-Stand festhalten.

## Betrieb

### Lokale Entwicklungsdienste

Nach `python scripts/container_init.py` auf dem Docker-Host:

```sh
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.local.yaml config --quiet
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.local.yaml ps
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.local.yaml logs --tail 100
docker compose -f .devcontainer/compose.yaml -f .devcontainer/compose.local.yaml down
```

`down` erhält die benannten Volumes. `down --volumes` löscht Dienstdaten und
gehört nicht zum normalen Arbeitsablauf.

### Deployment und Datenänderungen

Das Template selbst wird nicht produktiv betrieben. Erzeugte Anwendungen
ergänzen hier ihre konkreten Bereitstellungsschritte, Umgebungen,
Verantwortlichkeiten, Backups und Wiederherstellungsverfahren.

Das API-Rezept enthält einen Anwendungs-Dockerfile unter `deploy/`.
Entwicklungs-Keycloak, Testpasswörter und lokale Compose-Dienste sind keine
Produktionskonfiguration.

Vor einer Schemaänderung werden Datenmodell, Migration, Tests und Rückweg
gemeinsam geplant. Das ergänzende SQL-Skript des API-Katalogs setzt idempotente
Migrationen voraus; alternativ ein passendes Migrationswerkzeug wählen.
`db/init.sql` darf nur eine frische Testdatenbank initialisieren und ist kein
Produktionsmigrationsverfahren. Ein Backup liegt außerhalb des Git-Verzeichnisses.

### Störungen

| Symptom | Prüfung |
| --- | --- |
| Containerstart meldet fehlendes Override | `python scripts/container_init.py` auf dem Host ausführen |
| Referenzordner fehlt | Hostpfad, `local.json` und `REFERENCE_REPOS_ROOT` prüfen |
| PostgreSQL lehnt Anmeldung ab | Vorhandene Volume-Daten und tatsächliche `.env` vergleichen; neue Env-Werte ändern vorhandene DB-Benutzer nicht automatisch |
| API-Vertragstest schlägt fehl | Beabsichtigte Vertragsänderung prüfen; Implementierung und Vertrag gemeinsam aktualisieren |
| Agent-Aufruf fehlt | Installierte Integration und deren Aufrufsyntax prüfen |

## Wissensaustausch

| Ergebnis | Ziel |
| --- | --- |
| Projektarchitektur und Betrieb | Dieses DV-Konzept |
| Allgemeines Technologiewissen | `tech-knowledge-base` |
| Gemeinsame Infrastrukturkenntnisse | Infrastrukturartikel der Knowledge Base |
| Wiederverwendbare Dateien und Abläufe | `template-spec-kit` |

Die Knowledge Base verwendet `tNNNN-…` für Technologien und `iNNNN-…` für
Infrastruktur. Zuerst bestehende Artikel und ihre `AGENTS.md` lesen. Wissen
bevorzugt verlinken; relevante Versionen bei Architekturentscheidungen festhalten.

Ein Verbesserungs-Issue kann bei vorhandenem Auftrag über die GitHub CLI im
ausdrücklich genannten Repository erstellt werden. Dafür ist kein
`contents: write` erforderlich.

Für eine konkrete Dateiänderung:

```sh
python scripts/prepare_contribution.py knowledge --output .artifacts/contributions/knowledge --branch improve/postgres-notes
```

Das Skript klont ausschließlich das konfigurierte Ziel und erstellt einen
Arbeitsbranch. Es veröffentlicht nichts. Nach Prüfung kann der Branch mit
gezielten Rechten in das Ziel oder einen geeigneten Fork gepusht und ein PR
erstellt werden. `pull_requests: write` allein erlaubt keinen Branch-Push.
Die Referenzkopie bleibt unverändert.

## Weiterentwicklung und Versionen

Template-Version und verwendete Spec-Kit-Version stehen in `config/project.yaml`.
Neue Projekte erhalten zusätzlich den Ausgangscommit; `+working-tree` kennzeichnet
eine Erzeugung aus noch nicht vollständig eingecheckten Änderungen.

Template-Updates werden als gezielte Änderungen geprüft. Der Generator ist kein
Synchronisationswerkzeug für bestehende Anwendungen. Spec-Kit-Updates zunächst
an einem Testprojekt prüfen; bei bestehenden Integrationen den
manifestgestützten `specify integration upgrade`-Weg verwenden.

Neu ausgewählte Dienste erst nach Konfigurations- und Startprüfung in den
Katalog aufnehmen. Projektanforderungen, aktive Konfiguration und dieses
Dokument bei Änderungen zusammenführen.

## Prüfstatus

### Konsolidierung der Spec-Kit-Unterlagen – 23.09.2026

| Prüfung | Ergebnis |
| --- | --- |
| `python scripts/check.py` | Dokumentlinks, Anker, Dateisyntax und alle 14 Tests erfolgreich; erzeugte Projekte eingeschlossen |
| Befehlsbedeutung und Aufrufsyntax | Mit den CLI- und Integrationsreferenzen für Spec Kit 1.0.7 abgeglichen |
| Umfang der Bereinigung | Zwei allgemeine Spec-Kit-Rohdateien entfernt; Boardgame- und Sport-App-Unterlagen unverändert erhalten |
| Spec-Kit-Initialisierung, Agenten-Chat, interaktiver VS-Code-Start und CI | In dieser Sitzung nicht ausgeführt |

### Arbeitsstand beim Wiedereinstieg – 23.09.2026

| Prüfung | Ergebnis |
| --- | --- |
| `python scripts/check.py` | Dokumentlinks, Anker, Dateisyntax und alle 14 Tests erfolgreich |
| Status in erzeugten Projekten | Alle vier Profile und API-Rezept erfolgreich; Aufruf aus fremdem Arbeitsverzeichnis ohne Git oder Zusatzpakete, keine Dateiveränderungen |
| Fehlerfälle und Abschnittsgrenzen | Fehlende, leere und unlesbare Dokumente/Abschnitte sowie Überschriften in Codeblöcken geprüft |
| `python scripts/status.py` | Übersicht des Templates erfolgreich ausgegeben |
| VS-Code-Aufgabe | Konfiguration und tatsächlicher Statusbefehl automatisiert geprüft; interaktiver Start beim Ordneröffnen noch nicht ausgeführt (T006) |
| Neue Codex-Arbeitssitzung | Agentenregeln ergänzt; Anzeige in einer neu gestarteten Sitzung nicht separat geprüft |
| GitHub Actions und Laufzeitprüfungen der Profile | In dieser Sitzung nicht ausgeführt; bisheriger Stand unten |
| Branches des Templates | `main` und `development` auf `origin` veröffentlicht; Übernahme in neue Projekte über **Include all branches** dokumentiert |

### Bisherige Prüfung des Grundgerüsts

Stand der lokalen Überprüfung am 16.09.2026:

| Prüfung | Ergebnis |
| --- | --- |
| Dokumentlinks, Anker und Python-/JSON-/YAML-Syntax | Erfolgreich |
| Neun Generator- und Containerkonfigurationstests | Erfolgreich |
| Erzeugtes Python-Projekt: Paketbau, Installation und Importtest | Erfolgreich |
| Erzeugtes TypeScript-Projekt: Installation, Typprüfung und Node-Test | Erfolgreich |
| Erzeugtes API-Projekt: Paketbau und API-/Vertragstests | Vier Tests erfolgreich |
| API-Datenbanktest | Übersprungen; keine laufende PostgreSQL-Testinstanz |
| Maven-Build | Lokal nicht ausgeführt; JDK/Maven fehlen |
| Compose-Schema, Image-Bau und Dienststart | Lokal nicht ausgeführt; Docker fehlt |
| Spec-Kit-Initialisierung und Workflow-Validierung | CLI-Start durch Windows-Anwendungssteuerung blockiert |
| GitHub Actions | Konfiguriert, in dieser Sitzung nicht ausgeführt |

Die noch offenen Laufzeitprüfungen sind in der CI hinterlegt. Syntaxprüfungen
und Konfigurationstests ersetzen keinen erfolgreichen Containerstart.

## Quellen

- [VS-Code-Aufgaben beim Ordneröffnen](https://code.visualstudio.com/docs/debugtest/tasks#_run-behavior)
- [Projektanweisungen für Codex](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Spec-Kit-Anpassungen](https://github.github.io/spec-kit/guides/customization.html)
- [Spec-Kit-Workflows](https://github.github.io/spec-kit/reference/workflows.html)
- [Spec-Kit-Integrationen](https://github.github.io/spec-kit/reference/integrations.html)
- [Spec-Kit-CLI-Befehle, Stand 1.0.7](https://github.com/github/spec-kit/blob/v1.0.7/docs/reference/core.md)
- [Spec-Kit-Agent-Aufrufe und Integrationsdiagnose, Stand 1.0.7](https://github.com/github/spec-kit/blob/v1.0.7/docs/reference/integrations.md)
- [Spec Kit 1.0.7](https://github.com/github/spec-kit/releases/tag/v1.0.7)
- [Docker-Bind-Mounts](https://docs.docker.com/engine/storage/bind-mounts/)
- [Devcontainer-Mounts und Codespaces](https://code.visualstudio.com/remote/advancedcontainers/add-local-file-mount)
- [Codespaces-Repository-Rechte](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-repository-access-for-your-codespaces)
- [Maven-Projektstruktur](https://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
- [TypeScript in Node.js](https://nodejs.org/api/typescript.html)
- [Keycloak-Container](https://www.keycloak.org/server/containers)
- [Grafana in Docker](https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/)
