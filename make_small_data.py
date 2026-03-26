import pandas as pd

df = pd.read_csv("data/VisaFile.csv", encoding="latin1")

df_small = df.sample(n=5000, random_state=42)

df_small.to_csv("data/VisaFile_small.csv", index=False)

print("✅ Done")