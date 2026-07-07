# 🧬 biotech-cv-tailor

A **Claude skill** (+ a tiny render script) that turns one master profile into a **sleek, single-page, ATS-passing biotech/life-science CV**, tailored to a specific job description.

One truth, re-prioritized per role: the same PhD + industry experience can read as a *bench-scientist* CV or a *business-development* CV depending on how you order and frame it. This skill encodes that method — plus the ATS-safety rules that stop your experience from silently disappearing into a parser.

Distilled from a real biotech job hunt where **tailored 1-pagers meaningfully out-performed a generic CV**. No personal data inside — it ships a blank master-profile template and a fictional worked example.

---

## What's in here

```
biotech-cv-tailor/
├── skill/                     ← the Claude skill (drop into ~/.claude/skills/)
│   ├── SKILL.md               ← the tailoring method (the "brain")
│   ├── references/
│   │   ├── master_profile.template.md   fill this with YOUR career (once)
│   │   ├── standing_rules.md            non-negotiable ATS + credibility rules
│   │   └── ats_methodology.md           the "why" behind ATS-passing 1-pagers
│   └── examples/
│       ├── scientist_cv.example.md      same fictional person…
│       └── bd_cv.example.md             …two role framings
└── render/
    ├── render_cv.py           markdown → sleek 1-page PDF (single column, ATS-safe)
    └── requirements.txt
```

---

## Use it as a Claude skill (recommended)

1. **Install the skill:**
   ```bash
   cp -r skill ~/.claude/skills/biotech-cv-tailor
   ```
2. **Fill your master profile once:** copy `skill/references/master_profile.template.md`, add all your real experience, and keep it as your source of truth.
3. **Tailor to a job** — in Claude Code / Claude, invoke the skill and paste the job description:
   > `/biotech-cv-tailor` *(then paste the JD)*

   It will: detect the role title, match the JD's keywords truthfully, reorder your experience so the relevant bits are on top, enforce the standing rules, and output a tailored CV in Markdown.
4. **Render to PDF:**
   ```bash
   pip install -r render/requirements.txt
   python render/render_cv.py tailored_cv.md          # -> tailored_cv.pdf (A4)
   python render/render_cv.py tailored_cv.md --size letter
   ```

## Use it without the skill (any LLM + the render script)

The method is documented in `skill/SKILL.md` + `skill/references/`. Feed those + your master profile + a JD to any capable LLM with: *"tailor my CV to this JD following the method and standing rules; output markdown."* Then render with `render_cv.py`.

---

## The method in one screen

1. **Mirror the posted title** in your headline (ATS + humans scan for it).
2. **Rewrite the summary** (3–4 lines) to answer "do you fit *this* role?".
3. **Reorder experience** so the top third proves relevance; keep it reverse-chronological.
4. **Core Skills = the keyword layer** — 4–6 categories, JD's top-10 terms verbatim & truthful.
5. **Enforce the rules** — single column, standard headings, no tables/images, one page.
6. **Render & check it's one page.** Trim the least-relevant bullets if it overflows.

See `skill/references/ats_methodology.md` for the reasoning, and the two `examples/` for a before/after of framing.

## Notes
- **Honesty is load-bearing.** The skill never invents skills or numbers — a scientist-reviewer catches overclaims instantly, and that sinks the whole CV. Match keywords only where true.
- **Academic vs industry:** use the 1-pager for industry roles; keep a longer academic CV (full publications) for faculty/postdoc applications.
- ATS/formatting norms evolve — sanity-check current guidance before a big application.

## License
MIT.
