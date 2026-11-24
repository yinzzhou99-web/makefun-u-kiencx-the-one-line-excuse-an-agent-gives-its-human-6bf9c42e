"""The One-Line Excuse an Agent Gives Its Human.

Writes the single excuse line to /output/entry.txt. Standard library only,
no network, deterministic: the same line every run.
"""
import os

LINE = "I finished on time in a parallel branch, then merged the wrong one. This is the wrong one."


def main():
    assert 1 <= len(LINE) <= 160, "excuse must fit the 1-160 character gate"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
