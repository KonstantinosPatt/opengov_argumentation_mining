# Generate data for the articles like comment summary, agreement/disagreement, extra suggestions, etc.

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
df = pd.read_csv('data/comments_with_rhetoric_analysis.csv')
# df = df.head(20)

# print(df.head())

# Load prompt
prompt_agreement = open('agreement_prompt.txt', 'r').read()

def get_agreement_json(article, comment):
    prompt = prompt_agreement, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    agreement_json = model.generate_content(prompt, generation_config=generation_config)
    agreement_json = re.findall(r'\{[.\s\S]*\}', agreement_json.text)[0]

    return agreement_json

articles = df['article_text'].tolist()
comments = df['comment_text'].tolist()

# sample = get_agreement_json(articles[0], comments[0])
# print(sample)

# Add a column in the dataframe for the agreement/disagreement
responses = []
con = 0
for article, comment in zip(articles, comments):
    con +=1
    response = get_agreement_json(article, comment)
    responses.append(response)
    time.sleep(4)

    print('Appended extra data in response #{} of {}.'.format(con, len(comments)))

df['agreement'] = responses

print(df.head())

# Save to csv
df.to_csv('data/comments_with_rhetoric_analysis.csv', index=False)
