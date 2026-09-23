# Plan: Arbeitsstand beim Wiedereinstieg

## Umsetzung

- Im DV-Konzept einen Abschnitt `## Aktueller Arbeitsstand` vor dem
  Inhaltsverzeichnis pflegen. Unterüberschriften strukturieren den Stand;
  Verweise führen zu Feature-Aufgaben und ausführlichen Prüfergebnissen.
- README und Quickstart verlinken den Abschnitt. Die Basisvorlagen erhalten
  dieselbe Struktur mit eigenem Anfangsstand und Erzeugungsdatum.
- `scripts/status.py` liest den Abschnitt mit der Python-Standardbibliothek
  vom Pfad relativ zum Skript. Die Ausgabe endet vor der nächsten Überschrift
  der Ebene 1 oder 2; Überschriften in Codeblöcken begrenzen sie nicht.
- Den Statusbefehl in den Generatorkern aufnehmen. Die gemeinsame
  `.vscode/tasks.json` erhält eine Aufgabe mit `runOn: folderOpen`, sichtbarem
  Terminal und ohne Fokuswechsel. Die Erlaubnis für automatische Aufgaben
  bleibt eine lokale Entscheidung in VS Code.
- Pflege und Abgleich in `AGENTS.md`, im Entwicklungsablauf und in der
  vorhandenen Aufgaben-Vorlage festhalten.

## Prüfung

- `python scripts/check.py`: Dokumentlinks einschließlich README-Anker,
  Dateisyntax und alle Template-Tests.
- `tests/test_status.py`: Abschnittsgrenzen einschließlich Codeblöcken,
  fehlender/leerer Abschnitt, fehlendes/unlesbares Dokument; tatsächlicher
  Statusaufruf in erzeugten Projekten aller Profile und des API-Rezepts aus
  einem fremden Arbeitsverzeichnis; keine Dateiveränderungen durch die Anzeige.
- `python scripts/status.py`: Übersicht dieses Repositories kontrollieren.
- Manuell in VS Code: vertrauenswürdigen Workspace öffnen, automatische
  Aufgaben erlauben, sichtbare Ausgabe und erneutes Öffnen prüfen. Die Aufgabe
  außerdem über „Tasks: Run Task“ ausführen und mit dem DV-Konzept vergleichen.
  Eine hier nicht mögliche interaktive Prüfung ausdrücklich offen lassen.

## Abhängigkeiten

Keine neuen Pakete oder Dienste. Python ab 3.11 ist bereits Voraussetzung.
Der Statusbefehl benötigt keine installierten Profilabhängigkeiten.
