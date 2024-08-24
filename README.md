# Text-to-Music Generation with MusicGen 🎵

This repository houses a web application built with Streamlit, enabling users to create music based on textual descriptions using Meta's Audiocraft library and the MusicGen model.

## Core Features

- Text-Based Input: Provide a description of the music you wish to generate.
- Duration Selection: Choose the length of the music to be generated (up to 20 seconds).
- Music Creation: The app produces music aligned with the given description and chosen 
  duration.
- In-Browser Playback: Play the generated music directly within the web application.
## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/text-to-music-generator.git
    cd text-to-music-generator

    ```

2. **Set Up a Virtual Environment:**:
    ```bash
    python3 -m venv music-env
    source music-env/bin/activate
    ```

3. **Install the required Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use

1. **Launch the Application**:
    ```bash
    streamlit run app.py
    ```

2. **Access the Interface: Open your preferred web browser and navigate to http://localhost:8501 to interact with the app.**

3.**Generate Music**:

- **Enter a text description of the music in the provided area**.
- **Select the desired duration using the slider**.
- **Press "Generate Music" to produce and listen to your customized music**.

<img width="656" alt="332428522-da41fbea-6565-4ac7-a78f-559666ff4b6f" src="https://github.com/user-attachments/assets/702fe2d0-f20d-44bf-a27b-405cb76a7eac">

## Example

1. Type in a description such as "80s pop tune with strong drums and synth melodies."
2. Choose a duration, for example, 10 seconds.
3. Click the "Generate Music" button.
4.Enjoy listening to the generated music.

## Requirements

- `streamlit`
- `audiocraft`
- `torchaudio`
- `scipy`

## Directory Structure

- `app.py`: The main Streamlit application script.
- `requirements.txt`: The dependencies required to run the app.
- `audios/`: Directory to save generated audio files

## Acknowledgements

- This app utilizes Meta's Audiocraft library.
- Special thanks to the team behind the MusicGen model.

