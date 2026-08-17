# Module 10 — Capstone

Everything up to this point has been guided. This module isn't — you pick the shape of the final project yourself.

## The task

Pick **one** of the following (or, if you have your own idea grounded in this data, propose it instead):

1. **Extend to a second control type.** If you started with power (Module 7), add error events — or vice versa. Run the same process (pick a focus, describe what an anomaly looks like, detect, review) on something new.
2. **Build a "top suspicious events" report.** A script that scans the whole log, runs your best detector(s) across multiple control types or devices, and prints a ranked report of the most suspicious events it found.
3. **Profile one device in depth.** Pick a specific device with a lot of history and write a mini profile: what's normal for it, and what anomalies (if any) you found, using whichever method(s) from Modules 7-9 fit best.

There's no starter skeleton for this module — deliberately. Which functions you need depends entirely on which path you pick; reuse what you've already built in Modules 7-9 rather than starting from scratch.

## Guiding questions

- Why did you pick this path over the other two? What did it let you do that the others wouldn't have?
- Which detection method (z-score, IQR, rolling, Isolation Forest) ended up doing the most work for you here, and why that one?
- If you had another week on this, what's the next thing you'd try?

## Deliverable

Write up in this module's `answers.md`, as a short written report (about 1 page):

1. Which path you picked, and why.
2. What anomaly (or anomalies) you found, grounded in the real data — not a hypothetical.
3. Which method worked best for this, what didn't work, and why.
4. Thoughts, questions, and what you actually built, per the format in the main [README](../../README.md#instructions).
