import streamlit as st
import speech_recognition as sr

st.title("My Voice Chatbot Lab")

# Step A: A button to listen to your voice
if st.button("Click to Speak"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please speak now!")
        audio = r.listen(source)
        
    try:
        # Step B: Convert voice to text
        user_text = r.recognize_google(audio)
        st.write(f"**You said:** {user_text}")
        
        # Step C: Simple chatbot reply logic
        if "hello" in user_text.lower():
            bot_reply = "Hello! How can I help you with your lab today?"
        elif "your name" in user_text.lower():
            bot_reply = "I am your voice-enabled lab chatbot."
        else:
            bot_reply = f"You said: {user_text}. That is a great question!"
            
        # Step D: Display the response
        st.write(f"**Chatbot response:** {bot_reply}")
        
    except Exception as e:
        st.write("Sorry, I could not understand your voice. Please try again.")