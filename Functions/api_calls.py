from fastapi import FastAPI
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List
from pydantic import BaseModel
from sklearn.preprocessing import MinMaxScaler

# Create the app instance
app = FastAPI(title="Catchup API")

# Updated Model: Removed 'score'
class Suggestion(BaseModel):
    name: str
    contact_id: int
    local: int


@app.get("/suggest", response_model=List[Suggestion])
def get_friend_suggestion():
    # 1. Load your raw data
    member_contacts = pd.read_csv('../Database/raw/member_contacts.csv')
    # Assuming this file has 'days_since_contact', 'type_of_contact', and 'number_of_contacts'
    logs = pd.read_csv('../Database/marts/contact_member_logs.csv')

    # 2. Calculate the score in-memory (since it's not in the file)
    # This is the logic from your notebook Step 2
    normalize_columns = ['type_of_contact', 'days_since_contact', 'number_of_contacts']
    scaler = MinMaxScaler()

    # We'll calculate the score for the whole set for simplicity here
    # or you could split by local/non-local as you did in the notebook
    temp_df = logs.copy()
    for col in normalize_columns:
        temp_df[f"norm_{col}"] = scaler.fit_transform(temp_df[[col]])

    # Inverting as per your notebook logic
    temp_df['inv_norm_type'] = 1 - temp_df['norm_type_of_contact']
    temp_df['inv_norm_count'] = 1 - temp_df['norm_number_of_contacts']

    # Your formula
    temp_df['calculated_score'] = temp_df[['inv_norm_type', 'norm_days_since_contact', 'inv_norm_count']].mean(axis=1)

    # 3. Selection Logic
    suggestions = []
    for is_local in [1, 0]:
        subset = temp_df[temp_df['local'] == is_local].copy()

        # Weighted selection
        total_score = subset['calculated_score'].sum()
        subset['percent_cut'] = (subset['calculated_score'] / total_score) * 100
        subset['cum_sum'] = subset['percent_cut'].cumsum()

        random_val = np.random.rand() * 100
        # Find the first row where cum_sum is greater than our random number
        selected_row = subset[subset['cum_sum'] >= random_val].iloc[0]

        # Get the name from the other CSV
        name = member_contacts[member_contacts['contact_id'] == selected_row['contact_id']]['name'].iloc[0]

        suggestions.append({
            "name": name,
            "contact_id": int(selected_row['contact_id']),
            "local": int(selected_row['local'])
        })

    return suggestions
