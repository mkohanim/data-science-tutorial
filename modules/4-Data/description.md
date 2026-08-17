# `devices_log.tsv`

A real INSTEON/ISY-style device event export. Tab-separated. 116,407 rows, 121 unique devices, spanning May 2024 – Aug 2026.

## Columns

- `INSTEON/A10/X10 Device` — device name (e.g. `Family Room / Bar`)
- `Control` — what kind of event (`Status`, `On Level`, `Ramp Rate`, `Cool Setpoint`, `Current Power Used`, `Error`, etc. — 35 distinct control types)
- `Value` — the reported value (varies by control type: `On`/`Off`, a percentage, a temperature, watts, etc.)
- `Time` — timestamp, e.g. `Fri 2025/11/07 12:38:56 PM`
- `User` — `System`, `Program`, or `Web`
- `Log Type` — always `Unknown` in this export; not a useful signal

