import filecmp
import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
ROOT_SKILL = ROOT / "payoff-evaluator"
CURSOR_SKILL = ROOT / ".cursor" / "skills" / "payoff-evaluator"
REFERENCE = ROOT_SKILL / "references" / "evaluation-framework.md"
EXAMPLES = ROOT_SKILL / "references" / "examples.md"
OPENAI_YAML = ROOT_SKILL / "agents" / "openai.yaml"
SYNC_SCRIPT = ROOT / "scripts" / "sync_skill_copies.py"
VALIDATE_SCRIPT = ROOT / "scripts" / "validate_skill_repo.py"


class SkillRepoIntegrityTests(unittest.TestCase):
    def test_skill_md_uses_progressive_disclosure(self) -> None:
        skill = (ROOT_SKILL / "SKILL.md").read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")

        self.assertIn("读取 `references/evaluation-framework.md`", skill)
        self.assertIn("读取 `references/examples.md`", skill)
        self.assertIn("## Table of contents", reference)
        self.assertLess(len(skill.splitlines()), len(reference.splitlines()))

    def test_cursor_copy_matches_root_skill(self) -> None:
        compared = filecmp.dircmp(ROOT_SKILL, CURSOR_SKILL)
        self.assertEqual(compared.left_only, [])
        self.assertEqual(compared.right_only, [])
        self.assertEqual(compared.diff_files, [])

    def test_examples_are_split_from_core_reference(self) -> None:
        reference = REFERENCE.read_text(encoding="utf-8")
        examples = EXAMPLES.read_text(encoding="utf-8")

        self.assertIn("read `references/examples.md`", reference)
        self.assertIn("## Refactor", examples)
        self.assertNotIn("## 10. Examples", reference)

    def test_openai_yaml_matches_skill_creator_constraints(self) -> None:
        text = OPENAI_YAML.read_text(encoding="utf-8")

        self.assertIn('display_name: "Payoff Evaluator"', text)
        self.assertIn('default_prompt: "Use $payoff-evaluator', text)
        self.assertIn("short_description:", text)

    def test_frontmatter_description_keeps_trigger_coverage(self) -> None:
        skill = (ROOT_SKILL / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", skill, re.DOTALL)
        self.assertIsNotNone(match)
        frontmatter = match.group(1)

        self.assertIn("是否", frontmatter)
        self.assertIn("worth it", frontmatter)
        self.assertIn("为了醋包饺子", frontmatter)
        self.assertIn("weighted A-vs-B comparison", frontmatter)

    def test_repo_maintenance_scripts_exist(self) -> None:
        self.assertTrue(SYNC_SCRIPT.exists())
        self.assertTrue(VALIDATE_SCRIPT.exists())


if __name__ == "__main__":
    unittest.main()
