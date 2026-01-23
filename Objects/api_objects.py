from fastapi import FastAPI
import pandas as pd
import numpy as np
from datetime import datetime
from pydantic import BaseModel

# Create the app instance
app = FastAPI(title="Catchup API")

# Updated Model: Removed 'score'
class Suggestion(BaseModel):
    name: str
    contact_type: str
    local: int
    most_recent_contact: datetime
