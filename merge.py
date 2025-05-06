import ffmpeg
import os

video_folder = "videoclips"


clips = sorted(
    [os.path.join(video_folder, f) for f in os.listdir(video_folder) if f.endswith(".mp4")],
    key=lambda x: int(os.path.splitext(os.path.basename(x))[0])
)
print(clips)
audio = ffmpeg.input('audio_file.mp3')

resized_streams = []

for clip in clips:
    stream = (
        ffmpeg
        .input(clip)
        .filter('crop', 'ih*9/16', 'ih')  
        .filter('scale', 1080, 1920)     # Resize to standard reel size
        .filter('setsar', '1')           # Ensure pixel aspect ratio is 1:1
        .filter('fps', fps=30, round='up')
        .filter('format', 'yuv420p')
    )
    resized_streams.append(stream)

# Concatenate resized clips (video only, audio=0)
concatenated = ffmpeg.concat(*resized_streams, v=1, a=0)

# Output merged video with audio
ffmpeg.output(concatenated, audio.audio, 'reel_final.mp4', vcodec='libx264', acodec='aac', shortest=None).run(overwrite_output=True)
