from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play
import os

load_dotenv()

client = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

audio_stream = client.text_to_speech.convert(
   text = """Socho ek jagah...
Jahaan pahaadon ki hawa kahaniyan sunaati hai.

Yeh hai Badrinath —
Himalayas ke beech, 10 hazaar feet upar.

Ghanton ki awaaz, agarbatti ki khushboo,
aur Alaknanda nadi ka sukoon...

Mandir ke saamne khade ho kar —
ek alag hi shanti mehsoos hoti hai.

Garm chai lo,
barf se dhake pahaadon ko dekho,
aur khud se milo.

Badrinath ek manzil nahi,
ek anubhav hai.

Aao —
Apna agla safar yahaan se shuru karo."""
,

    voice_id="FmBhnvP58BK0vz65OOj7",
    model_id="eleven_multilingual_v2",
    output_format="mp3_44100_128",
     voice_settings={
        "stability": 0.4,
        "similarity_boost": 0.75,
        "speed": 0.75         
    }
)

with open("output_badrinath1.mp3", "wb") as f:
    for chunk in audio_stream:
        f.write(chunk)