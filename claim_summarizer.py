import pandas as pd
import json

# Load data
df = pd.read_csv('/Users/kp/Documents/EELLAK/arg_min_data/comments_with_rhetoric_analysis_just_toulmin.csv')

print(df.head())

rhetoric = df['rhetoric_analysis'].tolist()

print(rhetoric[0])

claims = ''
con = 0
for r in rhetoric:
    con +=1
    r = json.loads(r)
    claim = r['Chain of thought']['Claim']
    # print(con, claim)
    claims += claim + '\n'
# print(claims)

import google.generativeai as genai

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=0.5)   # Set generation configuration

prompt = "I'm going to give you a series of claims concerning whether Greeks of the Diaspora should have the right to vote. I need you to group them and then summarize each group. Also include a count of how many claims are in each group."

answer = model.generate_content(prompt + '\n\n' + claims, generation_config=generation_config)

print(answer.text)

# with open('claim_summaries.md', 'w') as f:
#     f.write(answer.text)

with open('claims.txt', 'w') as c:
    c.write(claims)
