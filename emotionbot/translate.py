from langdetect import detect
from transformers import pipeline

translator_en_hi = pipeline("translation_en_to_hi", model="Helsinki-NLP/opus-mt-en-hi")
translator_hi_en = pipeline("translation", model="Helsinki-NLP/opus-mt-hi-en")

def detect_language(text):
    return detect(text)

def translate_text(text, src_lang, tgt_lang):
    if src_lang == "en" and tgt_lang == "hi":
        return translator_en_hi(text)[0]['translation_text']
    elif src_lang == "hi" and tgt_lang == "en":
        return translator_hi_en(text)[0]['translation_text']
    return text  # No change if already in target
