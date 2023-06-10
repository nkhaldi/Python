from moviepy.editor import VideoFileClip

try:
    video_file = "tests/video.mp4"
    video = VideoFileClip(video_file)
except Exception as e:
    print(f"Videofile {video_file} was not found. {e}")
    exit()

try:
    audio = video.audio
    audio_file = video_file + ".mp3"
    audio.write_audiofile(audio_file)

except Exception as e:
    print(f"Can't save audio into {audio_file}. {e}")
