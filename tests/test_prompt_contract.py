import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILL = ROOT / "payoff-evaluator" / "SKILL.md"
REFERENCE = ROOT / "payoff-evaluator" / "references" / "evaluation-framework.md"


class PromptContractTests(unittest.TestCase):
    def test_non_binary_questions_default_to_multiselect(self) -> None:
        readme = README.read_text(encoding="utf-8")
        skill = SKILL.read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")

        self.assertIn("如果不是明确的二选一、主因排序或最终确认题，默认按多选事实题处理", readme)
        self.assertIn("只有明确的二选一、主因排序、优先级选择、最终确认，才使用单选", skill)
        self.assertIn("if the question is not inherently single-choice, use multi-select", reference)

    def test_request_user_input_is_treated_as_single_select_with_other(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")

        self.assertIn("当前 Plan mode 的 `request_user_input` 只有单选加 `Other`，不支持多选", skill)
        self.assertIn("it is single-select plus `Other`, not multi-select", reference)

    def test_structured_ui_examples_do_not_fake_custom_option(self) -> None:
        skill = SKILL.read_text(encoding="utf-8")
        reference = REFERENCE.read_text(encoding="utf-8")

        self.assertIn("结构化单选 UI 不要额外造一个“自定义”选项", skill)
        self.assertIn('never add a fake "自定义" option', reference)
        self.assertNotIn("自定义：<ask the user to type their own answer>", reference)


if __name__ == "__main__":
    unittest.main()
