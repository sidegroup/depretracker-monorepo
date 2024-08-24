import json
from typing import Union
from deep_translator import GoogleTranslator
from fastapi import FastAPI
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-1.3B")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-1.3B")

app = FastAPI()
@app.get("/")
def read_root():
    return {"ping": "pong"}


@app.get("/translate")
def translate_csv(text: str, source: str, target: str) -> Union[str, None]:
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id["por_Latn"]
    )
    results = tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]
    return results
