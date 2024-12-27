from flask import Flask, request, render_template, jsonify
import re
import pandas as pd
from transformers import pipeline, T5ForConditionalGeneration, T5Tokenizer

app = Flask(__name__)

# Load the T5 model and tokenizer once during app startup
model = T5ForConditionalGeneration.from_pretrained("t5-small")
tokenizer = T5Tokenizer.from_pretrained("t5-small")

# Helper function: Parse chat
def parse_chat(file):
    pattern = r"(\d{1,2}/\d{1,2}/\d{2,4}, \d{1,2}:\d{2} (?:AM|PM)) - ([^:]+): (.+)"
    messages = []
    # Decode byte file content to string
    file_content = file.read().decode('utf-8')  # Decode bytes to string
    for line in file_content.splitlines():
        match = re.match(pattern, line)
        if match:
            timestamp, sender, message = match.groups()
            messages.append([timestamp, sender, message])
    return pd.DataFrame(messages, columns=["Timestamp", "Sender", "Message"])

# Helper function: Clean message dynamically based on the speaker's name
def clean_message(message, speaker_name, receiver_name):
    # Remove URLs and special characters
    message = re.sub(r"http\S+|www\S+|https\S+", '', message)
    # Remove non-alphanumeric characters except spaces
    message = re.sub(r"[^\w\s,.\-!]", '', message)
    # Convert to lowercase
    message = message.lower()

    # Replace first-person pronouns with speaker's name
    message = message.replace('i ', f'{speaker_name} ').replace('i\'m ', f'{speaker_name} is ').replace('i\'ve ', f'{speaker_name} has ')
    message = message.replace('my ', f'{speaker_name}\'s ').replace('myself', speaker_name)
    
    # Replace second-person pronouns ("you") with receiver's name
    message = message.replace('you ', f'{receiver_name} ').replace('you\'re ', f'{receiver_name} is ').replace('you\'ve ', f'{receiver_name} has ')
    message = message.replace('your ', f'{receiver_name}\'s ').replace('yourself', receiver_name)

    return message

# Helper function: Extractive summary (using transformers)
def summarize_chat(messages, ratio=0.1):
    # Join all cleaned messages into a single string
    text = ' '.join(messages)

    # Debug log to display the cleaned messages
    print(f"Summarizing the following text for extractive summary:\n{text[:500]}...")

    # Summarizer pipeline
    summarizer = pipeline("summarization")

    try:
        # Adjust max_length, min_length, and other parameters for better results
        summary = summarizer(
            text,
            max_length=200,  # Limit the output length for a more concise summary
            min_length=50,   # Ensure there's enough content in the summary
            do_sample=False
        )
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during extractive summarization: {e}")
        return "Error generating extractive summary."

# Helper function: Abstractive summary using T5 (transformers)
def abstractive_summary(messages, max_length=100):
    text = ' '.join(messages)
    print(f"Summarizing the following text for abstractive summary:\n{text[:500]}...")  # Debug log

    try:
        # Tokenize the input text properly
        input_ids = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)

        # Generate the summary
        summary_ids = model.generate(input_ids, max_length=max_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)

        # Decode the generated summary
        return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    except Exception as e:
        print(f"Error during abstractive summarization: {e}")
        return "Error generating abstractive summary."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    try:
        chat_df = parse_chat(file)
    except Exception as e:
        return jsonify({"error": f"Error parsing file: {str(e)}"}), 500

    # Process messages: clean and replace pronouns dynamically
    chat_df['Cleaned_Message'] = chat_df.apply(
        lambda row: clean_message(
            row['Message'],
            row['Sender'],
            chat_df['Sender'][chat_df.index.get_loc(row.name) + 1] if row.name < len(chat_df) - 1 else row['Sender']
        ), axis=1
    )
    messages = chat_df['Cleaned_Message'].tolist()

    # Debug log: print cleaned messages
    print(f"Cleaned Messages: {messages[:5]}")  # Show the first 5 cleaned messages

    # Generate summaries
    try:
        extractive = summarize_chat(messages, ratio=0.1)
        abstractive = abstractive_summary(messages)
    except Exception as e:
        return jsonify({"error": f"Error generating summaries: {str(e)}"}), 500

    return jsonify({
        "extractive": extractive,
        "abstractive": abstractive
    })

if __name__ == '__main__':
    app.run(debug=True)
