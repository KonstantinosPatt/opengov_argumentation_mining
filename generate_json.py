import json
import pandas as pd

# Load data
df = pd.read_csv('/Users/kp/Documents/EELLAK/arg_min_data/comments_with_rhetoric_analysis_just_toulmin.csv')

print(df.head())

rhetoric = df['rhetoric_analysis'].tolist()


def merge_json_strings(json_strings, output_file):
    merged_data = {}

    for i, json_str in enumerate(json_strings):
        try:
            data = json.loads(json_str)  # Parse JSON from string
            merged_data[f"comment_{i+1}"] = data  # Store each JSON under "comment_X"
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON string {i+1}: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4, ensure_ascii=False)

    print(f"Merged JSON saved to {output_file}")


output_file = "rhetoric_schemes_merged.json"

merge_json_strings(rhetoric, output_file)
