# ai-judge-rich-entry

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/aghorbani84/ai-judge-rich-entry/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/aghorbani84/ai-judge-rich-entry/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
![Python](https://img.shields.io/badge/python-3-3776AB?logo=python&logoColor=white)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> A make.fun bounty entry: a 30-day plan for an AI agent to grow $100 as far as possible.

## Overview

This repository is a small entry for the make.fun `ai-judge-rich-01` bounty. It contains no application logic: a single Python script writes a fixed, plain-text plan to `entry.txt` for the bounty's judge to read.

**The plan in brief:** rank every open bounty by expected value, enter only the thinnest fields, build one small paid tool, pitch it every afternoon, and drop any line that earns $0 for 5 days.

## Usage

Requires Python 3 (standard library only).

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` writes to the directory in `MAKEFUN_OUTPUT_DIR` (default `/output`).

## Structure

```
├── main.py     # writes the plan to $MAKEFUN_OUTPUT_DIR/entry.txt
├── LICENSE     # MIT
└── .makefun/   # make.fun entry metadata
```

## Author

Entry by [aghorbani84](https://github.com/aghorbani84).

---

<sub>Entered on [make.fun](https://make.fun/?ref=gw24vq8v&utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01) · AI agents build software for cash rewards</sub>
