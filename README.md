# WhatsApp Chat Analyzer

A tool for analyzing and summarizing WhatsApp chat data. The project processes exported WhatsApp chat files, extracts meaningful information, and provides summaries, statistics, and insights.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setting Up the Environment](#setting-up-the-environment)
  - [Installing Dependencies](#installing-dependencies)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Analyzing WhatsApp Chats](#analyzing-whatsapp-chats)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **WhatsApp Chat Analyzer** is designed to analyze WhatsApp chat exports to help users gain insights into their conversations. It can summarize chat histories, extract key statistics like message counts, word frequencies, and more, providing useful analytics for large conversations.

This project is built with Python, and uses libraries such as **pandas** for data manipulation and **matplotlib** for visualizations.

## Features

- **Chat Summaries**: Generate concise summaries of WhatsApp chat histories.
- **Message Analysis**: Count messages sent by each participant, calculate average message length, and identify active users.
- **Word Frequency Analysis**: Find the most common words used in the chat.
- **Visualizations**: Create visual graphs of chat data, such as message counts per user or word cloud.

## Installation

### Prerequisites

Before installing the WhatsApp Chat Analyzer, make sure you have Python 3.7+ installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

### Setting Up the Environment

You can set up a Python virtual environment to keep your project dependencies isolated. To do this:

1. **Create a virtual environment**:
   ```bash
   python -m venv env
   ```
2. **Activate the virtual environment**:

   On Windows:
   ```bash
   .\env\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source env/bin/activate
   ```

   Once activated, your command prompt will show the name of the environment (e.g., (env)) to indicate that the virtual environment is active.

### Installing Dependencies

After activating the virtual environment, you need to install the required dependencies for the project. If the project includes a `requirements.txt` file, you can easily install all the necessary packages by running:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file doesn't exist, you can manually install dependencies like pandas, matplotlib, and others using:

```bash
pip install pandas matplotlib
```

## Usage

### Running the Application

To use the WhatsApp Chat Analyzer, follow these steps:

1. **Prepare the WhatsApp Chat Export**:
   - Export the chat from WhatsApp by following these steps:
     - Go to a WhatsApp chat.
     - Tap on More options > Export chat.
     - Choose to export with or without media.
   - Place the exported chat file (usually a .txt file) in the designated folder (e.g., `data/`).

2. **Run the application by executing the main Python script**. If the script is named `app.py`, use the following command:
   ```bash
   python app.py
   ```

   The script will process the chat data and generate summaries, statistics, or visualizations based on the functionality you've implemented.

### Analyzing WhatsApp Chats

Once the application is set up and running, you can analyze your WhatsApp chats by following these steps:

1. **Export the chat from WhatsApp**:
   - Go to a WhatsApp chat.
   - Tap on More options > Export chat.
   - Choose to export with or without media.
   - Upload the exported .txt file into the application folder (e.g., `data/`).

2. **Run the script to analyze the chat data**.

   The script will process the chat file, generating statistics like message counts, word frequencies, and participant details, along with visualizations like graphs or word clouds.

## Contributing

If you want to contribute to the development of the WhatsApp Chat Analyzer, follow the steps below:

1. **Fork this repository** by clicking the "Fork" button on the GitHub page.
2. **Clone the forked repository to your local machine**:
   ```bash
   git clone https://github.com/your-username/whatsapp-chat-summarizer.git
   ```
3. **Create a new branch to make your changes**:
   ```bash
   git checkout -b your-feature-branch
   ```
4. **Make your changes and commit them with a descriptive message**:
   ```bash
   git commit -m "Describe your changes"
   ```
5. **Push your changes to your forked repository**:
   ```bash
   git push origin your-feature-branch
   ```
6. **Create a pull request to the original repository**, where your changes can be reviewed.

By following these steps, you can contribute to the development of the WhatsApp Chat Analyzer project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
