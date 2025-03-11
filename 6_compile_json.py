import pandas as pd
import json
from collections import OrderedDict
import re

# Load data
df = pd.read_csv('/Users/kp/Documents/EELLAK/arg_min/data/comments_with_rhetoric_analysis.csv')
# print(df)

leg_id, art_id, com_id = df['legislation_id'].tolist(), df['article_id'].tolist(), df['comment_id'].tolist()
rhetoric = df['rhetoric_analysis'].tolist()
agreement = df['agreement'].tolist()
fact_check = df['fact_check'].tolist()

ids = []
for x,y,z in zip(leg_id, art_id, com_id):
    id = 'leg_' + str(x) + '_art_' + str(y) + '_com_' + str(z)
    ids.append(id)
    # print(id)


i  = 0 
id = ids[i]
rhetoric_j = json.loads(rhetoric[i]) 
agreement_j = json.loads(agreement[i]) 
fact_check_j = json.loads(fact_check[i])
for i in range(1, len(df)):
    rhetoric[i] = re.sub(': None', ': "None"', rhetoric[i])
    agreement[i] = re.sub(': None', ': "None"', agreement[i])
    fact_check[i] = re.sub(': None', ': "None"', fact_check[i])

combined_jsons = []
for i in range(1, len(df)):
    id = ids[i]
    rhetoric_j = json.loads(rhetoric[i]) 
    agreement_j = json.loads(agreement[i]) 
    fact_check_j = json.loads(fact_check[i])
    agreement_j['comment_id'] = id
    agreement_j['Chain of thought'] = rhetoric_j['Chain of thought']
    agreement_j['Data fact checking'] = fact_check_j
    
    # Reorder dictionary
    agreement_j = OrderedDict([
                                ('comment id', agreement_j['comment_id']),
                                ('summary', agreement_j['Summary']),
                                ('agreement', agreement_j['agreement']),
                                ('level', agreement_j['Level']),
                                ('chain of thought', agreement_j['Chain of thought']),
                                ('data fact checking', agreement_j['Data fact checking']),
                                ('suggestions', agreement_j['Suggestions'])
    ])
    combined_jsons.append(agreement_j)

# Save data
with open('data/comments_rhetoric_analysis.json', 'w') as f:
    json.dump(combined_jsons, f, indent=4)