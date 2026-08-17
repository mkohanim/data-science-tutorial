# Detecting Anomalies in Smart Home Device Logs
## A hands-on data science course (Python)

**Who this is for:** a teenager who can already write basic Python (variables, loops, functions) and wants a real project, not just tutorials.

**How it works:** each module ends with questions the student answers *in their own words* and code they write *themselves*. Nothing is pre-decided for them — they explore the real log, pick which anomalies matter, and build the pipeline. Answers live in each module's own `answers.md` (see Instructions below).

**The data:** a real exported device event log from an INSTEON/ISY-style home automation system — 116,407 rows, 121 devices, spanning May 2024 to Aug 2026. Not simulated. This means there's no pre-made answer key telling you which rows are anomalies — you have to build judgment for that yourself, which is closer to what real data science work is actually like.

**Tools:** Python 3, `pandas`, `numpy`, `matplotlib`. Later: `scikit-learn`. All free, all local.

---

## What's here

- `modules/` — the course itself, one folder per module (`1-Setup/` through `10-Capstone/`). Each folder holds that module's doc, any artifacts it needs (data files, skeleton `.py` code — e.g. `modules/4-Data/devices_log.tsv`, the real device event log, see [modules/4-Data/description.md](modules/4-Data/description.md) for column details), and your `answers.md`.
- `notebooks/` — put your exploration notebook(s) here.

## Instructions

Work through `modules/` in order — don't skip ahead. For each module:

1. **Finish the module.** Read its doc (e.g. `modules/1-Setup/setup.md`), do the exercises, and follow along in your own code (a notebook, or the module's own skeleton `.py` file, as the module says).
2. **Write it up in that module's `answers.md`.** E.g. after `modules/1-Setup/setup.md`, fill in `modules/1-Setup/answers.md`, and record:
   - **Answers** — your response to every question the module asks, in your own words.
   - **Thoughts** — anything you noticed, found surprising, or want to remember.
   - **Questions** — anything that's still unclear or you'd want to ask about.
   - **Completions** — what you actually did/ran/built (files touched, commands run, what worked or didn't).
3. **Commit it.** `git add modules/<N-Name>/answers.md` and commit before moving to the next module — that write-up is what makes your progress checkable later.

A blank or missing `answers.md` for a module means that module isn't done yet, regardless of what code exists elsewhere.

