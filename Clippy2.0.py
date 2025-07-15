# -*- coding: utf-8 -*-
"""
=============== Clippy2.0 ===============
A simple background tool for prompting
LLMs straight from the clipboard.
=========================================
"""

import sys

import keyboard
import pyperclip
import google.generativeai as genai


# --- Constants ---
API_KEY = "YOUR_GOOGLE_AI_API_KEY"
MODEL_NAME = "gemini-2.5-flash"

PROMPT_HOTKEY = "ctrl+alt+p"
TERMINATE_HOTKEY = 'ctrl+alt+q'


# --- Methods ---
def prompt_ai():
    """
    Gets the prompt from the clipboard, sends it to Gemini,
    and copies the response back to the clipboard.
    """
    try:
        prompt = pyperclip.paste()
        if not prompt:
            print("Clipboard is empty. Please copy some text to use as a prompt.")
        else:
            print(f"Prompting: {prompt[:10]}...")
            response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
            pyperclip.paste(response)

    except:
        print("Hmm. This did not work ...")


def shutdown():
    """
    Performs cleanup and exits the script.
    """
    print("Clippy2.0 says bye 👋")
    keyboard.unhook_all()
    sys.exit(0)


def main():
    """
    Main function to set up the API, register hotkeys, and run the script.
    """
    client = genai.Client(api_key=API_KEY)

    keyboard.add_hotkey(PROMPT_HOTKEY, prompt_ai, suppress=False)
    keyboard.add_hotkey(TERMINATE_HOTKEY, shutdown, suppress=False)

    print("Hello im Clippy2.0🧷")
    print(f"-> Press '{PROMPT_HOTKEY}' to send clipboard content as a prompt.")
    print(f"-> Press '{TERMINATE_HOTKEY}' to exit.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        shutdown()


if __name__ == "__main__":
    main()
