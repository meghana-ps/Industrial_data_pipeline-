import os
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def convert_json_to_csv(input_folder=".venv/input", output_folder=".venv/input_csv"):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".json"):
            json_path = os.path.join(input_folder, filename)
            csv_path = os.path.join(output_folder, filename.replace(".json", ".csv"))

            try:
                df = pd.read_json(json_path, lines=True)
            except ValueError:
                df = pd.read_json(json_path)

            df.to_csv(csv_path, index=False)
            logging.info(f"Converted {filename} → {csv_path}")


def merge_csvs(input_folder=".venv/input_csv", output_file=".venv/input_csv/merged_data.csv"):
    csv_files = [file for file in os.listdir(input_folder) if file.endswith(".csv")]
    df_list = [pd.read_csv(os.path.join(input_folder, file)) for file in csv_files]

    merged_df = pd.concat(df_list, ignore_index=True)
    merged_df.to_csv(output_file, index=False)
    logging.info(f"Merged {len(csv_files)} CSV files into {output_file}")


if __name__ == "__main__":
    convert_json_to_csv()
    merge_csvs()
