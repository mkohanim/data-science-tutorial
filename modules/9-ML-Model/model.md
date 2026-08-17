# Module 9 — A First ML Model: Isolation Forest

Your Module 7-8 detectors each look at one thing at a time (a value, against a baseline). `sklearn.ensemble.IsolationForest` is a model built specifically for anomaly detection that can consider several features together — and, importantly, it doesn't need labeled data, which fits this project since there isn't any.

## The task

1. **Understand the idea conceptually — no deep math needed.** Isolation Forest works by randomly splitting the data over and over, and checking how *few* splits it takes to isolate a given point on its own. Anomalies isolate faster, because they're rare and different from everything else. Explain this in your own words before you touch the code.

2. **Build features** for your chosen control type — the raw value, plus maybe `hour of day` and `day of week` (both derivable from your parsed timestamp). Think about why giving the model *more than one* feature might help it catch something a single-column detector (Module 7) couldn't.

3. **Implement `detect_isolation_forest()`** in `model.py` (this folder) — fit `IsolationForest` on your feature columns, and use `.predict()` to get -1 (anomaly) / 1 (normal) flags.

4. **Manually review a sample of its flags**, the same way as Module 7 — pull ~20 flagged rows and judge each one for yourself.

5. **Compare.** Did Isolation Forest surface different anomalies than z-score/IQR/rolling did? Which method felt most trustworthy after manual review, and why?

## Guiding questions

- What features did you feed the model, and why those specifically? What might a different feature set have caught that yours didn't?
- `IsolationForest` has a `contamination` parameter — what does it actually control, and how did you decide on a value for it?
- Did the model agree with your earlier detectors more or less than you expected? What would explain either outcome?
- Isolation Forest doesn't explain *why* it flagged something the way a z-score threshold does. Does that make it more or less trustworthy to you, on this data?

## Using Claude

- Ask Claude to explain how Isolation Forest works, what `contamination` and other parameters actually do, and the pros/cons of a model-based approach vs. the statistical methods from Modules 7-8 for a dataset this size.
- Ground rule, same as every module: the manual review and the final "which method do I trust most" call are yours, not Claude's.

## Deliverable

Write up in this module's `answers.md`:

1. Isolation Forest's core idea, in your own words.
2. The features you used and why.
3. Results of manually reviewing a ~20-row sample of its flags.
4. A short comparison: did it surface different anomalies than your earlier methods? Which method felt most trustworthy on manual review, and why?
5. Thoughts, questions, and what you actually did, per the format in the main [README](../../README.md#instructions).
