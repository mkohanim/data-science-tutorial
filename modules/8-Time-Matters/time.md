# Module 8 — Time Matters: Rolling Baselines

Your Module 7 detectors compare every value against one global mean/std for the whole time range. That's a problem if "normal" changes throughout the day — e.g. power draw is naturally higher in the evening. This module fixes that with a *rolling* baseline instead of a global one.

## The task

1. **Decide if this applies to your control type.** Does your Module 7 focus naturally vary through the day or week (e.g. power draw, activity-based `Status` changes)? If yes, continue below. If your control type is genuinely flat/constant regardless of time, say so and explain why a rolling baseline wouldn't help here — that's a valid answer too.

2. **Resample into fixed time buckets** (e.g. hourly) with `pandas.resample`, if useful for your analysis.

3. **Implement `detect_rolling_zscore()`** in `rolling.py` (this folder) — like `detect_zscore()` from Module 7, but compares each point to a *rolling* mean/std (a window of recent history) instead of the global mean/std. Requires a DatetimeIndex.

4. **Compare side-by-side**: plot your Module 7 global z-score flags against this module's rolling z-score flags, for the same device/control type. Where do they differ?

5. **Discuss**: why might a rolling baseline work better for data with daily/weekly patterns? When might it work *worse* (e.g. too short a window just chases noise)?

## Guiding questions

- What window size did you use (e.g. `"24h"`, `"7d"`), and why that one? What would happen with a much shorter or much longer window?
- Find one row flagged by the global method but *not* the rolling method (or vice versa). Why does the difference make sense given what a rolling window does?
- Is there a device/time where the rolling baseline itself looks wrong — e.g. it's still catching up right after a real shift in behavior?
- If your control type turned out to be flat/constant (step 1), what would you expect to see if you ran the rolling detector on it anyway?

## Using Claude

- Ask Claude for the pros and cons of different window sizes and resample frequencies for a dataset like this — but the choice of window size for *your specific device* has to be justified by you, not just copied from a suggestion.
- Same ground rule: be ready to explain your window-size choice and what you saw in the comparison plot, without notes.

## Deliverable

Write up in this module's `answers.md`:

1. Whether a rolling baseline applies to your control type, and why (or why not).
2. The window size you used and your reasoning for it.
3. A side-by-side plot comparing global z-score flags (Module 7) vs. rolling z-score flags (this module), and a note on which looks more sensible for this device.
4. Thoughts, questions, and what you actually did, per the format in the main [README](../../README.md#instructions).
