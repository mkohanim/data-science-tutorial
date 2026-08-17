"""
Isolation Forest skeleton — a first ML-based anomaly detector.

Unlike Modules 7-8, this can consider multiple features of a row at once
instead of just one value against a baseline.
"""

import pandas as pd
from sklearn.ensemble import IsolationForest


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Build a numeric feature DataFrame from your cleaned, filtered data:
    at minimum the value column, plus derived columns like hour-of-day
    and day-of-week from the parsed timestamp.

    TODO: implement.
    """
    raise NotImplementedError


def detect_isolation_forest(df: pd.DataFrame, feature_cols: list[str], contamination="auto") -> pd.Series:
    """
    Fit sklearn's IsolationForest on `feature_cols` and return the
    -1/1 predictions as a Series aligned to df's index.

    TODO: implement. Think about what `contamination` should be for your
    data before just leaving it on "auto".
    """
    raise NotImplementedError


if __name__ == "__main__":
    # TODO:
    # 1. Reuse your Module 7 pipeline to get cleaned, filtered data for
    #    your chosen control type.
    # 2. Call build_features(), then detect_isolation_forest().
    # 3. Reuse review_flags() from modules/7-Detect-Anomalies/detect.py
    #    to manually review a sample of the -1 (anomaly) rows.
    pass
