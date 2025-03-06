import google.generativeai as genai
from prompt_text import prompt_toulmin, system_instruction
import pandas as pd
import time
import re

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=1)   # Set generation configuration

# Load data
df = pd.read_csv('opengov_data_sample.csv')
df = df.head(20)

def get_toulmin_json(article, comment):
    prompt = prompt_toulmin, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    toulmin_json = model.generate_content(prompt, generation_config=generation_config)

    toulmin_json_clean = re.findall(r'\{[.\s\S]*\}', toulmin_json.text)[0]
    return toulmin_json_clean

articles = df['article_text'].tolist()
comments = df['comment_text'].tolist()


response = get_toulmin_json(articles[2], comments[2])
print(response)

responses = []
responses_j = ''
con = 0
for article, comment in zip(articles, comments):
    con +=1
    response = get_toulmin_json(article, comment)
    responses.append(response)
    responses_j += response + ',\n'
    time.sleep(4)

    print('Appended response #{} of {}.'.format(con, len(comments)))


df['rhetoric_analysis'] = responses

print(df.head())

df.to_csv('/Users/kp/Documents/EELLAK/arg_min_data/comments_with_rhetoric_analysis_just_toulmin.csv', index=False)
# with open('/Users/kp/Documents/EELLAK/arg_min_data/comments_with_rhetoric_analysis.json', 'w') as f:
#     f.write(responses_j)