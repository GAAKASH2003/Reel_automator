import ffmpeg

clips = ['MountainViewFinal.mp4', 'RiverView.mp4', 'Templeview_final.mp4', 'finalClip.mp4']
audio = ffmpeg.input('output_badrinath1.mp3')

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
