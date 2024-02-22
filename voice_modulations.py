from pydub import AudioSegment
import streamlit as st

# Function to add modulations to the translated audio
def add_modulations_to_audio(audio_file, output_file, pitch_modulation=0, speed_modulation=1.0):
    # Load the audio file
    audio = AudioSegment.from_file(audio_file)

    # Apply pitch modulation (in semitones, positive for increase, negative for decrease)
    audio = audio + pitch_modulation

    # Apply speed modulation (1.0 is normal speed, <1.0 for slower, >1.0 for faster)
    audio = audio.speedup(playback_speed=speed_modulation)

    # Save the modified audio file
    audio.export(output_file, format="mp3")

def main():
    st.title("Audio Modulation")

    # Display audio file
    audio_file = st.file_uploader("Upload audio file", type=["mp3"])

    if audio_file is not None:
        # Display sliders for pitch and speed modulation
        pitch_modulation = st.slider("Pitch Modulation", -12, 12, 0)
        speed_modulation = st.slider("Speed Modulation", 0.5, 2.0, 1.0, step=0.1)

        # Apply modulations and save the modified audio
        if st.button("Apply Modulations"):
            output_file = "output_audio_with_modulations.mp3"
            add_modulations_to_audio(audio_file, output_file, pitch_modulation, speed_modulation)
            st.success("Modulations applied successfully. Click the link below to download the modified audio.")
            st.audio(output_file, format="audio/mp3")

if __name__ == "__main__":
    main()
