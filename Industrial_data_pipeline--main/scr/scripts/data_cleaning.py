import pandas as pd
import isodate
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def convert_iso_to_minutes(duration):
    try:
        if pd.isna(duration) or duration == "":
            return None
        return int(isodate.parse_duration(duration).total_seconds() / 60)
    except:
        return None

def clean_data(input_file=".venv/input_csv/merged_data.csv", output_file=".venv/output/cleaned_data.csv"):
    df = pd.read_csv(input_file)

    df["cookTime_minutes"] = df["cookTime"].apply(convert_iso_to_minutes)
    df["prepTime_minutes"] = df["prepTime"].apply(convert_iso_to_minutes)

    df.fillna({"cookTime_minutes": df["cookTime_minutes"].median(), "prepTime_minutes": df["prepTime_minutes"].median()}, inplace=True)

    df["total_cook_time"] = df["cookTime_minutes"] + df["prepTime_minutes"]

    df.to_csv(output_file, index=False)
    logging.info(f"Cleaned data saved to {output_file}")

def cap_outliers(df, column):
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df[column] = df[column].apply(
            lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)

        return df
df = pd.read_csv(".venv/output/cleaned_data.csv")
for col in ["cookTime_minutes", "prepTime_minutes", "total_cook_time"]:
        df = cap_outliers(df, col)
df.to_csv(".venv/output/final_cleaned_data.csv", index=False)

if __name__ == "__main__":
    clean_data()
