# from google import genai
# from prompt_text import main_prompt
# import pandas as pd
# import time
# import re

# api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
# client = genai.Client(api_key=api_key)


# prompt =  'Write a song about the port of Peiraius'
    
# answer = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)

# print(answer.text)


# import google.generativeai as genai

# # Configure your API key
# api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
# genai.configure(api_key=api_key)

# # Set up the model
# model = genai.GenerativeModel("gemini-2.0-flash")

# # Set generation configuration
# generation_config = genai.types.GenerationConfig(
#     temperature=0.5
# )

# # Generate content
# response = model.generate_content(
#     "Write a short poem about the ocean.",
#     generation_config=generation_config
# )

# print(response.text)

