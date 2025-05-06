import whisper


# Load model (no need to specify task/language here)
model = whisper.load_model("base")

# Transcribe and translate the audio
result = model.transcribe("audio_file.mp3", task="translate", language="en")

# Write subtitles to an .srt file
with open("output_subtitles.srt", "w", encoding="utf-8") as f:
    for i, segment in enumerate(result['segments'], start=1):
        # Format timestamp as HH:MM:SS,mmm
        start = segment['start']
        end = segment['end']
        start_time = f"{int(start // 3600):02}:{int((start % 3600) // 60):02}:{int(start % 60):02},{int((start % 1)*1000):03}"
        end_time = f"{int(end // 3600):02}:{int((end % 3600) // 60):02}:{int(end % 60):02},{int((end % 1)*1000):03}"

        f.write(f"{i}\n")
        f.write(f"{start_time} --> {end_time}\n")
        f.write(f"{segment['text']}\n\n")


