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
df = pd.read_csv('data/comments_with_rhetoric_analysis.csv')
# df = df.head(20)

# Load prompt
prompt_fact_check = open('fact_check_prompt.txt', 'r').read()

def get_factcheck_json(datum):
    prompt = prompt_fact_check, "\n Here's the statement: \n{}".format(datum)
    
    factcheck_json = model.generate_content(prompt, generation_config=generation_config)

    # factcheck_json = re.findall(r'\{[.\s\S]*\}', factcheck_json.text)[0]
    return factcheck_json.text

data = df['rhetoric_analysis'].tolist()

error_json = '''
{
  "is_true": None,
  "reason": None
}'''

con = 0
fact_checks = []
for d in data:
    con +=1
    d = json.loads(d)
    datum = d['Chain of thought']['Data']
    fact_check = get_factcheck_json(datum)
    try:
        fact_check = re.findall(r'\{[.\s\S]*\}', fact_check)[0]
    except:
        fact_check = error_json
    fact_checks.append(fact_check)
    print('Appended fact checking analysis in response #{} of {}.'.format(con, len(data)))

    time.sleep(4)

df['fact_check'] = fact_checks

df.to_csv('data/comments_with_rhetoric_analysis.csv', index=False)
