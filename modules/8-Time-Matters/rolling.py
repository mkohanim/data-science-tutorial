"""
Rolling-baseline anomaly detection skeleton.

Builds on Module 7's detect_zscore() — same idea, but compared against a
rolling window instead of the whole series' global mean/std.
"""

import pandas as pd


def detect_rolling_zscore(series: pd.Series, window: str = "24h", threshold: float = 3.0) -> pd.Series:
    """
    Like detect_zscore, but compares each point to a rolling mean/std
    instead of the global mean/std. Requires series to have a
    DatetimeIndex.

    Useful for a control type like 'Current Power Used', where "normal"
    naturally varies by time of day.

    TODO: implement with series.rolling(window). Decide how to handle
    the start of the series, where there isn't a full window yet.
    """
    raise NotImplementedError


def plot_global_vs_rolling(series: pd.Series, global_mask: pd.Series, rolling_mask: pd.Series) -> None:
    """
    Plot `series` over time, with points flagged by `global_mask` marked
    one way and points flagged by `rolling_mask` marked another way, so
    you can visually compare the two detectors.

    TODO: implement with matplotlib. Don't forget a legend distinguishing
    the two flag types.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. Reuse your Module 7 pipeline to get a cleaned, filtered Series
    #    for your chosen control type, indexed by time.
    # 2. Run detect_rolling_zscore() and compare against detect_zscore()
    #    from modules/7-Detect-Anomalies/detect.py.
    # 3. Call plot_global_vs_rolling() to see them side-by-side.
    pass
