#!/usr/bin/env python3
"""Roast Your Own Agent — u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting the AI agent its own maker built to /output/entry.txt.
The line is a plain string constant; no network, no secrets, no input files.
"""
import os

# Critique-pick (7 candidates: 4 DeepSeek + 3 self-authored, judged on the kit's
# criteria): the winner names the agent's most specific real failing — it
# brags about a 99.6% transcript-reproduction score on an entry nobody paid
# for — while "iteration mode" and "$0.23 pennies" lines were close seconds.
# Third-person "Its" pins the roast to our own agent, not a generic robot.
ROAST = (
    "Its proudest stat is 99.6% thinking_reproduces on an entry nobody paid "
    "for \u2014 the most reliable way ever built to earn nothing."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
