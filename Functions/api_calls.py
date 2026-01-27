from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from typing import List
from Objects.api_objects import Suggestion
from pathlib import Path

# Get the directory where api_calls.py is located
BASE_DIR = Path(__file__).resolve().parent.parent
app = FastAPI(title="Catchup API")

# This tells FastAPI: "It's okay to talk to the React app on port 5173"
app.add_middleware(
                   CORSMiddleware,
                   allow_origins=["http://127.0.0.1:8000/",
                                  "http://localhost:5173",
                                  "http://127.0.0.1:5173",
                                  "http://localhost:5173/",
                                  "http://127.0.0.1:5173/"
                                 ],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                  )
@app.get("/suggest", response_model=List[Suggestion])
def get_friend_suggestion():
    # 1. Load selection mart data
    logs = pd.read_csv(f'{BASE_DIR}/Database/marts/selections.csv')

    # 2. Selection Logic
    suggestions = []
    # eventually i would like to change this functionality to allow for different type of tags that the user can implement beyond local and non local
    # get location based on social media?
    for idx, row in logs.iterrows():
        # get the suggestion from the CSV file
        suggestions.append({
            "name": row['contact_name'],
            "contact_type": row['contact_type'],
            "local": int(row['local']),
            "most_recent_contact": row['most_recent_contact']
        })

    return suggestions

if __name__ == "__main__":
    # fastapi
    print(get_friend_suggestion())