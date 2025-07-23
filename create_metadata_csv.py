import csv

tsv_path = 'cv-corpus-22.0-delta-2025-06-20/th/other.tsv'
csv_path = 'metadata.csv'

with open(tsv_path, encoding='utf-8') as tsvfile, \
     open(csv_path, 'w', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')
    writer = csv.writer(csvfile)
    writer.writerow(['audio_path', 'text', 'speaker_name'])
    for row in reader:
        wav_path = f"clips_wav/{row['path'].replace('.mp3', '.wav')}"
        text = row['sentence'].strip()
        speaker = row['client_id']
        writer.writerow([wav_path, text, speaker])
