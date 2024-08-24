import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write
import streamlit as st
import scipy

print("Application initialized")


def initialize_model():
    music_model = MusicGen.get_pretrained('facebook/musicgen-small')
    return music_model

def create_music(description, duration_seconds: int):
    print(f"Generating music for: '{description}' with duration: {duration_seconds} seconds")
    
   
    music_model = initialize_model()
    music_model.set_generation_params(duration=duration_seconds) 
    
    
    waveform = music_model.generate([description])
    
    return waveform, music_model.sample_rate

def run_app():
    st.title("Text-to-Music Generator 🎵")

    with st.expander("How does it work?"):
        st.write("This app generates music from text descriptions using Meta's Audiocraft library, employing the MusicGen Small model.")

    input_text = st.text_area("Describe the music you want to generate...")
    duration_input = st.slider("Select duration (in seconds)", min_value=0, max_value=20, value=10)

    if input_text and duration_input:
        if st.button("Generate Music"):
            st.write("Generating music, please wait...")
            waveform, sample_rate = create_music(input_text, duration_input)
          
            output_path = "generated_audio/audio_output"
            for idx, single_waveform in enumerate(waveform):
                audio_write(f"{output_path}", single_waveform.cpu(), sample_rate, strategy="loudness", loudness_compressor=True)
            st.audio(f"{output_path}.wav", format='audio/wav')

if __name__ == "__main__":
    run_app()
