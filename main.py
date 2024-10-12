from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import os
import random

app = FastAPI()

@app.get("/")
async def home():
    return RedirectResponse("/docs")

@app.get("/random")
async def random_expansion(acr=None):
    try:
        if acr is not None:
            selected_file = f'{acr.lower()}.txt'
            filepath = os.path.join('expansions', selected_file)
        else:
            files = os.listdir('expansions')
            selected_file = random.choice(files)
            filepath = os.path.join('expansions', selected_file)

        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        selected_line = random.choice(lines)

        return {
            "acronym": selected_file.replace('.txt', '').upper(),
            "expansion": selected_line.strip()
        }
    except Exception as e:
        return {"error": str(e)}