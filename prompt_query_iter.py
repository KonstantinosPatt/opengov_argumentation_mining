from google import genai
from prompt_text import main_prompt
import pandas as pd
import re

client = genai.Client(api_key="AIzaSyC79gY3eduoIp56EEYFglAOUpo9GhvKZzU")

df = pd.read_csv('_SELECT_Article_legislation_id_PublicConsultation_article_id_Art_202502271248.csv')

def get_toulmin_json(article, comment):
    prompt = main_prompt, "\n Here's the article: \n{} \n and here's the comment: \n {} \n".format(article, comment)
    
    toulmin_json = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

    toulmin_json_clean = re.findall(r'\{[.\s\S]*\}', toulmin_json.text)[0]
    return toulmin_json_clean

articles = df['article_text'].tolist()
comments = df['comment_text'].tolist()

responses = []
con = 0
for article, comment in zip(articles, comments):
    response = get_toulmin_json(article, comment)
    responses.append(response)

    print('Appended response #{} of {}.'.format(con, len(comments)))
    con +=1

df['rhetoric_analysis'] = responses

print(df.head())

df.to_csv('comments_with_rhetoric_analysis.csv', index=False)