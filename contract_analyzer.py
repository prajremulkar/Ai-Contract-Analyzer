# AI Contract Analyzer - Minimal Demo
# -----------------------------------
# Principal Product Manager / AI Prototype
# Purpose: Summarizes contracts and flags missing clauses using OpenAI API

# Install dependencies (run in notebook or terminal if needed)
# !pip install openai pandas

import openai
import pandas as pd

# -----------------------
# 1. Set API Key (replace with your key)
# -----------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

# -----------------------
# 2. Example contract text (anonymized)
# -----------------------
contract_text = """
This contract is between Company A and Company B. Payment terms: 30 days. 
Liability: Company B is responsible for damages caused by negligence.
Termination: Either party may terminate with 30-day notice.
"""

# -----------------------
# 3. Define clauses to check
# -----------------------
expected_clauses = [
    "Payment terms",
    "Liability",
    "Termination",
    "Confidentiality",
    "Dispute resolution"
]

# -----------------------
# 4. Use OpenAI API to summarize contract
# -----------------------
def summarize_contract(text):
    prompt = f"""
    Summarize the following contract and list key clauses. Highlight any missing clauses from this list: {expected_clauses}

    Contract:
    {text}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response['choices'][0]['message']['content']

# -----------------------
# 5. Generate summary
# -----------------------
summary = summarize_contract(contract_text)
print("----- Contract Summary -----")
print(summary)

# -----------------------
# 6. Optional: Create a simple DataFrame for review
# -----------------------
results = pd.DataFrame({
    "Clause": expected_clauses,
    "Status": ["Present" if clause.lower() in contract_text.lower() else "Missing" for clause in expected_clauses]
})

print("\n----- Clause Check -----")
print(results)
