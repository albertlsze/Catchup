from fastapi import FastAPI
import pandas as pd
import numpy as np
from datetime import datetime
from typing import List
from pydantic import BaseModel
from Objects.api_objects import Suggestion

@app.get("/suggest", response_model=List[Suggestion])
def get_friend_suggestion():
    # 1. Load selection mart data
    logs = pd.read_csv('../Database/marts/selections.csv')

    # 3. Selection Logic
    suggestions = []
    # eventually i would like to change this functionality to allow for different type of tags that the user can implement beyond local and non local
    # get location based on social media?
    for row in logs.itterrows():
        # get the suggestion from the CSV file
        suggestions.append({
            "name": row['contact_name'],
            "contact_type": row['contact_type'],
            "local": int(row['local']),
            "most_recent_contact": row['most_recent_contact']
        })

    return suggestions
