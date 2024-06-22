#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and print the
titles of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom_user_agent'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            try:
                data = response.json()
                posts = data.get('data',{}).get('children',[])
                if not posts:
                    print("None")
                    return
                for post in posts:
                    print(post['data']['title'])
            except ValueError:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
