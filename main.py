import requests 

api_key = 'c3bb154782234373853d428c8ee4fd3a'
url = "https://newsapi.org/v2/everything?q=tesla&from=2025-01-01&sortBy=publishedAt&apiKey=c3bb154782234373853d428c8ee4fd3a" 

requests = requests.get(url)
content = requests.json()
for article in content["articles"]:
    print(article["title"]) 
    print(article["description"]) 
    print("\n")
