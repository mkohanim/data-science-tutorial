# Detecting Anomalies in Smart Home Device Logs
### A hands-on data science course (Python)

**Who this is for:** a teenager who can already write basic Python (variables, loops, functions) and wants a real project, not just tutorials.

**How it works:** each module ends with questions the student answers *in their own words* and code they write *themselves*. Nothing is pre-decided for them — they explore the real log, pick which anomalies matter, and build the pipeline. Answers should live in a running notebook or `NOTES.md` they keep for the whole course.

**The data:** a real exported device event log from an INSTEON/ISY-style home automation system — 116,407 rows, 121 devices, spanning May 2024 to Aug 2026. Not simulated. This means there's no pre-made answer key telling you which rows are anomalies — you have to build judgment for that yourself, which is closer to what real data science work is actually like.

**Tools:** Python 3, `pandas`, `numpy`, `matplotlib`. Later: `scikit-learn`. All free, all local.

---

## Module 0 — Tools setup (60–90 min)

Get the environment working before touching data science. Short, guided steps, done in this order:

1. **Create a GitHub account** (github.com/join). Explain in plain terms: GitHub hosts code online and tracks its history ("version control") so you can save progress and never lose work.
2. **Install VS Code** (code.visualstudio.com) — the editor they'll write Python in.
3. **Open VS Code, then open its integrated terminal** (`` Ctrl+` `` on Windows/Linux, `` Cmd+` `` on Mac, or Terminal → New Terminal).
4. **Install Git from that terminal** (Windows, via winget):
   ```
   winget install --id Git.Git -e --source winget
   ```
5. **Close VS Code completely and reopen it** — this is required so VS Code picks up the newly installed `git` command.
6. **Install VS Code extensions** (Extensions panel — the squares icon in the left sidebar, or `Ctrl+Shift+X`). Search for and install each of these:
   - **Python** (Microsoft) — Python language support
   - **Python Debugger** (Microsoft) — step-through debugging for Python
   - **Vim** — modal editing keybindings
   - **Claude Code** — AI pair-programmer inside VS Code

**Short concept tutorials (10–15 min each, plain language, no jargon dump):**
- *VS Code basics:* opening a folder, the integrated terminal, running a `.py` file, the Explorer panel.
- *GitHub concepts:* repository, commit, push/pull, clone — explained as "a repo is a project folder that lives online and remembers every version of itself."
- *Git basics:* `git clone <url>`, `git status`, `git add`, `git commit -m "message"`, `git push` — the core loop they'll use from Module 0.5 onward.
- *Vim basics (optional, only if the student is curious):* normal vs. insert mode, `i` to insert, `Esc` to go back, `:wq` to save and quit. Totally fine to skip using Vim keybindings day-to-day and just note it's there.
- *Claude Code:* what it's for (asking questions about code, getting suggestions, not doing the thinking *for* them), and the ground rule for this course — it's a helper for understanding stuck points, not for skipping the exercises.

**Deliverable:** GitHub account created, VS Code installed, Git installed (`git --version` works in the terminal after restarting VS Code), all four extensions installed, one test file run successfully (e.g. `print("hello")`).

---

## Module 0.5 — Get the starter repo

Clone the starter repo for this project from the VS Code integrated terminal, using the `git` installed in Module 0:

```
git clone <your-repo-url>
cd <repo-folder>
pip install -r requirements.txt
```

Walk through what's inside together:
- `data/devices_log.tsv` — the real log. Tab-separated, columns: device, control, value, time, user, log type.
- `src/load_data.py` — stubbed functions for loading and cleaning the log.
- `src/detect_anomalies.py` — stubbed detection functions.
- `notebooks/` — where exploration work goes.
- `NOTES.md` — filled in module by module.

**Deliverable:** repo cloned locally, `pip install -r requirements.txt` runs with no errors, they can explain in one sentence what each file/folder is for.

---

## Module 1 — Why this project (30–45 min)

Read about a couple of real anomaly-detection use cases (e.g. a smart thermostat that starts cycling every 2 minutes because a sensor is failing, or a smart plug reporting power draw that never happened). Discuss with the student:

- What does "anomaly" mean vs. just "different"?
- Why would a homeowner *want* to know about this automatically instead of noticing it themselves?

**Deliverable:** 3–5 sentences, in their own words, on what an anomaly is and one made-up example of a device anomaly.

---

## Module 2 — Understand the real log & pick a focus

Open `data/devices_log.tsv` and look at it directly (a spreadsheet app or `head` in the terminal) before writing any pandas code. Then answer, in writing, before touching code:

1. **What's actually in each column?**
   `Control` has ~35 distinct values in this file — things like `Status`, `On Level`, `Ramp Rate`, `Cool Setpoint`, `Heat Setpoint`, `Current Power Used`, `Current Voltage`, `Error`. Have the student list a handful they recognize and guess what each represents.

2. **What kind of anomaly matters most, and in which control type?**
   Have them pick ONE control type to start (not "everything" — that's a trap for a first project). Good beginner choices given this data:
   - **Value anomalies:** `Current Power Used` or `Current Voltage` — a device drawing way more or less power than normal
   - **Timing anomalies:** `Status` (on/off) — a device turning on at an unusual hour
   - **Failure signals:** `Error` — literal error events already logged by the system

3. **What would a real anomaly look like here?**
   Have them describe, in a sentence, what a suspicious row would actually look like for their chosen control type — device name, rough value, time of day.

**Deliverable:** which control type they're focusing on and why, plus a one-sentence description of what a real anomaly would look like in that data.

---

## Module 3 — Load & clean the real log

Real exported data is messier than anything simulated. Guide the student to write `src/load_data.py`:
- Load the tab-separated file with `pandas`
- Parse the `Time` column into real datetimes
- Look for junk rows (e.g. this file has some rows where the device is `0` and control is `null` — junk from the system, not real events) and decide what to filter out
- Filter down to just their chosen control type from Module 2

There's no "right" cleaning decision here — the point is the student has to make and justify choices, and write those choices down.

**Deliverable:** a cleaned DataFrame containing only their chosen control type, plus notes on what rows they excluded and why.

---

## Module 4 — Exploratory Data Analysis (EDA)

Before detecting anomalies, understand normal. Have them:
- `.describe()` and `.info()` on their filtered data
- Plot the value over time with `matplotlib` for one or two specific devices
- Compute mean/std/median by device
- Try to *visually* spot anything that looks off, just by eyeballing the plot

**Deliverable:** an annotated plot with anything that looks suspicious circled by hand, and a note on what drew their eye to it.

---

## Module 5 — Simple statistical detection

Two classic, explainable methods — no ML yet:
- **Z-score:** flag points more than N standard deviations from the mean
- **IQR method:** flag points outside 1.5× the interquartile range

Have the student implement both in `src/detect_anomalies.py` as functions that take a pandas Series and return a boolean mask.

**Since there's no answer key**, evaluation works differently than with simulated data: pull out the flagged rows (`review_flags()` in the stub) and manually look at each one. Does it actually look anomalous given what the device is and when it happened, or is the detector just reacting to normal variation? This manual-judgment step *is* the deliverable — it's a real and important part of doing anomaly detection on unlabeled data.

**Deliverable:** how many rows each method flagged, and — after manually reviewing a sample of ~20 — how many of those flags they'd actually call real anomalies vs. false alarms, with reasoning.

---

## Module 6 — Time matters

If their anomaly type involves timing or naturally varies through the day (e.g. power draw is higher in the evening):
- Resample into fixed time buckets (e.g. per-hour) with `pandas.resample`
- Compute a **rolling mean and rolling standard deviation** and flag points that deviate from the *rolling* baseline rather than the global one
- Discuss: why is a rolling baseline better for data with daily/weekly patterns?

**Deliverable:** side-by-side plot comparing global z-score flags vs. rolling z-score flags, and a note on which looks more sensible for this device.

---

## Module 7 — A first ML model

Introduce `sklearn.ensemble.IsolationForest` — a model built specifically for anomaly detection that doesn't need labeled data (which fits this project well, since there isn't any).
- Fit it on numeric features (value, maybe hour-of-day, day-of-week)
- Use `.predict()` to get -1/1 anomaly flags
- Manually review a sample of its flags the same way as Module 5

Discuss conceptually (no deep math needed): Isolation Forest works by randomly splitting data and checking how *few* splits it takes to isolate a point — anomalies isolate faster because they're rare and different.

**Deliverable:** a short comparison — did IsolationForest surface different anomalies than z-score/IQR did? Which method felt most trustworthy on manual review?

---

## Module 8 — Capstone

The student picks (or you assign) one of:
- Extend the analysis to a second control type (e.g. if they started with power, add error events)
- Build a script that scans the whole log and prints a ranked "top suspicious events" report
- Pick one specific device with a lot of history and write a mini profile of its normal behavior plus any anomalies found

**Deliverable:** a short written report (1 page): what anomaly they detected, which method worked best, what didn't work, and why — grounded in the real data, not a hypothetical.

---

## Notes for whoever is teaching

- Resist pre-answering Module 2 — letting the student pick a control type and discover it was a bad choice (too sparse, too noisy) is one of the best learning moments, and Module 3 is exactly where that surfaces.
- Because this is real unlabeled data, expect Module 5 onward to feel less clean than a textbook exercise — flags will include false positives, and that ambiguity is the point, not a bug in the course.
- Keep everything in Python per your existing workflow; no need for extra frameworks.
- Total time: roughly 8–12 sessions of 45–90 minutes depending on the student's pace.
