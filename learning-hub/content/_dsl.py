"""Tiny DSL for writing course content as Python instead of hand-escaped JSON."""

def L(n, title, hook, sections, takeaways, terms, quiz, case, apply):
    q_out = []
    for i, q in enumerate(quiz):
        if q[0] == "tf":
            _, prompt, ans, why = q
            q_out.append({"id": f"l{n}q{i+1}", "kind": "tf", "q": prompt, "options": ["True", "False"],
                          "answer": 0 if ans else 1, "why": why})
        else:
            _, prompt, opts, ans, why = q
            q_out.append({"id": f"l{n}q{i+1}", "kind": "mc", "q": prompt, "options": opts, "answer": ans, "why": why})
    ctitle, scenario, cqs = case
    return {
        "n": n, "title": title, "hook": hook,
        "sections": [{"h": h, "html": html.strip()} for h, html in sections],
        "takeaways": takeaways,
        "terms": [{"term": t, "def": d, "type": k} for t, d, k in terms],
        "quiz": q_out,
        "case": {"title": ctitle, "scenario": scenario.strip(),
                 "questions": [{"q": q, "model": m.strip()} for q, m in cqs]},
        "apply": apply,
    }
