"""Verify status display and its wiring in generated projects."""

from contextlib import redirect_stdout
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from create_project import create_project, render_files
from status import status_section


class StatusTests(unittest.TestCase):
    def test_only_status_section_is_shown_including_subheadings(self):
        section = (
            "## Aktueller Arbeitsstand\n\n**Stand:** 2026-09-23\n\n"
            "### Zuletzt erledigt\n\n- Einrichtung abgeschlossen.\n\n"
            "### Nächste Schritte\n\n1. Erstes Feature planen."
        )
        for boundary in ("## Inhalt", "# Anhang"):
            with self.subTest(boundary=boundary):
                document = "# Projekt\n\n" + section + "\n\n" + boundary + "\n\nAnderer Inhalt."
                self.assertEqual(status_section(document.replace("\n", "\r\n")), section)
        self.assertEqual(status_section(section), section)

    def test_headings_inside_code_blocks_do_not_start_or_end_the_section(self):
        for fence in ("```", "~~~~"):
            with self.subTest(fence=fence):
                example = f"{fence}markdown\n## Aktueller Arbeitsstand\nBeispiel\n{fence}\n"
                section = (
                    "## Aktueller Arbeitsstand\n\n### Nächste Schritte\n\n"
                    f"{fence}markdown\n## Beispielüberschrift\n{fence}\n\nWeiterarbeiten."
                )
                self.assertEqual(status_section(example + section + "\n\n## Inhalt"), section)

    def test_missing_or_empty_status_is_reported(self):
        for document in ("# Projekt\n", "```\n## Aktueller Arbeitsstand\n```"):
            with self.subTest(document=document), self.assertRaisesRegex(ValueError, "fehlt"):
                status_section(document)
        for document in ("## Aktueller Arbeitsstand\n", "## Aktueller Arbeitsstand\n\n## Inhalt"):
            with self.subTest(document=document), self.assertRaisesRegex(ValueError, "leer"):
                status_section(document)

    def test_cli_reports_unavailable_documents_without_traceback(self):
        cases = (
            (None, "Projektstatus nicht verfügbar"),
            (b"\xff", "Projektstatus nicht verfügbar"),
            (b"# Projekt\n", "fehlt"),
            (b"## Aktueller Arbeitsstand\n", "leer"),
        )
        for content, message in cases:
            with self.subTest(content=content), TemporaryDirectory() as directory:
                root = Path(directory)
                (root / "scripts").mkdir()
                (root / "docs").mkdir()
                script = root / "scripts/status.py"
                shutil.copyfile(ROOT / "scripts/status.py", script)
                if content is not None:
                    (root / "docs/DV_KONZEPT.md").write_bytes(content)
                result = subprocess.run(
                    [sys.executable, "-B", "-S", "-X", "utf8", str(script)],
                    cwd=ROOT, capture_output=True, encoding="utf-8", check=False,
                )
                self.assertEqual(result.returncode, 1)
                self.assertEqual(result.stdout, "")
                self.assertIn(message, result.stderr)
                self.assertIn("DV_KONZEPT.md", result.stderr)
                self.assertNotIn("Traceback", result.stderr)

    def test_generated_projects_display_their_own_status_without_writing_files(self):
        profiles = [(stack, None) for stack in ("none", "python", "typescript", "java-maven")]
        profiles.append(("none", "api-service"))
        for stack, recipe in profiles:
            with self.subTest(stack=stack, recipe=recipe), TemporaryDirectory() as directory:
                root = Path(directory) / "Projekt mit Leerzeichen"
                with redirect_stdout(io.StringIO()):
                    create_project(root, render_files("new-project", stack, [], recipe))
                before = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                concept = (root / "docs/DV_KONZEPT.md").read_text(encoding="utf-8")
                readme = (root / "README.md").read_text(encoding="utf-8")
                self.assertIn("(docs/DV_KONZEPT.md#aktueller-arbeitsstand)", readme.split("## Start")[0])
                self.assertRegex(concept, r"\*\*Stand:\*\* \d{4}-\d{2}-\d{2} \(Projekterzeugung\)")
                self.assertNotIn("{{CREATED_DATE}}", concept)
                self.assertNotIn("002-projektstatus", concept)
                self.assertFalse((root / ".git").exists())
                tasks = json.loads((root / ".vscode/tasks.json").read_text(encoding="utf-8"))["tasks"]
                task = next(task for task in tasks if task["label"] == "Projektstatus anzeigen")
                self.assertEqual(task["type"], "process")
                self.assertEqual(task["command"], "python")
                self.assertEqual(task["runOptions"]["runOn"], "folderOpen")
                self.assertEqual(task["presentation"]["reveal"], "always")
                self.assertFalse(task["presentation"]["focus"])
                self.assertTrue(any(task["label"] == "Projekt prüfen" for task in tasks))
                args = [arg.replace("${workspaceFolder}", str(root)) for arg in task["args"]]
                # Run the task from elsewhere without site packages, even with an ASCII default.
                result = subprocess.run(
                    [sys.executable, "-B", "-S", *args],
                    cwd=directory, capture_output=True, encoding="utf-8", check=False,
                    env={**os.environ, "PYTHONIOENCODING": "ascii"},
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stderr, "")
                self.assertIn(status_section(concept), result.stdout)
                self.assertIn("Grundgerüst", result.stdout)
                self.assertIn("Noch keine Projektprüfungen", result.stdout)
                self.assertNotIn("{{", result.stdout)
                after = {path.relative_to(root): path.read_bytes() for path in root.rglob("*") if path.is_file()}
                self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
