"""Show the documented project status without changing project files."""

from pathlib import Path
import re
import sys


def status_section(document: str) -> str:
    """Read the agreed level-two section, preserving subheadings and code blocks."""
    lines = []
    active = False
    fence = ""
    for line in document.splitlines():
        if fence:
            if active:
                lines.append(line)
            if re.fullmatch(r" {0,3}" + re.escape(fence[0]) + r"{" + str(len(fence)) + r",}\s*", line):
                fence = ""
            continue
        opening = re.match(r" {0,3}(`{3,}|~{3,})", line)
        if opening:
            fence = opening.group(1)
        elif active and re.match(r"#{1,2}\s", line):
            break
        elif line.rstrip() == "## Aktueller Arbeitsstand":
            active = True
        if active:
            lines.append(line)
    if not active:
        raise ValueError("Abschnitt '## Aktueller Arbeitsstand' fehlt im DV-Konzept.")
    if not any(line.strip() for line in lines[1:]):
        raise ValueError("Abschnitt '## Aktueller Arbeitsstand' ist leer.")
    return "\n".join(lines).strip()


def main() -> int:
    # Keep German text readable in terminals and redirected Windows output.
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
    concept = Path(__file__).resolve().parents[1] / "docs/DV_KONZEPT.md"
    try:
        section = status_section(concept.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Projektstatus nicht verfügbar: {error}\nQuelle: {concept}", file=sys.stderr)
        return 1
    print(section)
    print(f"\nQuelle: {concept}")
    print("Dokumentierter Stand; kein automatischer Abgleich mit Git oder Tests.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
