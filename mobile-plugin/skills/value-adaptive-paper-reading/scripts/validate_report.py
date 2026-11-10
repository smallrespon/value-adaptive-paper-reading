#!/usr/bin/env python3
"""Check the structural completeness of a paper-reading report.

This script checks headings and common unresolved placeholders only.
It does NOT verify whether claims, citations, equations, or interpretations are true.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

GROUPS = {
    "阅读价值/决策卡": ["阅读决策卡", "阅读价值", "价值评估", "阅读建议"],
    "整体导读": ["一页读懂", "执行摘要", "论文概览", "核心结论"],
    "研究问题": ["研究问题", "核心问题", "研究目标", "问题定义"],
    "方法/论证/研究设计": [
        "核心方法", "方法与技术路线", "理论分析", "研究设计",
        "核心论证", "文献综合", "数据集与基准", "系统设计"
    ],
    "结果与证据": ["结果与证据", "实验与结果", "结果分析", "理论结果", "证据分析", "综合发现"],
    "局限/批判性分析": ["局限性", "批判性分析", "讨论与局限", "局限与展望"],
    "掌握目标/自测": ["掌握目标", "学习目标", "自测", "知识检查"],
    "证据索引/完整性审计": ["证据索引", "原文依据", "完整性审计", "来源与覆盖", "引用与覆盖"]
}

PLACEHOLDER_PATTERNS = [
    r"\bTODO\b", r"\bTBD\b", r"\[待补充\]", r"【待补充】",
    r"\[填写.*?\]", r"【填写.*?】", r"<待补充>"
]

def find_heading_text(text: str) -> list[str]:
    headings = []
    for line in text.splitlines():
        m = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if m:
            headings.append(m.group(1).strip())
    return headings

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path, help="Markdown report to validate")
    parser.add_argument("--strict", action="store_true",
                        help="Return non-zero if any required section is missing")
    args = parser.parse_args()

    if not args.report.is_file():
        print(f"ERROR: file not found: {args.report}", file=sys.stderr)
        return 2

    text = args.report.read_text(encoding="utf-8")
    headings = find_heading_text(text)
    normalized = "\n".join(headings)

    missing = []
    for label, aliases in GROUPS.items():
        if not any(alias.lower() in normalized.lower() for alias in aliases):
            missing.append(label)

    placeholders = []
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, text, flags=re.IGNORECASE):
            placeholders.append(pattern)

    print(f"Report: {args.report}")
    print(f"Headings found: {len(headings)}")

    if missing:
        print("\nMISSING SECTION GROUPS:")
        for item in missing:
            print(f"  - {item}")
    else:
        print("\nPASS: all baseline section groups are present.")

    if placeholders:
        print("\nPOSSIBLE UNRESOLVED PLACEHOLDERS:")
        for item in placeholders:
            print(f"  - pattern: {item}")
    else:
        print("PASS: no common unresolved placeholders found.")

    print("\nLIMITATION: this is a structural check only. It does not validate factual accuracy,")
    print("source locators, mathematical correctness, or whether the report truly covers the paper.")

    if args.strict and missing:
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
