import pandas as pd

def convert_iso_to_minutes(duration):
    try:
        if pd.isna(duration) or duration == "":
            return None
        return int(isodate.parse_duration(duration).total_seconds() / 60)
    except:
        return None
