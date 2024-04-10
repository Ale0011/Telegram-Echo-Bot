# 💬 Telegram Echo Bot

This Python script facilitates sending messages via Telegram's Bot API to a user, group, or channel, and additionally captures valuable information from the response. It's an ideal tool for automating notifications, alerts, or any kind of messages that need to be sent from various systems, servers, or personal projects. Beyond simply sending messages, this script also leverages the API's response to provide insights into the chat, making it a versatile tool for both communication and information retrieval.

## Features

- 📨 **Send messages** quickly to any Telegram chat, group, or channel.
- 📑 **Retrieve and log chat details** from the message response, providing insights into the related chat ID.
- 🛠️ **User-friendly interaction** with prompts for each required input, making it easy for anyone to use.
- 🚀 **Easy integration** into larger systems for automated alerts or notifications, with additional context from message responses for logging or auditing purposes.

## Getting Started

### Prerequisites

To use this script, you'll need:
- Python 3.x installed on your system.
- A Telegram bot token, which you can obtain by creating a bot through [BotFather](https://t.me/botfather) on Telegram.
- The chat ID of the user, group, or channel to which you want to send messages. For private chats with the bot, you can easily obtain this by initiating a conversation with your bot and visiting https://api.telegram.org/bot<YourBOTToken>/getUpdates.

### Installation

1. **Clone this repository** to your local machine using:

    ```bash
    git clone https://github.com/Ale0011/telegram-echo-bot.git
    ```

2. **Navigate** into the project directory:

    ```bash
    cd telegram-echo-bot
    ```

3. **Install required packages** (if any):

    Since this script uses the `requests` library, ensure it's installed:

    ```bash
    pip install requests
    ```

## Usage

To run the script, simply execute it with Python:

```bash
python3 TelegramMessageInsight.py
```

Follow the on-screen prompts to input:

- The **message text** you wish to send.
- Your **Telegram bot token**.
- The **chat ID** of the destination chat.

The script will then send your message and output the response from the Telegram API, confirming the message delivery.

## Contributing

Contributions to improve the script or fix issues are very welcome. Please feel free to **fork** the repository, make your changes, and submit a **pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Acknowledgements

- Thanks to the [Telegram API](https://core.telegram.org/bots/api) for making bot interactions simple and powerful.
- This project is created for educational and automation purposes. Please use it responsibly and adhere to Telegram's usage policies.

