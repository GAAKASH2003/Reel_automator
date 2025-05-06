from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os

load_dotenv()

with open("script.txt", "r", encoding="utf-8") as file:
    script_text = file.read()

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_stream = client.text_to_speech.convert(
   text = script_text
,

    voice_id="FmBhnvP58BK0vz65OOj7",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
     voice_settings={
        "speed": 0.8         
    }
)

with open("audio_file.mp3", "wb") as f:
    for chunk in audio_stream:
        f.write(chunk)