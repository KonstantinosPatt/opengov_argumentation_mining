import google.generativeai as genai
import pandas as pd
import time
import re

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=1)   # Set generation configuration

# Load data
df = pd.read_csv('data/opengov_data_sample.csv')
# Choose comments from a specific article, in this case article 1
df = df.loc[df['article_id'] == 1]

# Load prompt
prompt_toulmin = open('toulmin_prompt_3.txt', 'r').read()

def get_toulmin_json(article, comment):
    prompt = prompt_toulmin, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    toulmin_json = model.generate_content(prompt, generation_config=generation_config)

    toulmin_json_clean = re.findall(r'\{[.\s\S]*\}', toulmin_json.text)[0]
    return toulmin_json_clean

articles = df['article_text'].tolist()
comments = df['comment_text'].tolist()

# Add a column in the dataframe for the rhetorical analysis
responses = []
con = 0
for article, comment in zip(articles, comments):
    con +=1
    response = get_toulmin_json(article, comment)
    responses.append(response)
    time.sleep(4)

    print('Appended toulmin analysis in response #{} of {}.'.format(con, len(comments)))

df['rhetoric_analysis'] = responses

# print(df.head())

# Save to csv
df.to_csv('data/comments_with_rhetoric_analysis.csv', index=False)
