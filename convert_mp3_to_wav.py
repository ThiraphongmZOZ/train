import os
from pydub import AudioSegment

ffmpeg_path = os.path.abspath(r"C:/project/train/ffmpeg/bin")
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]


mp3_dir = 'cv-corpus-22.0-delta-2025-06-20/th/clips'
wav_dir = 'clips_wav'
os.makedirs(wav_dir, exist_ok=True)

for file in os.listdir(mp3_dir):
    if file.endswith('.mp3'):
        mp3_path = os.path.join(mp3_dir, file)
        wav_path = os.path.join(wav_dir, file.replace('.mp3', '.wav'))
        sound = AudioSegment.from_mp3(mp3_path)
        sound = sound.set_channels(1).set_frame_rate(16000)
        sound.export(wav_path, format='wav')
        print(f'Converted: {file}')
