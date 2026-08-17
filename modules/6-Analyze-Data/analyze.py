"""
Charting skeleton for exploring the real device event log with matplotlib.

Fill in each function. Nothing here plots correctly yet on purpose.

These functions expect a DataFrame that's already been loaded and cleaned
with the functions you wrote in modules/5-Load-Data/load_data.py (parsed
timestamps, noise rows dropped). See the note at the bottom of this file
for one way to reuse that code from here.
"""

import matplotlib.pyplot as plt
import pandas as pd


def plot_value_over_time(df: pd.DataFrame, device: str, control_type: str) -> None:
    """
    Line chart of `Value` over `Time` for a single device and Control type.

    Filter df down to rows matching `device` and `control_type`, sort by
    time, then plot value vs. time. This is the chart most likely to show
    spikes, gaps, or drift for one specific device.

    TODO: implement. Don't forget plt.xlabel/ylabel/title so the chart is
    readable without reading the code that made it. End with plt.show().
    """
    raise NotImplementedError


def plot_events_per_device(df: pd.DataFrame, top_n: int = 15) -> None:
    """
    Bar chart of event counts per device, for the `top_n` most active
    devices.

    TODO: implement. Hint: df['device'].value_counts() gets you most of
    the way there — the rest is turning that into a bar chart.
    """
    raise NotImplementedError


def plot_events_by_hour(df: pd.DataFrame) -> None:
    """
    Bar chart of event counts grouped by hour of day (0-23), across the
    whole log. Meant to answer: does this house have a daily rhythm?

    TODO: implement. Hint: your parsed Time column has a .dt.hour accessor.
    """
    raise NotImplementedError


def to_wide_format(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape the long-format log (one row per event) into wide format: one
    row per device+timestamp, one column per Control type.

    This is one of the "different shapes" from Module 4 — use it to see
    whether wide format makes any chart easier or harder to build.

    TODO: implement, e.g. with df.pivot_table(index=..., columns='control',
    values='value', aggfunc=...). Decide what to do with timestamps that
    don't line up exactly across control types.
    """
    raise NotImplementedError


def to_hourly_counts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape the log into a different granularity: one row per device per
    hour, with a count of events in that hour.

    This is another one of the "different shapes" from Module 4 — a
    resample/groupby aggregation instead of a pivot.

    TODO: implement, e.g. with df.set_index('time').groupby('device')
    .resample('1h').size().
    """
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. Load and clean the data using load_raw_log(), parse_timestamps(),
    #    and drop_noise_rows() from modules/5-Load-Data/load_data.py.
    #    (See the import note below for one way to reach that file from here.)
    # 2. Call a few of the functions above and look at what comes out.
    #
    # Simplest way to reuse Module 5's loader without copy-pasting it:
    #
    #   import sys
    #   from pathlib import Path
    #   sys.path.append(str(Path(__file__).resolve().parent.parent / "5-Load-Data"))
    #   from load_data import load_raw_log, parse_timestamps, drop_noise_rows
    #
    # Or just copy the three function calls in by hand — either is fine.
    pass
