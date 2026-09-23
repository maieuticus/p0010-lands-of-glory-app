# Feature 002: Arbeitsstand beim Wiedereinstieg

## Ziel

Beim Öffnen eines Projekts sollen die zuletzt erledigten und die nächsten
geplanten Schritte schnell auffindbar sein. Der verbindliche Arbeitsstand
bleibt im DV-Konzept; Feature-Aufgaben bleiben in ihrer jeweiligen `tasks.md`.

## Akzeptanzkriterien

1. Die README des Templates und jedes erzeugten Projekts verlinkt direkt unter
   dem Titel auf `docs/DV_KONZEPT.md#aktueller-arbeitsstand`.
2. Der Abschnitt steht am Anfang des DV-Konzepts und enthält Standdatum,
   aktives Feature, zuletzt Erledigtes, laufende Arbeit, priorisierte nächste
   Schritte sowie Blockaden und den tatsächlichen Prüfstatus.
3. `python scripts/status.py` zeigt genau diesen dokumentierten Abschnitt an,
   ohne Projektdateien zu verändern. Der Aufruf funktioniert auch aus einem
   anderen Arbeitsverzeichnis und ohne Git-Repository oder Zusatzpakete.
   Fehlende, leere oder unlesbare Statusabschnitte führen zu einer verständlichen
   Fehlermeldung und einem Rückgabewert ungleich null.
4. Eine VS-Code-Aufgabe zeigt denselben Status beim Öffnen im Terminal an,
   sofern der Workspace vertraut ist und automatische Aufgaben erlaubt sind.
   Sie ist auch manuell ausführbar; bestehende Prüfaufgaben bleiben erhalten.
5. Agentenregeln verlangen einen abgeglichenen Überblick zu Beginn einer neuen
   Arbeitssitzung und die Pflege nach wesentlichen beauftragten Änderungen
   sowie vor einer Übergabe. Der gespeicherte Stand wird nicht als automatisch
   aktuell oder als Nachweis nicht ausgeführter Prüfungen ausgegeben.
6. Erzeugte Projekte erhalten einen datierten Anfangsstand mit ihren nächsten
   Einrichtungsschritten. Arbeitsverlauf und Features des Templates werden
   nicht übernommen; bestehende Projekte werden nicht automatisch geändert.

## Abgrenzung

Keine zusätzliche Statusdatenbank, kein zweites Konzeptdokument und keine
Ableitung fachlicher Prioritäten allein aus Git-Commits oder Checkboxen.
Die Anzeige im Codex-Chat erfolgt bei der ersten Antwort einer neuen
Arbeitssitzung; eine Agentenregel löst beim bloßen Ordneröffnen keinen Chat aus.

## Nachweise

Automatisierte Prüfungen und der manuelle VS-Code-Starttest stehen in
[plan.md](plan.md) und [tasks.md](tasks.md). Der aktuelle Projektstand bleibt
im [DV-Konzept](../../docs/DV_KONZEPT.md#aktueller-arbeitsstand).
