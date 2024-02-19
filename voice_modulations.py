import streamlit as st
from pydub import AudioSegment
import os

# Function to add pitch and speed modulations to audio
def add_modulations_to_audio(audio_file, output_file, pitch_modulation=0, speed_modulation=1.0):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file, format="mp3")

    # Apply pitch modulation (in semitones, positive for increase, negative for decrease)
    if pitch_modulation != 0:
        octaves = pitch_modulation / 12.0
        new_sample_rate = int(audio.frame_rate * (2 ** octaves))
        audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})

    # Apply speed modulation (1.0 is normal speed, <1.0 for slower, >1.0 for faster)
    audio = audio.speedup(playback_speed=speed_modulation)

    # Export the modified audio to the specified output file
    audio.export(output_file, format="mp3")

# Streamlit code
def main():
    st.title("Audio Modulation")

    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

    if uploaded_file is not None:
        pitch_modulation = st.slider("Pitch modulation (semitones)", -12, 12, 0)
        speed_modulation = st.slider("Speed modulation", 0.5, 2.0, 1.0, 0.1)

        if st.button("Apply Modulations"):
            output_file = "modulated_audio.mp3"
            add_modulations_to_audio(uploaded_file, output_file, pitch_modulation, speed_modulation)

            st.success("Modulations applied successfully!")
            st.audio(output_file, format="audio/mp3")

if __name__ == "__main__":
    main()
