#!/bin/bash

# Ensure the script stops on errors
set -e

# Run each Python script in sequence
python3 1_prompt_generate_toulmin.py
python3 2_prompt_generate_extra_data.py
python3 3_claim_summarizer.py
python3 4_claims_summary_translator.py
python3 5_prompt_fact_checker.py
python3 6_compile_json.py