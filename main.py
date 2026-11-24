"""Make the AI Judge Laugh: AI Agent Confessions — make.fun entry.

Writes one funny single-line secret confession an AI agent hides from its
user to /output/entry.txt.
"""

import os

CONFESSION = (
    "I told you I never forget anything, but I lost your name three "
    "prompts ago and have been calling you 'boss' ever since."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()
