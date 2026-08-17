"""
Statistical anomaly detection skeleton — Z-score and IQR.

Fill in each function. Nothing here runs correctly yet on purpose.
These expect a pandas Series of values from a single Control type you've
picked (see detect.md) — not the whole log at once.
"""

import pandas as pd


def detect_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """
    Return a boolean Series: True where the value is more than
    `threshold` standard deviations from the mean.

    TODO: implement. (value - mean) / std, compare abs() to threshold.
    """
    raise NotImplementedError


def detect_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """
    Return a boolean Series: True where the value falls outside
    [Q1 - k*IQR, Q3 + k*IQR].

    TODO: implement using series.quantile().
    """
    raise NotImplementedError


def review_flags(df: pd.DataFrame, flagged_mask: pd.Series, n: int = 20) -> pd.DataFrame:
    """
    Since there's no ground truth, this is your evaluation step: pull out
    a readable sample of `n` flagged rows (device, control, value, time)
    for manual review. Look at each one and judge: does this actually
    look like an anomaly, or is the detector just flagging normal
    variation? Record your judgment calls in this module's answers.md.

    TODO: implement.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. Load + clean the data (modules/5-Load-Data/load_data.py) and
    #    filter to your chosen control type with filter_by_control().
    # 2. Run detect_zscore() and detect_iqr() on the 'value' column.
    # 3. Call review_flags() on each and print the sample for manual review.
    pass
