import pandas as pd

df = pd.read_csv('metadata.csv')  # โหลดข้อมูลทั้งหมด
eval_df = df.sample(frac=0.1, random_state=42)  # สุ่ม 10% สำหรับ validation
train_df = df.drop(eval_df.index)  # ที่เหลือคือ training

train_df.to_csv('metadata_train.csv', index=False)  # บันทึก train
eval_df.to_csv('metadata_eval.csv', index=False)    # บันทึก eval
