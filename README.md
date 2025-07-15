# Clippy2.0🧷
[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Your favourite AI is just a hotkey away. This lightweight Python script allows prompting LLMs straight from the clipboard.
---

## 🤔 Why AI Clipboard Helper?
In a world of constant context switching, this tool is designed to streamline your workflow. Stop wasting time switching between your editor, a browser, and back again.
* **Developers**: Refactor code, write docstrings, or explain complex functions instantly.
* **Writers & Marketers**: Rephrase sentences, correct grammar, or generate content ideas on the fly.
* **Students**: Summarize articles, explain concepts, or translate text for your studies.
This tool puts the power of a large language model right at your fingertips, saving you time and keeping you focused.

---
## 🛠️ Installation & Setup
Follow these steps to get the AI Clipboard Helper up and running on your machine.

### Prerequisites
* **Python 3.7+**
* **pip** (Python's package installer)
* A **Google AI API Key**. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### Step 1: Clone the Repository 💾
First, clone this project to your local machine using Git.
```bash
git clone [https://github.com/alphaname007/Clippy2.0.git](https://github.com/alphaname007/Clippy2.0.git)
cd ai-clipboard-helper
````

### Step 2: Install Dependencies 📚
This project uses a few external libraries. Install them easily using the requirements.txt file.
```bash
pip install -r requirements.txt
````

### Step 3: Set Up Your API Key 🔑
Replace `GOOGLE_AI_API_KEY` with your Google AI API key.

---
## 🐍 Run Clippy2.0
```bash
python Clippy2.0.py
````
You'll see a confirmation message that the script is running, and it will continue to run in the background.

---
## 🔀 The Workflow
* 📋 Copy: Highlight and copy any text to your clipboard `Ctrl+C`. This text is your prompt.
* ⚡️ Activate: Press the hotkey `Ctrl+Alt+P`. The script will print a "Processing..." message in the terminal.
* ✨ Paste: In a few seconds, the AI's response will be automatically copied to your clipboard. Just paste it (Ctrl+V) wherever you need it!

---
## 🛑 Stop the Script
To stop the script, you can either:
* Press the termination hotkey: `Ctrl+Alt+Q`.
* Go to the terminal where it's running and press `Ctrl+C`.

---
## 👥 Contribute
Contributions are welcome! Whether it's reporting a bug, suggesting a feature, or submitting a pull request, your help is appreciated.


---
## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.
