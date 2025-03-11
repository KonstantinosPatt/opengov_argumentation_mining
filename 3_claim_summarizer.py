import google.generativeai as genai
import pandas as pd
import json

# Load data
df = pd.read_csv('data/comments_with_rhetoric_analysis.csv')

# print(df.head())

rhetoric = df['rhetoric_analysis'].tolist()

for r in rhetoric[:5]:
    print(r)

claims = ''
con = 0
for r in rhetoric:
    con +=1
    r = json.loads(r)
    # claim = r['Chain of thought']['Claim']
    print(con, claim)
    claims += claim + '\n'

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=0.5)   # Set generation configuration

prompt = "I'm going to give you a series of claims. I need you to group them and then summarize each group. Also include a count of how many claims are in each group."

answer = model.generate_content(prompt + '\n\n' + claims, generation_config=generation_config)

# print(answer.text)

with open('data/claim_summaries.md', 'w') as f:
    f.write(answer.text)

with open('data/claims.txt', 'w') as c:
    c.write(claims)
