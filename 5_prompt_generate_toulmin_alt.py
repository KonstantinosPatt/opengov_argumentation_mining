import google.generativeai as genai
import pandas as pd
import json
import time
import re

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=1)   # Set generation configuration

# Load data
df = pd.read_csv('data/opengov_data_sample.csv')
# df = df.head(20)

# Load prompt
prompt_toulmin_6 = open('toulmin_prompt.txt', 'r').read()
prompt_toulmin_3 = open('toulmin_prompt_3.txt', 'r').read()


def get_toulmin_json_6(article, comment):
    prompt = prompt_toulmin_6, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    toulmin_json = model.generate_content(prompt, generation_config=generation_config)

    toulmin_json_clean = re.findall(r'\{[.\s\S]*\}', toulmin_json.text)[0]
    return toulmin_json_clean

def get_toulmin_json_3(article, comment):
    prompt = prompt_toulmin_3, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    toulmin_json = model.generate_content(prompt, generation_config=generation_config)

    toulmin_json_clean = re.findall(r'\{[.\s\S]*\}', toulmin_json.text)[0]
    return toulmin_json_clean

articles = df['article_text'].tolist()
comments = df['comment_text'].tolist()

# Add a column in the dataframe for the rhetorical analysis (full toulmin)
responses_6 = []
con = 0
for article, comment in zip(articles, comments):
    con +=1
    response_6 = get_toulmin_json_6(article, comment)
    responses_6.append(response_6)
    time.sleep(4)

    print('Appended response #{} of {}.'.format(con, len(comments)))

df['rhetoric_analysis_6'] = responses_6


# Add a column in the dataframe for the rhetorical analysis (half toulmin)
responses_3 = []
con = 0
for article, comment in zip(articles, comments):
    con +=1
    response_3 = get_toulmin_json_3(article, comment)
    responses_3.append(response_3)
    time.sleep(4)

    print('Appended response #{} of {}.'.format(con, len(comments)))

df['rhetoric_analysis_3'] = responses_3

# print(df.head())

# Save to csv
df.to_csv('data/comments_with_rhetoric_analysis_6_and_3.csv', index=False)

# Create a json file with all the rhetorical analysis
# combined_json = []

# for r in responses:
#     r = json.loads(r)
#     combined_json.append(r)

# with open('data/rhetoric_analysis.json', 'w') as f:
#     json.dump(combined_json, f, indent=4)
