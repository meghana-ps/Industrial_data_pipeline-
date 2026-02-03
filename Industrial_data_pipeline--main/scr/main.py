import logging
from scripts.data_preprocessing import convert_json_to_csv, merge_csvs
from scripts.data_cleaning import clean_data
from scripts.data_analysis import filter_beef_recipes, calculate_avg_cook_time
from scripts.data_visualization import plot_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("Starting Data Engineering Pipeline...")

    convert_json_to_csv()
    merge_csvs()
    clean_data()
    filter_beef_recipes()
    calculate_avg_cook_time()
    plot_data()
    logging.info("Pipeline execution completed.")

if __name__ == "__main__":
    main()

