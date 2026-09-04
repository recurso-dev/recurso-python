"""Pytest entry point for the no-network smoke test.

`tests/smoke_test.py` stays a standalone script (publish.yml runs it
directly); this wrapper makes the same checks part of `python -m pytest`.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import smoke_test  # noqa: E402


def test_smoke_script_passes(capsys):
    exit_code = smoke_test.main()
    out = capsys.readouterr().out
    assert exit_code == 0, f"smoke_test failures: {smoke_test.FAILURES}\n{out}"
    assert smoke_test.CHECKS_RUN > 0
