# Video Reel Generator

This project automates the creation of engaging video reels by combining a voiceover, subtitles, and video clips. The process involves generating the voiceover from a script, creating subtitles, searching for video clips, trimming them, and merging everything into a final reel that can be used for social media platforms like Instagram Reels.

## Workflow

### Step 1: Writing a Script

- **ChatGPT** or manual writing can be used to generate the script for the voiceover. This script will serve as the basis for the narration in the final video.

### Step 2: Generating Voice From Script

- Use **Eleven Labs API** or **TTSmaker** (an online tool for Hindi text-to-speech) to generate the voiceover.
- If using **Eleven Labs**, ensure you have an API key and integrate it into your code for generating the audio file.
- **TTSmaker** is a great tool for generating high-quality Hindi voiceovers.

### Step 3: Generating Subtitles File and Timeframe Report

- **Whisper AI**: Use Whisper to transcribe the audio and generate the subtitle file (`.srt` format).
- **Generate Timeframe Report**: Once the subtitles are generated, use **ChatGPT** with the following prompt to generate a clean timeframe report:

  ```plaintext
  "I have a subtitle file in .srt format. Generate a clean timeframe report showing: segment number, start time, end time, duration in seconds, visual suggestion for reels, and subtitle text. Also, suggest a visually clean and readable tabular format to present the data for use in reports or overlays."
  ```

### Step 4: Gathering the video clips and place them in a folder

### Step 5: Merging the audio and video files using merge.py file
