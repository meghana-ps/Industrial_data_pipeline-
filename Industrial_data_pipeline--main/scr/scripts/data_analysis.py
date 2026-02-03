import pandas as pd
import ast
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
def parse_ingredients(ingredient_str):
    try:
        if isinstance(ingredient_str, list):
            return ingredient_str
        return ast.literal_eval(ingredient_str) if isinstance(ingredient_str, str) and ingredient_str.startswith(
            "[") else [ingredient_str]
    except (ValueError, SyntaxError):
        logging.warning(f"Failed to parse ingredients: {ingredient_str}")
        return []

def filter_beef_recipes(input_file=".venv/output/cleaned_data.csv", output_file=".venv/output/beef_recipes.csv"):
    df = pd.read_csv(input_file)
    df["ingredients"] = df["ingredients"].apply(parse_ingredients)
    df_beef = df[df["ingredients"].apply(lambda ingredients: any("beef" in item.lower() for item in ingredients))]
    df_beef.to_csv(output_file, index=False)
    logging.info(f"Beef recipes are extracted and saved to {output_file} ({len(df_beef)} rows)")\

def calculate_avg_cook_time(input_file=".venv/output/beef_recipes.csv", output_file=".venv/output/processed_data.csv"):
    df = pd.read_csv(input_file)
    df["avg_total_cooking_time"] = df["cookTime_minutes"] + df["prepTime_minutes"]
    def classify_difficulty(time):
        return "easy" if time < 30 else "medium" if time <= 60 else "hard"
    df["difficulty"] = df["avg_total_cooking_time"].apply(classify_difficulty)
    df_final = df.groupby("difficulty", as_index=False)["avg_total_cooking_time"].mean()
    df_final.to_csv(output_file, index=False)
    logging.info(f"Processed dataset saved to {output_file}")


if __name__ == "__main__":
    filter_beef_recipes()
    calculate_avg_cook_time()
