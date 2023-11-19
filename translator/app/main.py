import json
from typing import Union
from deep_translator import GoogleTranslator

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"ping": "pong"}


@app.get("/translate")
def translate_csv(text: str, source: str, target: str) -> Union[str, None]:
    try:
        translation = GoogleTranslator(source=source, target=target).translate(text)
    except Exception as e:
        if "Text length need to be between 0 and 5000 characters" in str(e):
            return json.dumps({"error": "Text length need to be between 0 and 5000 characters"})

        return json.dumps({"error": "Something went wrong with translation"})
    return translation
