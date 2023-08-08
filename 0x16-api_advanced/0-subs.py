#!usr/bin/python3
"""
module to count number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    user_agent = "MyRedditClient/1.0"

    """
    URL of the Reddit API endpoint for the subreddit's about page
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {
        "User-Agent": user_agent
    }

    try:
        response = requests.get(url, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        elif response.status_code == 404:
            return 0  # Subreddit not found
        else:
            print(f"Error: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Error: {e}")
        return 0
