import pandas as pd
import os
from dotenv import load_dotenv
import kagglehub
from openai import OpenAI

# Load API key from .env
load_dotenv()
client = OpenAI()

# Download and load dataset
path = kagglehub.dataset_download("uciml/sms-spam-collection-dataset")
csv_file = os.path.join(path, "spam.csv")
df = pd.read_csv(csv_file, encoding='latin-1')

# Keep only useful columns
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

# Pick 2 few-shot examples
example_1 = 'Free entry in 2 a wkly comp to win FA Cup final tkts! Text FA to 87121 to receive entry code.'
label_1 = 'Spam'

example_2 = 'Hey, are we still meeting for lunch today at 1 PM? Let me know.'
label_2 = 'Not Spam'

# Pick a test message from the dataset (not used above)
test_message = df[df['label'] == 'ham'].sample(1)['message'].values[0]

# Build few-shot prompt
prompt = f"""
Classify the following message as Spam or Not Spam:

Message 1: "{example_1}"
Label: {label_1}

Message 2: "{example_2}"
Label: {label_2}

Message 3: "{test_message}"
Label:
"""

print("Prompt Sent to GPT:")
print(prompt)

# Send the prompt to OpenAI and get classification (OpenAI v1.0+ style)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

# Extract the model's classification
classification = response.choices[0].message.content.strip()

# Show results
print("\n📨 Test Message:")
print(test_message)
print("\n🤖 GPT Predicted Label:")
print(classification)
