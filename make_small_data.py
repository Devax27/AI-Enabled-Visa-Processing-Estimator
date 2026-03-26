import pandas as pd

# ✅ FIX: add encoding
df = pd.read_csv("data/VisaFile.csv", encoding="latin1")

# sample
df_small = df.sample(n=5000, random_state=42)

# save
df_small.to_csv("data/VisaFile_small.csv", index=False)

print("✅ Small dataset created!")