from datasets import load_dataset
import pandas as pd

ds = load_dataset("ixrbhii/india-aqi-hourly-cams")["train"]

missing = {}

for batch in ds.iter(batch_size=100000):
    for column, values in batch.items():
        missing[column] = missing.get(column, 0) + pd.isna(values).sum()

print("\nTOTAL ROWS:", len(ds))

print("\nMISSING VALUES:")
for column, count in missing.items():
    print(f"{column}: {count} ({count / len(ds) * 100:.2f}%)")

print("\nUNIQUE STATIONS:", len(ds.unique("name")))
print("\nSAMPLE STATIONS:", ds.unique("name")[:15])