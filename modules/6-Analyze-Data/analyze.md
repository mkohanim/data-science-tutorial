# Module 6 — Analyze: What Does This Log Actually Mean?

You can load and clean the data (Module 5). Now actually look at it — not row by row, but as a whole — using `matplotlib`. Put your exploration in a notebook under `notebooks/` (in this same folder). `analyze.py` (also in this folder) is a charting skeleton with function stubs to fill in — use it as a starting point, or as functions you import into your notebook.

This module doesn't have one "correct" chart to produce. The goal is building a real mental model of what's normal for this house, using pictures instead of staring at raw rows.

## The task

1. **Load and clean the data** using what you built in `load_data.py`, then bring it into a notebook (`notebooks/`) so you can iterate quickly with `matplotlib`.

2. **Figure out what this whole log actually means, in your own words.** Not just "device events" — what does it actually tell you about a house full of INSTEON/ISY devices over roughly two years? How the house is used, which devices matter most, whether activity is steady or bursty, whatever you can genuinely learn from it.

3. **Look for interesting patterns using charts.** Some starting points — pick a few, don't feel obligated to do all of them:
   - Plot one or two specific devices' values over time. Anything jump out — spikes, gaps, drift, repeating cycles?
   - Count events per device. Is activity spread evenly, or do a handful of devices dominate the log?
   - Count events by hour of day or day of week. Does the house have a rhythm?
   - Compare two `Control` types against each other.
   - Anything else you're genuinely curious about — this part is open-ended on purpose.

4. **Try more than one shape of the log — reuse the reshaping you thought about back in Module 4.** Don't just chart the raw long-format log once and stop. Reshape it at least one more way (e.g. pivot to wide format, aggregate into hourly/daily buckets, sort/group by device vs. by time) and chart that version too. `analyze.py` has stubs for two of these (`to_wide_format`, `to_hourly_counts`) to get you started — feel free to write your own instead. Does a different shape make a pattern easier to see, or harder? Does it surface anything the first shape hid?

5. **Answer honestly: is this analysis actually giving you something loading and eyeballing the data didn't?** Or would loading the file and skimming `.head()` / `.describe()` have told you just as much, and the charts were mostly just nice to look at? Argue for your *actual* position, not whichever answer sounds more like what a course "should" want.

## Guiding questions

- What do `.describe()` and `.info()` on your cleaned data tell you — if anything — before you've plotted a single chart?
- What's the smallest set of charts that would let a stranger understand "what this house's data looks like" in under a minute?
- For a specific question you had, would a line chart, bar chart, or histogram have told you more? Why that one and not the others?
- Pick one pattern you found. Could you have found it just from summary statistics, without a chart? Why or why not?
- Was there a chart you made that told you nothing useful? Why do you think it didn't work for that question?
- Between the shapes you tried, did any single one feel like "the" right shape for exploration, or did different questions genuinely need different shapes?

## Using Claude

- Ask Claude to help debug matplotlib code or explain what a *type* of pattern usually indicates in time-series data — but the read of what *your specific chart* means has to be yours. Claude isn't looking at your plot.
- Good prompts: "why is this matplotlib code throwing X error," "what does a repeating spike pattern like this usually indicate in sensor data," "what's a good chart type for showing counts by hour of day?"
- You'll be quizzed on your own read of your own charts, not on what Claude said a chart like that "usually" shows.

## Deliverable

Write up in this module's `answers.md`:

1. In your own words: what this whole log actually means — what you can genuinely learn about this house and its devices from it.
2. At least two interesting patterns you found via charts — for each: what chart you made, what you saw, and why you think it's a real pattern and not noise.
3. The different shapes of the log you tried (at least two) and what changed between them — did reshaping make any pattern easier to spot, harder, or surface something new entirely?
4. Your honest answer to: is analysis of this data actually important here, or would loading and looking have been sufficient? Argue it with real reasoning, not just the expected answer.
5. Thoughts, questions, and what you actually did — the notebook you built, charts you tried, prompts you used — per the format in the main [README](../../README.md#instructions).
