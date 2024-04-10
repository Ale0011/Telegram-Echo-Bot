#!/usr/bin/python

import requests
import sys

def display_banner():
    banner = """
    ##############################################
    #            TelegramMessageInsight          #
    ##############################################
    """
    print(banner)

# Display the banner when the script is executed
display_banner()

# Function to prompt the user for input with an example
def prompt_with_example(prompt, example):
    user_input = input(f"{prompt} (example: {example}): ")
    return user_input

# Ask for user input instead of command line arguments
print("Please enter the required information below:")
text = prompt_with_example("Text to send in the message", "Hello, world!")
token = prompt_with_example("Telegram bot token", "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11")
chat_id = prompt_with_example("Telegram chat ID", "@my_channel_or_chat_id")

# Check if required inputs are provided
if not token or not chat_id:
    print("Error: Telegram bot token and chat ID are required.")
    sys.exit()

# Create URL for API request
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}"

# Send API request and print response
r = requests.get(url)
print(r.json())
