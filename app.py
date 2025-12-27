import os
from dotenv import load_dotenv

# 1) Load .env right away
load_dotenv()

import streamlit as st
from components.voice_input import listen
from components.ai_core import AIAgent
from components.tts import speak, pause_speaking, resume_speaking
from components.history import History

# 2) Now import your skills
from skills import (
    weather,
    translator,
    wiki,
    time as time_skill,
    decision,
)

# Configuration
st.set_page_config(page_title="Advanced Voice Assistant", layout="wide")
agent = AIAgent(api_key=os.getenv("GEMINI_API_KEY"))
history = History()

# Sidebar
with st.sidebar:
    st.header("Settings")
    lang = st.selectbox("TTS Language", ["English", "Hindi"])
    use_skills = st.multiselect(
        "Enable Skills",
        ["weather", "translate", "wiki", "time", "decision"],
    )
    
    # History controls in sidebar
    st.header("Conversation History")
    if st.button("Clear History"):
        history.clear()
        st.success("History cleared!")
    
    # Show last 5 messages in sidebar
    st.subheader("Recent Messages")
    for msg in history.get(limit=5):
        st.text(f"{msg['timestamp']}\n{msg['role'].capitalize()}: {msg['text']}\n")

st.title("Advanced Voice Assistant")
st.write("Click **Talk** or type below to interact.")

# Create columns for controls
col1, col2, col3 = st.columns(3)
text_input = st.text_input("Or type your query here:")

def route_and_respond(text: str) -> str:
    lc = text.lower()
    if "weather" in use_skills and "weather" in lc:
        return weather.get_weather(lc.split("in")[-1].strip())
    if "translate" in use_skills and lc.startswith("translate"):
        try:
            return translator.translate(text.split(maxsplit=1)[1], dest="hi")
        except Exception as e:
            return f"Translation error: {str(e)}"
    if "wiki" in use_skills and ("who is" in lc or "what is" in lc):
        return wiki.wiki_search(lc.replace("who is", "").replace("what is", "").strip())
    if "time" in use_skills and "time" in lc:
        return time_skill.current_time()
    if "decision" in use_skills and "decide" in lc:
        options = [opt.strip() for opt in lc.split("between")[-1].split("or")]
        return f"I decide: {decision.make_smart_decision(options)}"
    return agent.ask(text, context=history.get())

# Voice interaction
with col1:
    if st.button("Talk"):
        try:
            user_text = listen()
            if user_text:
                history.add("user", user_text)
                st.markdown(f"**You:** {user_text}")
                response = route_and_respond(user_text)
                history.add("assistant", response)
                st.markdown(f"**Assistant:** {response}")
                speak(response, lang="hi" if lang == "Hindi" else "en")
        except Exception as e:
            st.error(f"Voice input failed: {e}")

# Control buttons
with col2:
    if st.button("Pause"):
        pause_speaking()
        st.info("Paused speaking")

with col3:
    if st.button("Resume"):
        resume_speaking()
        st.success("Resumed speaking")

# Text interaction
if text_input:
    history.add("user", text_input)
    response = route_and_respond(text_input)
    history.add("assistant", response)
    st.markdown(f"**Assistant:** {response}")
    speak(response, lang="hi" if lang == "Hindi" else "en")

# History display
st.markdown("### Full Conversation History")
st.text_area("History", history.get_formatted_history(), height=300)
