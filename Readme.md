python -m venv .venv
..venv\Scripts\activate

pip install pydub
pip install pandas
pip install tokenizers

mkdir clips_wav
python convert_mp3_to_wav.py python create_metadata_csv.py python split_train_eval.py

git clone https://github.com/nguyenhoanganh2002/XTTSv2-Finetuning-for-New-Languages.git cd XTTSv2-Finetuning-for-New-Languages pip install -r requirements.txt

pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

XTTSv2-Finetuning-for-New-Languages/ ├── datasets-th/ │ ├── wavs/ │ │ ├── xxx.wav │ │ └── yyy.wav │ ├── metadata_train.csv │ ├── metadata_eval.csv

โหลดโมเดล XTTS Pretrained python download_checkpoint.py --output_path checkpoints/

python extend_vocab_config.py --output_path=checkpoints/ --metadata_path=..\metadata_train.csv --language th --extended_vocab_size 2000

python-new_csv.py

edit json1 = json.load(open(os.path.join(old_tokenizer, 'vocab.json'))) to json1 = json.load(open(os.path.join(old_tokenizer, 'vocab.json'), encoding='utf-8'))

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

pip install coqpit pip install numpy pandas

python train_gpt_xtts.py --output_path=checkpoints/ --metadatas ../metadata.csv,../metadata_eval.csv,th --num_epochs=5 --batch_size=4 --grad_acumm=2 --max_text_length=250 --max_audio_length=255995 --weight_decay=1e-2 --lr=5e-6 --save_step=2000

pip install torch==2.5.1 torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121







python train_dvae_xtts.py `                            
>>   --output_path checkpoints/ `
>>   --train_csv_path ../metadata.csv `
>>   --eval_csv_path ../metadata_eval.csv `
>>   --language th `
>>   --num_epochs 5 `
>>   --batch_size 64 `
>>   --lr 1e-4

python train_gpt_xtts.py ` 
>>    --output_path checkpoints/ ` 
>>    --metadatas ../metadata.csv,../metadata_eval.csv,th ` 
>>    --num_epochs 5 ` 
>>    --batch_size 2 ` 
>>    --grad_acumm 4 ` 
>>    --max_text_length 250 ` 
>>    --max_audio_length 255995 ` 
>>    --weight_decay 1e-2 ` 
>>    --lr 1e-5 ` 
>>    --save_step 2000


python train_gpt_xtts.py --output_path checkpoints/ --metadatas ../metadata.csv,../metadata_eval.csv,th --num_epochs 5 --batch_size 2 --grad_acumm 4 --max_text_length 250 --max_audio_length 255995 --weight_decay 1e-2 --lr 1e-5 --save_step 2000



python train_gpt_xtts.py `
  --output_path checkpoints/ `
  --metadatas ../metadata.csv,../metadata_eval.csv,th `
  --num_epochs 5 `
  --batch_size 2 `
  --grad_acumm 4 `
  --max_text_length 250 `
  --max_audio_length 255995 `
  --weight_decay 1e-2 `
  --lr 1e-5 `
  --save_step 2000
