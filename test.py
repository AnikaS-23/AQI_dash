
from modules.data_loader import load_processed_data

# Load the sample dataset
df = load_processed_data(use_sample=True)

print("\nFirst 5 records:")
print(df.head())

print("\nDataset columns:")
print(df.columns.tolist())
