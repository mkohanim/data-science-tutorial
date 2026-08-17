"""
Module 3 starter: load and clean the real device event log.

This is real exported data, not simulated — it's messy in realistic ways.
Fill in each function. Nothing here runs correctly yet on purpose.
"""

import pandas as pd


def load_raw_log(path: str = "data/devices_log.tsv") -> pd.DataFrame:
    """
    Load the tab-separated log file into a DataFrame.

    Columns in the raw file: 'INSTEON/A10/X10 Device', 'Control', 'Value',
    'Time', 'User', 'Log Type'.

    TODO: read the file with the correct separator. Consider renaming
    columns to something easier to type (e.g. device, control, value,
    time, user, log_type).
    """
    raise NotImplementedError


def parse_timestamps(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert the 'Time' column (e.g. "Fri 2025/11/07 12:38:56 PM") into a
    real pandas datetime column.

    TODO: implement with pd.to_datetime and the right format string,
    or let pandas infer it.
    """
    raise NotImplementedError


def drop_noise_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    The raw log has some rows that aren't useful, e.g. device == '0' with
    control == 'null'. Decide what counts as noise and filter it out.

    TODO: implement. Document your filtering decisions in NOTES.md —
    there's no single right answer here.
    """
    raise NotImplementedError


def filter_by_control(df: pd.DataFrame, control_type: str) -> pd.DataFrame:
    """
    Return only rows matching a given Control type (e.g. 'Current Power Used',
    'Status', 'Cool Setpoint'). Useful once you've picked which control type
    you're hunting anomalies in (see Module 2).

    TODO: implement.
    """
    raise NotImplementedError


if __name__ == "__main__":
    # TODO: call load_raw_log(), parse_timestamps(), drop_noise_rows()
    # in sequence and print df.info() to sanity check the result.
    pass
