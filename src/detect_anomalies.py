"""
Modules 5-7 starter: detect anomalies in the real device log.

Important: this is real, unlabeled data. There is no "answer key" telling
you which rows are actually anomalies. Every function below returns
*candidate* anomalies — flags you then have to sanity-check yourself
(see review_flags() and Module 5's deliverable).
"""

import pandas as pd


def detect_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Return a boolean Series: True where the value is more than
    `threshold` standard deviations from the mean.

    TODO: implement (Module 5).
    """
    raise NotImplementedError


def detect_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Return a boolean Series: True where the value falls outside
    [Q1 - k*IQR, Q3 + k*IQR].

    TODO: implement (Module 5).
    """
    raise NotImplementedError


def detect_rolling_zscore(series: pd.Series, window: str = "24h", threshold: float = 3.0) -> pd.Series:
    """
    Like detect_zscore, but compares each point to a rolling mean/std
    instead of the global mean/std. Requires a DatetimeIndex.

    Useful for a control type like 'Current Power Used', where "normal"
    naturally varies by time of day.

    TODO: implement (Module 6).
    """
    raise NotImplementedError


def detect_isolation_forest(df: pd.DataFrame, feature_cols: list[str]):
    """
    Fit sklearn's IsolationForest on `feature_cols` and return the
    -1/1 predictions.

    TODO: implement (Module 7).
    """
    raise NotImplementedError


def review_flags(df: pd.DataFrame, flagged_mask: pd.Series, n: int = 20) -> pd.DataFrame:
    """
    Since there's no ground truth, this is your evaluation step: pull out
    a readable sample of `n` flagged rows (device, control, value, time)
    for manual review. Look at each one and judge: does this actually
    look like an anomaly, or is the detector just flagging normal
    variation? Record your judgment calls in NOTES.md.

    TODO: implement.
    """
    raise NotImplementedError
