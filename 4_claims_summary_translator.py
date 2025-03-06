import google.generativeai as genai

# setup Gemini
api_key = open('/Users/kp/Documents/EELLAK/arg_min_data/gemini_key.txt', 'r').read().strip()
genai.configure(api_key=api_key)    # Configure your API key
model = genai.GenerativeModel("gemini-2.0-flash")   # Set up the model
generation_config = genai.types.GenerationConfig(temperature=1)   # Set generation configuration

# Load data
summary = open('data/claim_summaries.md', 'r').read()
# print(summary)

prompt = "Translate the following English text to Greek: " + summary

answer = model.generate_content(prompt, generation_config=generation_config)

# print(answer.text)

with open('data/claim_summaries_gr.md', 'w') as f:
    f.write(answer.text)
