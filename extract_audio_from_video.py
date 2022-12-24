import moviepy.editor
from pathlib import Path


try:
    video_file = 'tests/video.mp4'
    video = moviepy.editor.VideoFileClip(video_file)
except:
    print(f"Videofile {video_file} was not found")
    exit()

try:
    audio = video.audio
    audio_file = video_file + '.mp3'
    audio.write_audiofile(audio_file)
except:
    print(f"Can't save audio into {audio_file}")
