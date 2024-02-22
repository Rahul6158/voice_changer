import streamlit as st
from pydub import AudioSegment
import io

# Streamlit app title
st.title("Audio Player")

# Display file uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["mp3"])

# If an audio file is uploaded
if audio_file is not None:
    # Read the uploaded file
    audio_bytes = audio_file.read()

    # Load the audio file into Pydub
    try:
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes), format="mp3")
        st.success("Audio file loaded successfully!")
    except Exception as e:
        st.error(f"Error loading audio file: {str(e)}")
