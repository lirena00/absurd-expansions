from fastapi import FastAPI
import os
import random

app = FastAPI()

@app.get("/random")
async def random_expansion(abbr=None):
    if abbr is not None:
        selected_file = f'{abbr.lower()}.txt'
        filepath = f'expansions\{selected_file}'
    else:
        files = os.listdir('expansions')
        selected_file = random.choice(files)
        filepath = os.path.join('expansions', selected_file)

    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    selected_line = random.choice(lines)

    return {
        "abbreviation": selected_file.replace('.txt', '').upper(),
        "expansion": selected_line.strip()}
