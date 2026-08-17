# Module 4 — Data: Reading the Real Log

Open `devices_log.tsv` (in this same folder) and read [description.md](description.md) before writing any code. Look at the raw file directly — a spreadsheet app, or just scrolling it — not through a pandas function yet. You can't make good decisions about data you haven't actually looked at.

## The task

1. **Explain what the data means, in your own words.** What does one row represent? What is each column actually capturing? How do rows relate to each other — e.g. does the same device show up across many rows over time?

2. **Is this data in the right shape for data science analysis?** This is the core question of the module. Answer it seriously, both directions:
   - **Argue yes** — give real reasons the current shape could already work for analysis.
   - **Argue no** — give real reasons it might need to be reshaped, resorted, or restructured before analysis.
   - **If your answer is no:** propose the specific shape, sequence, or sorting you'd use instead, and explain *why* it would work better for detecting anomalies in this data.

There's no single correct answer here — the goal is that you can defend whichever position you land on with real reasons tied to this specific file.

## Guiding questions

Use these to think through "shape" from a few angles — you don't need to answer all of them in writing.

- **Long vs. wide:** right now, every row is one event: one device, one `Control` type, one `Value`, one `Time`. That's called *long* format. An alternative is *wide* format — one row per device per timestamp, with a separate column for each `Control` type (`Status`, `Current Power Used`, etc.). What would wide format make easier? What would it make harder or messier, given that not every device reports every control type at every timestamp?
- **Sorting:** is the file already sorted in an order that's useful for analysis (chronological? grouped by device?)? What sort order would you want before doing anything time-based, like a rolling average per device?
- **Granularity:** should each row stay as one individual event, or would grouping rows together early (e.g. one row per device per hour) help? What do you gain by aggregating early — and what do you lose?
- **Junk rows:** the file has some rows that look like system junk (e.g. device `0`, `Control` = `null`). Does the presence of rows like that change what "the right shape" even means, before any cleanup happens?

## Using Claude

- Use Claude Code to explore the ideas above, but **specifically ask it for the pros and cons of each shape/sequence/sorting option** — don't take its first suggestion as the answer. Good prompts to try:
  - "What are the pros and cons of long format vs. wide format for an event log like this, if the goal is anomaly detection?"
  - "What are the pros and cons of sorting this data by time only, vs. by device then time?"
  - "What are the pros and cons of aggregating events into hourly buckets before analysis, vs. keeping every row?"
- **Ground rule:** don't accept the first answer as final. Ask it to also argue the *other* side of whatever it recommended, then decide for yourself — based on this specific dataset and goal — which case is more convincing. You'll be quizzed on why you chose what you chose, not just what Claude said.

## Deliverable

Write up in this module's `answers.md`:

1. In your own words: what a row in `devices_log.tsv` represents, and what each column means.
2. Is this data in the right shape for data science analysis? Lay out the case for **yes** and the case for **no**.
3. If no: the specific shape/sequence/sorting you'd use instead and why — including the pros/cons you weighed (with Claude's help) for at least two options you seriously considered.
4. Thoughts, questions, and what you actually did — files opened, prompts you tried — per the format in the main [README](../../README.md#instructions).
