---
name: biotech-cv-tailor
description: Tailor a sleek, single-page, ATS-passing biotech/life-science CV to a specific job description. Use when the user pastes a job description (or names a role) and wants their CV adapted for it — reordering experience by relevance, mirroring the role title, matching ATS keywords truthfully, and rendering to a clean 1-page PDF. Works from the user's master profile.
---

# Biotech CV Tailor

Turn ONE master profile into a role-specific, one-page, ATS-friendly CV for a given job — the way strong biotech candidates tailor: **same truth, re-prioritized and re-framed for the target reader (both the ATS and the hiring scientist).**

## When to use
The user pastes/points to a **job description** (or names a target role) and wants a CV tailored to it. If no master profile exists yet, help them fill `references/master_profile.template.md` first.

## Inputs
1. **Master profile** — the user's full career truth (all roles, skills, education). Load `references/master_profile.template.md` if they don't have one filled in.
2. **Target job** — the JD text, or a role + company.

## The method (follow in order)

### 1. Read the JD like an ATS *and* a hiring manager
- Pull the **exact role title** and the **top ~10 keywords/requirements** (skills, tools, techniques, therapeutic area, seniority).
- Identify the **one real thing** they need this hire to do. Everything you emphasize should serve that.

### 2. Mirror the title
- The **headline under the name** should echo the JD's title (e.g., JD says "Translational Scientist" → headline leads with "Translational Scientist"). ATS and humans both scan for the title they posted.

### 3. Rewrite the Professional Summary (3–4 lines)
- Lead with the identity that matches the role, the single most relevant credential, and one proof point. Cut anything the role doesn't care about.

### 4. Re-order and re-weight Experience
- **Reverse-chronological by default**, BUT surface the *most relevant* experience: reorder bullets within each role so the top 1–2 bullets speak to *this* JD.
- Rewrite role sub-titles to bridge to the target (e.g., a research role framed toward BD, or toward bench science, depending on the JD).
- Keep bullets **achievement-first**: action verb → what → result/scale. Quantify where honest.

### 5. Core Skills = the ATS keyword layer
- Group skills into 4–6 **categories** (e.g., *Molecular & Cell Biology*, *Protein Engineering*, *Computation*, *Clinical & Regulatory*). Dense but truthful.
- Ensure the JD's top-10 terms appear **verbatim and truthfully** somewhere (skills or bullets). Never invent a skill to match.

### 6. Enforce the standing rules
- Apply every rule in `references/standing_rules.md` (consistent credential framing, no false language/skill claims, one page, no ATS-breaking elements). These are non-negotiable.

### 7. Keep it to ONE page, ATS-safe
- Single column. No tables, text boxes, columns, images, or headers/footers (they scramble ATS parsers).
- Standard section headers: *Professional Summary · Core Skills · Experience · Education*.
- Cut the least-relevant material until it fits one page. A tight, relevant 1-pager beats a complete 2-pager.

### 8. Render
- Output the tailored **Markdown** first (so the user can tweak wording), then render to PDF:
  ```bash
  python render/render_cv.py tailored_cv.md
  ```
- Confirm it's one page; if it overflows, trim the least-relevant bullets and re-render.

## Output format
1. A short note: the role title detected, the 5–8 keywords you matched, and what you reordered/cut and why.
2. The tailored CV as clean Markdown (ready to render).
3. The render command.

## References (bundled)
- `references/master_profile.template.md` — fill-in-the-blank master profile.
- `references/standing_rules.md` — the non-negotiable CV rules.
- `references/ats_methodology.md` — the deeper "why" behind ATS-passing 1-pagers.
- `examples/scientist_cv.example.md` + `examples/bd_cv.example.md` — the **same fictional candidate**, two role framings. Study how the headline, summary, skill emphasis, and experience order change while the underlying facts stay identical.
