import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def plot_data(input_file=".venv/output/final_cleaned_data.csv"):
    df = pd.read_csv(input_file)

    sns.set_style("darkgrid")

    plt.figure(figsize=(8, 5))
    sns.histplot(df["cookTime_minutes"], bins=20, kde=True, color="blue")
    plt.title("Cook Time Distribution Histogram")
    plt.xlabel("Minutes")
    plt.ylabel("Frequency")
    plt.savefig(".venv/output/cook_time_hist.png")

    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["cookTime_minutes"], color="orange")
    plt.title("Box Plot for Cook Time")
    plt.savefig(".venv/output/cook_time_boxplot.png")

    plt.figure(figsize=(8, 5))
    sns.histplot(df["prepTime_minutes"], bins=20, kde=True, color="blue")
    plt.title("Prep Time Distribution Histogram")
    plt.xlabel("Minutes")
    plt.ylabel("Frequency")
    plt.savefig(".venv/output/prep_time_hist.png")

    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["prepTime_minutes"], color="orange")
    plt.title("Box Plot for Cook Time")
    plt.savefig(".venv/output/prep_time_boxplot.png")

    logging.info("Plots saved in the output folder.")


if __name__ == "__main__":
    plot_data()
