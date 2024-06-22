#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return the
number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number
    of subscribers for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.

    Returns:
    int: The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
