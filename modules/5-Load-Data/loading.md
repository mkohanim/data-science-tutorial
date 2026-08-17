# Module 5 — Loading Data with pandas

You've read the raw file by eye and thought about its shape. Now load it into Python for real, using `pandas`.

## The task

1. **Research what pandas is and why it's important, in your own words.** What problem does it solve that plain Python (lists, dicts, loops) doesn't handle well? Why is it the standard tool for this kind of work instead of, say, reading the file line-by-line yourself?

2. **Implement `load_raw_log()`** in `load_data.py` (in this same folder) so it actually reads `modules/4-Data/devices_log.tsv` into a DataFrame. Confirm it works by printing `.info()` and `.head()` and checking the result looks like the real data. See [coding.md](coding.md) for what the skeleton looks like and how to run it from VS Code.

3. **Think about load-time strategy.** This file is ~116,000 rows — small enough that brute force works fine. But get in the habit of asking these questions anyway, because they stop being optional once a file is gigabytes instead of megabytes:
   - **How would you optimize load times** for this file — or one 100x bigger?
   - **Do you load everything into memory**, or only the columns/rows you actually need?
   - **Do you filter before loading** (e.g. skipping rows pandas never has to parse) **or after loading** (read everything into a DataFrame, then filter with pandas)? What's the tradeoff between the two?

## More questions to think through

These follow from the ones above — you don't need to answer every single one in writing, but think about which apply to this file.

- **dtypes:** should you tell pandas the column types up front (`dtype=`), or let it infer them? What does inference cost you — in time, memory, or correctness surprises (e.g. a numeric-looking column that's secretly got a stray text value in it)?
- **Column selection:** do you need every column right away, or can you skip ones you know you won't use yet (e.g. `Log Type`, which the description notes is always `Unknown`)? What pandas option controls that?
- **Parsing dates:** should `Time` be parsed into a real datetime *during* the load, or as a separate step afterward? Does it matter for speed, correctness, or just convenience?
- **Chunking:** pandas can read a file in pieces instead of all at once. When would that matter for a file this size — and what do you lose by not having the whole thing in memory together (e.g. computing a global mean)?
- **File format:** this file is a `.tsv`. If you were going to load it over and over while developing, would converting it to a different format first (e.g. Parquet) save you anything? Why would a different format load faster than plain text in the first place?
- **Caching:** while you're iterating on `load_raw_log()`, you'll probably run your script dozens of times. Is there a way to avoid re-parsing the raw file from scratch on every single run?
- **Sampling while developing:** would you want to load all 116,407 rows every time you test a change, or a smaller slice first? What pandas option would let you do that?

## Using Claude

- Use Claude Code to research what pandas is and how these loading options actually work — but for the strategy questions, **specifically ask for the pros and cons of each approach for this dataset** (116K rows, one `.tsv`, loaded repeatedly during development) vs. a hypothetical much larger one. The right answer at this file's size is often different from the right answer at real scale — make sure you understand why, not just which option to pick.
- **Ground rule:** don't accept the first answer as final — same as previous modules, you'll be quizzed on *why*, not just *what*.

## Deliverable

Write up in this module's `answers.md`:

1. In your own words: what pandas is, and why it's a better fit for this kind of work than plain Python.
2. Your working `load_raw_log()` (or a link/reference to it in `load_data.py`), plus the `.info()` output showing it actually loads the real file.
3. Your answers to the three core strategy questions (optimize load time / load everything vs. selectively / filter before vs. after loading), plus at least three of the "more questions" that felt most relevant to this file — including the pros/cons Claude helped you weigh for each.
4. Thoughts, questions, and what you actually did, per the format in the main [README](../../README.md#instructions).
