# Quickstart

Schon eingerichtet? Direkt zum
[aktuellen Arbeitsstand](docs/DV_KONZEPT.md#aktueller-arbeitsstand).
Im Terminal zeigt `python scripts/status.py` denselben Stand an.

Die verbindlichen Schritte und Voraussetzungen stehen im
[DV-Konzept – Einrichtung](docs/DV_KONZEPT.md#einrichtung).

1. Python ab 3.11 bereitstellen und `python -m pip install -r scripts/requirements.txt` ausführen.
2. Ein neues Projekt mit `python scripts/create_project.py --name mein-projekt --stack python --output ../mein-projekt` erzeugen.
3. Das erzeugte Projekt öffnen und dessen README folgen.
4. Projektziel, Architektur, Entwicklung und Betrieb im dortigen `docs/DV_KONZEPT.md` konkretisieren.
5. Spec Kit für die gewünschte Agent-Integration initialisieren und das erste kleine Feature spezifizieren.

Terminalbefehle und ihre Bedeutung erklärt die
[Befehlsübersicht](docs/DV_KONZEPT.md#befehle-und-aufruforte).
Für Codex und Copilot gelten unterschiedliche
[Chat-Aufrufe](docs/DV_KONZEPT.md#agent-integration-und-chat-aufrufe).

Für die Arbeit am Template selbst gelten
[Entwicklung und Prüfungen](docs/DV_KONZEPT.md#entwicklung).
