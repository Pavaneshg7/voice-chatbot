import streamlit as st
from streamlit_mic_recorder import speech_to_text

st.title("My Voice Chatbot Lab")
st.write("Click the button below and speak into your microphone:")

# This uses the browser's microphone directly on the cloud web page
text = speech_to_text(language='en', start_prompt="Click to Speak", stop_prompt="Stop Recording", key='STT')

if text:
    st.write(f"**You said:** {text}")
    
    # Simple chatbot response logic
    if "hello" in text.lower():
        bot_reply = "Hello! How can I help you with your lab today?"
    elif "your name" in text.lower():
        bot_reply = "I am your voice-enabled lab chatbot."
    else:
        bot_reply = f"You received: {text}. That's a great input!"
        
    st.write(f"**Chatbot response:** {bot_reply}")
