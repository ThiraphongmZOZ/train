import pandas as pd

# โหลดไฟล์ metadata_train.csv เดิม (comma)
df = pd.read_csv('metadata.csv')

# เปลี่ยนชื่อคอลัมน์ audio_path → audio_file
df.rename(columns={'audio_path': 'audio_file'}, inplace=True)

# เปลี่ยน path clips_wav/xxx.wav → wavs/xxx.wav
df['audio_file'] = df['audio_file'].apply(lambda x: x.replace('clips_wav/', 'wavs/'))

# save ด้วย | (pipe)
df.to_csv('metadata_.csv', sep='|', index=False)
