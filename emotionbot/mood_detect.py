from transformers import pipeline

# 🧠 Multiclass Emotion Detection Model
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

def detect_mood(text):
    result = classifier(text)[0][0]  # because top_k=1 returns a list of lists
    return result['label'].lower()  # like "joy", "anger", "sadness", etc.


'''from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_mood(text):
    result = classifier(text)[0]
    label = result['label']
    if label == "POSITIVE":
        return "happy"
    elif label == "NEGATIVE":
        return "sad"
    else:
        return "neutral"'''
