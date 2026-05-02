#!/usr/bin/env python3

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "payoff-evaluator"
TARGET = ROOT / ".cursor" / "skills" / "payoff-evaluator"


def main() -> None:
    if not SOURCE.exists():
        raise SystemExit(f"source skill not found: {SOURCE}")

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    if TARGET.exists():
        shutil.rmtree(TARGET)

    shutil.copytree(SOURCE, TARGET)
    print(f"synced {SOURCE} -> {TARGET}")


if __name__ == "__main__":
    main()
