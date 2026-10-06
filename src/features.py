import pandas as pd


def v2_features(df: pd.DataFrame) -> None:
    # Categorical features
    df["ADEP_eq_flag"] = (df["ADEP_mvt"] == df["ADEP_flt"])
    df["SCHED_TIME_month"] = (df["SCHED_TIME_UTC_mvt"].dt.month).astype("category")
    df["SCHED_TIME_day"] = (df["SCHED_TIME_UTC_mvt"].dt.day).astype("category")
    df["SCHED_TIME_dow"] = (df["SCHED_TIME_UTC_mvt"].dt.day_of_week).astype("category")
    df["SCHED_TIME_hour"] = (df["SCHED_TIME_UTC_mvt"].dt.hour).astype("category")
    df["SCHED_TIME_minute"] = (df["SCHED_TIME_UTC_mvt"].dt.minute).astype("category")

    # Numerical features
    df["f1"] = (df["LOBT_flt"] - df["IOBT_flt"]).dt.total_seconds()
    df["f2"] = (df["ARVT_3_flt"] - df["ARVT_1_flt"]).dt.total_seconds()
    df["f3"] = (df["MVT_TIME_UTC_mvt"] - df["EOBT_1_flt"]).dt.total_seconds()
    df["f4"] = (df["MVT_TIME_UTC_mvt"] - df["AOBT_3_flt"]).dt.total_seconds()
    df["f5"] = (df["AOBT_3_flt"] - df["EOBT_1_flt"]).dt.total_seconds()
