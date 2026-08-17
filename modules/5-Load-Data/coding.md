# Coding: the `load_data.py` skeleton

This is a companion to [loading.md](loading.md) — it walks through the actual file you'll be editing, `load_data.py` (in this same folder), and how to run it.

## What's in the skeleton

The file defines four functions and a `main` block. Every function currently just `raise NotImplementedError` — that's on purpose, so the file runs without silently doing the wrong thing before you've written anything.

- **`load_raw_log(path)`** — should read `devices_log.tsv` into a DataFrame. This is what Module 5 asks you to implement first.
- **`parse_timestamps(df)`** — should convert the `Time` column (currently just text, e.g. `"Fri 2025/11/07 12:38:56 PM"`) into a real pandas datetime column, so you can later sort, filter, or plot by time.
- **`drop_noise_rows(df)`** — should filter out junk rows the export left behind (e.g. rows where the device is `0` and the control is `null`). You decide what counts as noise and document why.
- **`filter_by_control(df, control_type)`** — should narrow the data down to a single `Control` type (e.g. just `"Current Power Used"`) once you've decided which one you're focusing on.
- **`if __name__ == "__main__":`** — the block that runs when you execute this file directly (as opposed to importing it from somewhere else). Right now it's a `TODO` and a `pass`; once you've implemented the functions above, this is where you call them in sequence and print `df.info()` to sanity-check the result.

Each function has a docstring describing exactly what it should do — read those before you start writing code, they're the spec.

## Running it from VS Code (Run and Debug)

1. Open `load_data.py` in the editor.
2. Open the **Run and Debug** panel — the ▷ icon with a bug on it in the left sidebar (or `Ctrl+Shift+D`).
3. Click **Run and Debug**. The first time, VS Code will ask you to pick a debug configuration — choose **Python File**. This runs the file exactly as `python load_data.py`, but through the debugger, so you can pause and inspect things.
4. Output appears in the **Debug Console** / integrated terminal at the bottom.

A faster shortcut once you're not debugging anything specific: the ▶️ **Run Python File** button in the top-right corner of the editor (a triangle "play" icon) runs the file the same way, without the debugger attached.

**Why this matters for `load_raw_log`'s default path:** the function's default argument is `path="modules/4-Data/devices_log.tsv"` — a path *relative to the folder VS Code runs the command from*, not relative to `load_data.py` itself. By default, VS Code runs both "Run Python File" and "Run and Debug" from your **workspace root** (the folder you opened in VS Code — `data-science-tutorial/`), so that relative path resolves correctly even though `load_data.py` lives one level down in `modules/5-Load-Data/`. If you ever open just the `modules/5-Load-Data/` folder on its own instead of the whole repo, that path will break — that's expected, not a bug in your code.

## Using the debugger

Since every function currently raises `NotImplementedError`, running the file as-is will just crash with that error the moment `main` calls the first unimplemented function — that's expected until you fill something in.

Once you've implemented `load_raw_log()`:

1. Click in the left margin next to a line inside `load_raw_log()` to set a **breakpoint** (a red dot appears).
2. Run with **Run and Debug** (not the plain ▶️ button — breakpoints only pause execution in debug mode).
3. Execution stops at your breakpoint. Use the debug toolbar to **Step Over** (run one line) or **Continue** (run to the next breakpoint), and hover over any variable to see its current value — this is the fastest way to see exactly what pandas is doing to your DataFrame at each step.
