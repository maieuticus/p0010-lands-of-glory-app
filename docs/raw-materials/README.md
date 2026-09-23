# Rohmaterialien

Hier liegen ursprüngliche Unterlagen. Sie sind Eingaben für die Spezifikation,
keine zusätzliche verbindliche Architektur- oder Betriebsanleitung.

- [Sport-App-Konzept](sport_app_gesamtkonzept_implementierungsleitfaden.md):
  vorhandene projektspezifische Eingabe, bei der Umstrukturierung unverändert erhalten.
- [Historischer Boardgame-Quickstart](boardgame-quickstart.md):
  bisheriges Beispiel; dessen Struktur und Kommandos sind nicht die aktuelle Template-Anleitung.

Neue Projekte erhalten einen leeren Rohmaterialbereich. Diese Unterlagen werden
vom Generator nicht kopiert.

## Auswertung der Spec-Kit-Unterlagen am 23.09.2026

Die allgemeinen Inhalte wurden mit dem Template und der Dokumentation von
Spec Kit 1.0.7 abgeglichen. Die aktuellen Erklärungen stehen im DV-Konzept und
in den entsprechenden Basisvorlagen für neu erzeugte Projekte.

| Rohmaterial | Übernahme und Verbleib |
| --- | --- |
| `SpecKit - quickstart.md` | Einrichtung, Terminal-/Chat-Trennung und kleine Feature-Schritte in [Einrichtung](../DV_KONZEPT.md#einrichtung) und [Feature-Ablauf](../DV_KONZEPT.md#ablauf-je-feature) übernommen; überholte Rohdatei entfernt. |
| `spec-kit-quickstart.md` | Kurzbeschreibungen in [Befehle und Aufruforte](../DV_KONZEPT.md#befehle-und-aufruforte) konsolidiert und korrigiert; doppelte Rohdatei entfernt. |
| [Boardgame-Quickstart](boardgame-quickstart.md) | Allgemeine Hinweise zum Sichten vorhandener Unterlagen, getrennten Ausgangs-/Initialisierungscommits und kleinen Feature-Schnitten übernommen. Wegen eigenständiger Spielanforderungen und Projektstruktur als historische Eingabe erhalten. |

Bewusst angepasst wurden die Installation auf die festgelegte CLI-Version,
die agentabhängigen Chat-Aufrufe und die Bedeutung von `specify check`
(Werkzeugverfügbarkeit). Profilabhängige `uv`-/pytest-Kommandos, pauschales
`git add .` und ein automatischer Push wurden nicht als Standard übernommen.
Die Initialisierung folgt dem vorhandenen Ablauf zum Erhalt der Constitution;
getrennte Architekturdateien aus dem Boardgame-Beispiel ersetzen das DV-Konzept nicht.

Das Sport-App-Konzept war nicht Teil dieser Spec-Kit-Auswertung und bleibt
unverändert. Weitere Rohmaterialien erst nach Prüfung ihrer noch nicht
übernommenen Inhalte und im beauftragten Umfang entfernen.
