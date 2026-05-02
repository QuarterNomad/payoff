#!/usr/bin/env python3

from pathlib import Path
import os
import subprocess
import sys
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
QUICK_VALIDATE = Path("/Users/zhanzhifan/.codex/skills/.system/skill-creator/scripts/quick_validate.py")
PY_DEPS = Path("/tmp/skill_creator_validate_deps")


def run(cmd: List[str], env: Optional[Dict[str, str]] = None) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, env=env, check=True)


def ensure_quick_validate_deps() -> Dict[str, str]:
    env = os.environ.copy()
    extra_pythonpath = env.get("PYTHONPATH", "")
    env["PYTHONPATH"] = str(PY_DEPS) + (os.pathsep + extra_pythonpath if extra_pythonpath else "")

    yaml_init = PY_DEPS / "yaml" / "__init__.py"
    if not yaml_init.exists():
        PY_DEPS.mkdir(parents=True, exist_ok=True)
        run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--target",
                str(PY_DEPS),
                "pyyaml",
            ]
        )
    return env


def main() -> None:
    run([sys.executable, "scripts/sync_skill_copies.py"])
    run([sys.executable, "-m", "unittest", "-v"])

    env = ensure_quick_validate_deps()

    if QUICK_VALIDATE.exists():
        run([sys.executable, str(QUICK_VALIDATE), "payoff-evaluator"], env=env)
        run([sys.executable, str(QUICK_VALIDATE), ".cursor/skills/payoff-evaluator"], env=env)
    else:
        print("quick_validate.py not found; skipping skill-creator validation")


if __name__ == "__main__":
    main()
