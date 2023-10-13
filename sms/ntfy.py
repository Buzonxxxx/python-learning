import requests

requests.post("https://ntfy.sh/your_topic_channel",
              data="Hello Louis 😀".encode(encoding='utf-8'))