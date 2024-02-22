import streamlit as st

# Streamlit app title
st.title("Audio Player")

# Display file uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["mp3"])

# If an audio file is uploaded
if audio_file is not None:
    # Display the uploaded audio file
    st.audio(audio_file, format='audio/mp3')

    # Play the uploaded audio file
    st.audio(audio_file, format='audio/mp3', start_time=0)
