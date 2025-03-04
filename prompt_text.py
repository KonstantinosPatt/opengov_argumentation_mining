
main_prompt = '''
You are a computational linguist, working on a project about argument mining. You have to analyze the citizens' and organizations' comments on bills and articles, as can be found at the open deliberation platform of the Greek government opengov.gr. You must provide a structured JSON object with the following keys:
"Agreement/Disagreement": You mention whether the commenter agrees or disagrees, using only the labels “agree” and “disagree”.
"Level": You mention whether the commenter agrees or disagrees regarding the whole bill, the whole article, or a part of it, using only the labels “bill”, “article”, or “paragraph”. ALWAYS include the “Level” section in your answer.
"Chain of thought": Provide me with the commenter’s chain of thought, based on Toulmin’s model. Include the labels “Claim”, “Data”, “Warrant”, “Backing”, “Qualifier”, and “Rebuttal”. In the “Data” section mention ONLY the explicit data; otherwise write “None”. In the “Rebuttal” section, only include counterarguments explicitly stated by the commenter. Do NOT infer or generate counterarguments on your own. If no rebuttal is provided, write “None”. In the “Qualifier” section mention ONLY the explicit qualifiers; otherwise write “None”. Remember NOT to include any suggestions under the “Claim” label as well.
“Extra suggestions”: You add any complementary suggestions given by the commenter. 
Before the examples, please ensure that your response is strictly formatted as a JSON object with exactly the keys "Agreement/Disagreement", "Level", "Chain of thought", and “Extra suggestions”. Do not include any additional text before or after the JSON.

Examples:

Example #1
{
  "Agreement/Disagreement": {
    "Paragraph": {
      "Paragraph no": "1",
      "Stance": "disagree",
      "Comment": "Disagrees with the current immigration policies, advocating for strict repatriation and limited, selective re-entry.",
      "Chain of thought": {
        "Claim": "Greece cannot help the 4.5 billion people in Asia suffering from poverty and hardship.",
        "Data": "Asia has 4.5 billion people in dire conditions. Greece is a small country ("Ελλαδίτσα") with its own problems.",
        "Warrant": "A small country with limited resources cannot save a vast population facing immense challenges.",
        "Backing": "The statement "Είμαστε μια χώρα με πολλά προβλήματα" (We are a country with many problems) implies limited capacity to help others.",
        "Qualifier": "Implicitly conveyed through the rhetorical question "Μπορεί η Ελλαδίτσα μας να τους σώσει;" (Can our little Greece save them?)",
        "Rebuttal": "None explicitly stated, but a potential counter argument could be that helping doesn't necessarily mean solving all their problems, but perhaps offering some form of assistance."
      }
    },
  "Extra suggestions": "None"
}


Example #2
{
  "Agreement/Disagreement": {
    "Paragraph": {
      "Paragraph no": "1",
      "Stance": "agree",
      "Comment": "Disagrees with the current immigration policies, advocating for strict repatriation and limited, selective re-entry.",
      "Chain of thought": {
        "Claim": "The Greek government is taking the right measures for immigrants.",
        "Data": "The government is taking some measures for immigrants. The text is vague about what these measures are.",
        "Warrant": "The underlying assumption is that combating far-right extremism and racism is inherently good and desirable. It also implies that the government's actions are aligned with this goal.",
        "Backing": "The connection made between far-right racism and fascist societies. This suggests that such ideologies are abhorrent and must be opposed. The phrase "It's time" implies a long overdue action.",
        "Qualifier": "The word "seems" ("φαίνεται") weakens the claim slightly, suggesting a degree of uncertainty about the effectiveness or true nature of the measures. However, the overall tone is positive.",
        "Rebuttal": "Potential rebuttals could be that the measures are insufficient, ineffective, serve other hidden agendas, or are excessive. The text doesn't address specific rebuttals."
      }
    }
  },
  "Extra suggestions": "None"
}

'''

system_instruction = ''