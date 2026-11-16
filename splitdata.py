import pandas as pd
import gzip
import os

input_file = "data/processed/airscope_cleaned.csv"

part1_file = "data/processed/airscope_part1.csv.gz"
part2_file = "data/processed/airscope_part2.csv.gz"

part1_rows = 1043572
rows_processed = 0

header1 = True
header2 = True

with gzip.open(part1_file, "wt", encoding="utf-8") as f1, \
     gzip.open(part2_file, "wt", encoding="utf-8") as f2:

    for chunk in pd.read_csv(input_file, chunksize=100000):

        split_at = max(0, min(len(chunk), part1_rows - rows_processed))

        if split_at > 0:
            chunk.iloc[:split_at].to_csv(f1, index=False, header=header1)
            header1 = False

        if split_at < len(chunk):
            chunk.iloc[split_at:].to_csv(f2, index=False, header=header2)
            header2 = False

        rows_processed += len(chunk)

print("Splitting completed!")
print("Total rows:", rows_processed)

print("Part 1:", round(os.path.getsize(part1_file) / (1024**2), 2), "MB")
print("Part 2:", round(os.path.getsize(part2_file) / (1024**2), 2), "MB")