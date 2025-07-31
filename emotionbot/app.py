import streamlit as st
from mood_detect import detect_mood
from translate import detect_language, translate_text
from persona_handler import respond_as

st.set_page_config(page_title="EmotionBot 💬", layout="centered")

st.title("WabiSabi 🌈")
st.markdown("Feel free to talk. I'm listening...")

# Choose persona
persona = st.selectbox("Who would you like to talk to?", ["Friend", "Therapist", "Mentor", "Psychologist"])

# Input message
user_input = st.text_area("You:", key="input")

if st.button("Send"):
    # Detect mood
    mood = detect_mood(user_input)

    # Language detection
    lang = detect_language(user_input)

    # Translate to English if needed
    text_en = translate_text(user_input, lang, "en") if lang != "en" else user_input

    # Respond based on persona
    bot_reply = respond_as(persona.lower(), text_en, mood)

    # Translate back if needed
    final_reply = translate_text(bot_reply, "en", lang) if lang != "en" else bot_reply

    st.markdown(f"**Mood Detected:** `{mood}`")
    st.markdown(f"**EmotionBot ({persona}):** {final_reply}")
