# Device Anomaly Detection — Starter Project

Starting point for the "Detecting Anomalies in Smart Home Device Logs" course, built around a **real** exported device event log.

## What's here

- `data/devices_log.tsv` — a real INSTEON/ISY-style device event export. Tab-separated. 116,407 rows, 121 unique devices, spanning May 2024 – Aug 2026. Columns:
  - `INSTEON/A10/X10 Device` — device name (e.g. `Family Room / Bar`)
  - `Control` — what kind of event (`Status`, `On Level`, `Ramp Rate`, `Cool Setpoint`, `Current Power Used`, `Error`, etc. — 35 distinct control types)
  - `Value` — the reported value (varies by control type: `On`/`Off`, a percentage, a temperature, watts, etc.)
  - `Time` — timestamp, e.g. `Fri 2025/11/07 12:38:56 PM`
  - `User` — `System`, `Program`, or `Web`
  - `Log Type` — always `Unknown` in this export; not a useful signal
- `src/load_data.py` — skeleton for loading and cleaning the real log. Stubbed with `TODO`s.
- `src/detect_anomalies.py` — skeleton for the detection modules. Also stubbed.
- `notebooks/` — put your exploration notebook(s) here.
- `NOTES.md` — your running answers to each module's deliverable.

## Important: there's no answer key

This is real data, not simulated — nobody has pre-labeled which rows are anomalies. That changes the project in a meaningful way (see the curriculum, Module 2 onward): instead of checking your detector against known planted anomalies, you'll be judging results by domain sense (does this flag make sense for a house?) and by manually reviewing a sample.

## Setup

1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate` (Mac/Linux) or `.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`

## How to use this repo

Nothing in `src/` works yet on purpose. Follow the course modules in order; each module tells you which stub to fill in.
