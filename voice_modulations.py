import streamlit as st
import io
from pydub import AudioSegment
from pydub.utils import get_encoder_name

# Set the path to ffmpeg and ffprobe executable files
AudioSegment.ffmpeg = "/fftools/ffmpeg.h"
AudioSegment.ffprobe = "fftools/ffprobe.c"

# Streamlit app title
st.title("Audio Player")

# Display file uploader for audio files
audio_file = st.file_uploader("Upload an audio file", type=["mp3"])

# If an audio file is uploaded
if audio_file is not None:
    try:
        # Load the uploaded audio file into Pydub
        audio_bytes = audio_file.read()
        audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
        
        # Display the uploaded audio file
        st.audio(audio_bytes, format='audio/mp3')
    except Exception as e:
        st.error(f"Error loading audio file: {str(e)}")
