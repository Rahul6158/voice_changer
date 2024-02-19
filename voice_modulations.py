from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

def add_modulations_to_audio(audio_file, output_file, pitch_modulation=0, speed_modulation=1.0):
    # Save the uploaded file
    with open("temp_audio_file.mp3", "wb") as f:
        f.write(audio_file.read())

    # Load the audio file
    audio = AudioSegment.from_file("temp_audio_file.mp3")

    # Apply pitch modulation (in semitones, positive for increase, negative for decrease)
    if pitch_modulation != 0:
        octaves = pitch_modulation / 12.0
        new_sample_rate = int(audio.frame_rate * (2 ** octaves))
        audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})

    # Apply speed modulation (1.0 is normal speed, <1.0 for slower, >1.0 for faster)
    audio = audio.speedup(playback_speed=speed_modulation)

    # Export the modified audio to the specified output file
    audio.export(output_file, format="mp3")

    # Remove the temporary file
    os.remove("temp_audio_file.mp3")
