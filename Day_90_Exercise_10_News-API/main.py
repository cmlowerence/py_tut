import requests
from os import system
import os

def say(txt):
    print(txt)
    system(f'say "{txt}"')

def get_api_key():
    with open(".credentials", 'r') as f:
        return f.readline().strip()

def fetch_news(api_key, topic):
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': topic,
        'apiKey': api_key,
        'language': 'en',
    }
    response = requests.get(url, params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])

        if not articles:
            print(f"No articles found for '{topic}'.")
            return

        for article in articles:
            author = article['author']
            title = article['title']
            description = article['description']
            publishedAt = article['publishedAt']

            say(f"News from {author} dated on {publishedAt.split('T')[0]} ")
            say(title)
            print("\nNews in detail:")
            say(description)
            usr_res = input("Press Enter to continue or type 'exit' to stop: ")
            if usr_res.lower() == 'exit':
                return

    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    apiKey = get_api_key()

    print(" Welcome to News Buddy ".center(50, '='))
    system(f"say Welcome to News Buddy: ")

    say("Enter the topic on which you want to see the news...")
    
    while True:
        topic = input("News based on: ")
        if topic.lower() == 'exit':
            break
        if topic:
            fetch_news(apiKey, topic)
