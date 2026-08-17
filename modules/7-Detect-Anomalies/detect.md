# Module 7 — Detect Anomalies: Z-Score & IQR

You've explored the log broadly (Module 6). Time to narrow down and build your first real detectors — two classic, explainable statistical methods, no ML yet.

## The task

1. **Pick ONE control type to focus on.** Not "everything" — trying to detect anomalies across all 35 control types at once is a trap for a first project; you'll end up detecting nothing well. Good starter picks, based on what you've already seen in the data:
   - **Value anomalies:** `Current Power Used` or `Current Voltage` — a device drawing way more or less power than normal.
   - **Timing anomalies:** `Status` (on/off) — a device turning on at an unusual hour.
   - **Failure signals:** `Error` — literal error events already logged by the system.

   Pick one and write down why.

2. **Describe, in one sentence, what a real anomaly would actually look like** for your chosen control type — device name (or type of device), rough value, and time of day. Write this down *before* you build the detector — it's your target, and it stops you from just accepting whatever the math spits out.

3. **Implement `detect_zscore()` and `detect_iqr()`** in `detect.py` (this folder) — each takes a pandas Series and returns a boolean mask (True = flagged).
   - Z-score: flag points more than N standard deviations from the mean.
   - IQR: flag points outside `[Q1 − k×IQR, Q3 + k×IQR]`.

4. **Run both on your chosen control type's values.** How many rows does each flag? Do they agree on which rows, or flag different things?

5. **Manually review the flags — this is the actual deliverable.** There's no answer key for this data, so evaluation works differently than a textbook exercise: use `review_flags()` to pull out a readable sample of ~20 flagged rows (device, control, value, time) and look at each one yourself. Does it actually look anomalous given what the device is and when it happened — or is the detector just reacting to normal variation? Record your judgment call and *why* for each.

## Guiding questions

- Why does picking one control type matter here, instead of running a detector over the whole log at once?
- What threshold did you use for z-score (or `k` for IQR), and why that value specifically — not just whatever a default happened to be?
- Where do z-score and IQR disagree? What does that disagreement tell you about the shape of your data (e.g. is it skewed, does it have outliers that distort the mean)?
- What's the cost of a detector that flags too much (lots of false alarms) vs. one that flags too little (misses real problems) — for a smart home, specifically?
- After reviewing ~20 flags by hand, what pattern did you notice among the ones you decided *weren't* real anomalies? Is there a way to encode that back into the detector?

## Using Claude

- Ask Claude to explain the math, help debug your implementation, and give you the pros and cons of z-score vs. IQR for a dataset like this (e.g. how each handles skewed distributions or heavy outliers).
- **What Claude can't do for you:** the manual review in step 5. It hasn't seen this specific device's history — whether a flagged row is a real anomaly or normal variation is a judgment call you have to make and defend.
- Same ground rule as always: you'll be quizzed on why you made the calls you made.

## Deliverable

Write up in this module's `answers.md`:

1. Which control type you're focusing on, and why.
2. A one-sentence description of what a real anomaly would look like for that control type.
3. How many rows each method (z-score, IQR) flagged, and where they agreed/disagreed.
4. Results of your manual review of a ~20-row sample: how many you'd actually call real anomalies vs. false alarms, with reasoning for at least a few individual rows.
5. Thoughts, questions, and what you actually did, per the format in the main [README](../../README.md#instructions).
