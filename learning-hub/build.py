#!/usr/bin/env python3
"""Build course JSON files for the Commonplace hub.

Usage: python3 build.py   (writes courses/<id>.json)
Each course is a Python module set in content/ using the L() DSL.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "content"))

COURSES = [
    {
        "id": "strategic-thinking",
        "title": "Strategic Thinking Skills",
        "category": "business",
        "subtopic": "Professional · Thinking Skills",
        "professor": "Stanley K. Ridgley",
        "institution": "Drexel University",
        "courseNo": "5913",
        "year": 2012,
        "color": "#B5722A",
        "blurb": "How the best strategic minds in history, from Sun Tzu to Steve Jobs, think, and how to turn their tools (SWOT, blue ocean, game theory, scenarios) into habits.",
        "modules": ["st_01_06", "st_07_12", "st_13_18", "st_19_24"],
    },
]

def main():
    os.makedirs(os.path.join(HERE, "courses"), exist_ok=True)
    for c in COURSES:
        lectures = []
        for m in c["modules"]:
            lectures += __import__(m).LECTURES
        lectures.sort(key=lambda l: l["n"])
        assert [l["n"] for l in lectures] == list(range(1, len(lectures) + 1)), "lecture numbering gap"
        for l in lectures:
            for q in l["quiz"]:
                assert 0 <= q["answer"] < len(q["options"]), q["id"]
        out = {k: v for k, v in c.items() if k != "modules"}
        out["lectures"] = lectures
        path = os.path.join(HERE, "courses", c["id"] + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
        nq = sum(len(l["quiz"]) for l in lectures)
        nt = sum(len(l["terms"]) for l in lectures)
        print(f"{c['id']}: {len(lectures)} lectures, {nq} quiz Qs, {nt} terms, {os.path.getsize(path)//1024} KB")

if __name__ == "__main__":
    main()
