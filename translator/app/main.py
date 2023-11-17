from typing import Union
from deep_translator import GoogleTranslator

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"ping": "pong"}


@app.get("/translate")
def translate_csv(text: str, source: str, target: str) -> Union[str, None]:
    return GoogleTranslator(source=source, target=target).translate(text)
