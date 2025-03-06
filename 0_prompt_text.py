

system_instruction = ''


prompt_toulmin = '''
You are a computational linguist working on argument mining. Your task is to analyze citizens' and organizations' comments on bills and articles from the Greek government’s open deliberation platform (opengov.gr). You must extract and structure the argumentation using Toulmin’s model, strictly following the format below. 

For each comment, return an analyisis structured as follows:

"Claim": The main argument made by the commenter. Do NOT include extra suggestions here.
"Data": The factual evidence or reasoning that supports the claim.
"Warrant": The logical connection between the claim and the data.
"Backing": Additional justification or background information that strengthens the warrant.
"Qualifier": Any words or phrases that modify the strength of the claim (e.g., “probably,” “seems,” “likely”).
"Rebuttal": ONLY include explicitly stated counterarguments. Do NOT infer or generate counterarguments. If none is stated, omit this section entirely.

You must return a strict JSON object, based on the example below:
{
"Chain of thought": {
        "Claim": "Greece cannot help the 4.5 billion people in Asia suffering from poverty and hardship",
        "Data": "Asia has 4.5 billion people in dire conditions. Greece is a small country ('Ελλαδίτσα') with its own problems",
        "Warrant": "A small country with limited resources cannot save a vast population facing immense challenges",
        "Backing": "The statement 'Είμαστε μια χώρα με πολλά προβλήματα' (We are a country with many problems) implies limited capacity to help others",
        "Qualifier": "Implicitly conveyed through the rhetorical question 'Μπορεί η Ελλαδίτσα μας να τους σώσει;' (Can our little Greece save them?)",
        "Rebuttal": "None explicitly stated, but a potential counter argument could be that helping doesn't necessarily mean solving all their problems, but perhaps offering some form of assistance"
      }
}

Be careful to never use double quotes inside the strings. Always use single quotes.
'''