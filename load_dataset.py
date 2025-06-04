import kagglehub
import pandas as pd
import os

# Step 1: Download dataset from KaggleHub
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")

print("Path to dataset files:", path)

# Step 2: Locate the correct CSV file (usually named 'spam.csv')
csv_file = os.path.join(path, "spam.csv")

# Step 3: Load into pandas
df = pd.read_csv(csv_file, encoding='latin-1')

# Step 4: Display sample data
print("\nSample Data:")
print(df.head())

# Step 5: Show dataset shape and label distribution
print("\nDataset shape:", df.shape)
print("Label counts:")
print(df['v1'].value_counts())  # 'v1' is the label column (spam or ham)
