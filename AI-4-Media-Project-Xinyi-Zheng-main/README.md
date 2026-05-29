# AI-4-Media-Project-Xinyi-Zheng


## Student name: Xinyi Zheng
## Student number: 24005614
## Project title:Gesture-Driven Audiovisual Interaction
## Link to project video recording: https://ual.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=d020072b-d383-4688-bc8f-b2a6005c7af3

# Setup instructions:

Instructions for setting up the conda environment, any files that need downloading, and the specific technical instructions for how to run your code project go here:


1. Activate the environment:  
   Activate the environment using:
   ```bash
   conda activate aim
   ```

2. Install required Python packages:  
   Install the necessary packages using pip:
   ```bash
   pip install mediapipe opencv-python numpy pydub pyaudio
   ```
3.Install FFmpeg (for audio conversion):  
   FFmpeg is required for converting audio files to the correct format. Install it using the following commands:
   - On Ubuntu/Debian:
     ```bash
     sudo apt-get install ffmpeg
     ```
   - On macOS (using Homebrew):
     ```bash
     brew install ffmpeg
     ```
   - On Windows:  
     Download FFmpeg from [here](https://ffmpeg.org/download.html) and add it to your system PATH.

4. Downloading Required Files
The project requires the following files to run:
Music Tracks:  
   Download three music tracks in `.wav` format and place them in the project directory. Name them as follows:
   - `output.wav`
   - `output2.wav`
   - `output3.wav`

   These tracks will be used for audio playback and switching.

5. MediaPipe Models:  
   The MediaPipe Hands model will be automatically downloaded when you run the code. No manual download is required.

6. Running the Project

Once the environment is set up and the required files are downloaded, follow these steps to run the project:

Run the main script:  
   Execute the following command to start the gesture-driven audiovisual interaction system:
   ```bash
   work.py

```


