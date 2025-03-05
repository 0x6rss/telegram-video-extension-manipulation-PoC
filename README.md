# Telegram Video Extension Manipulation PoC

This repository demonstrates a Proof of Concept (PoC) for manipulating the Telegram video (mp4) extension. The PoC shows how a malicious video file (with a `.mp4` extension) can be sent via Telegram, and it also serves as an example of how to interact with external systems via Telegram messages. This PoC uses a custom script to embed data inside the video file that can perform a network request when the file is opened.

**Blog Post:**  
[Evilloader Blog Post](https://cti.monster/blog/2025/03/04/evilloader.html)

### Overview

This PoC leverages the Telegram Bot API to send a specially crafted `.mp4` file to a Telegram chat. The file contains embedded HTML and JavaScript that, when executed (e.g., through a browser or an attacker-controlled environment), sends the IP address and geolocation data of the user to a remote server.

The **key components** of this PoC are:

- **Telegram Bot**: Used to send the video.
- **Embedded HTML/JS**: Inside the `.mp4` video, which is a potential security risk, is used to send back information about the user's IP, country, city, etc.
- **Custom Server**: A local server that receives the geolocation data sent from the manipulated `.mp4` file.

### Prerequisites

Before running this PoC, you need to configure a few things in your environment:

1. **Create a `.env` file**:
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```

2. **Edit the `.env` file**:
   - Open `.env` and update the following values:
     - `BOT_TOKEN`: Your Telegram bot token. You can get this by creating a bot on Telegram via BotFather.
     - `CHAT_ID`: The chat ID where you want to send the video. This can be a group or individual chat.
     - `IP`: The IP address or hostname of the server where you want to log the IP and geolocation data.

    ```
