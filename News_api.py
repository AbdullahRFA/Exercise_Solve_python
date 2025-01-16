"""
Use the newsAPI and the requests module to fetch the daily news related to different topics.
Go to : https://newsapi.org/
and explore the various options to build your application

"""

import requests


def fetch_news(topic, api_key):
    """
    Fetch daily news articles related to a specific topic.
    Args:
        topic (str): The topic to search for news articles.
        api_key (str): Your NewsAPI key.
    """
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,  # Topic to search for
        "sortBy": "publishedAt",  # Sort by the most recent
        "apiKey": api_key,  # Your API key
        "language": "en"  # Language of the news
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        if articles:
            print(f"\nTop news about '{topic}':\n")
            for i, article in enumerate(articles[:5], start=1):  # Show top 5 articles
                print(f"{i}. {article['title']}")
                print(f"   Source: {article['source']['name']}")
                print(f"   URL: {article['url']}\n")
        else:
            print(f"No news articles found for '{topic}'.")
    else:
        print("Error fetching news:", response.status_code, response.text)


if __name__ == "__main__":
    # Replace with your actual NewsAPI key
    API_KEY = "5460119314ab448caafcce4d84bac8ee"

    print("Welcome to the News Fetcher!")
    topic = input("Enter a topic to fetch news: ").strip()

    if topic:
        fetch_news(topic, API_KEY)
    else:
        print("Topic cannot be empty!")