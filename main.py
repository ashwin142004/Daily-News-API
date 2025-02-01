import requests 
from send_email import send_email

topic = "tesla"

api_key = 'c3bb154782234373853d428c8ee4fd3a'
url = "https://newsapi.org/v2/everything?" \
    f"q={topic}&" \
    "sortBy=publishedAt&" \
    "apiKey=c3bb154782234373853d428c8ee4fd3a&" \
    "language=en" 

requests = requests.get(url)
content = requests.json()

body = "Subject: Today's News\n\n"
for article in content["articles"][:20]:
    if article["title"] is not None:
        body += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

body = body.encode("utf-8")
send_email(message=body)
