#!/usr/bin/python3
"""
This module provides a function to query the Reddit API and return a
list of titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and
    returns a list of titles of all hot articles
    for a given subreddit.

    Args:
    subreddit (str): The name of the subreddit.
    hot_list (list): The list of hot article titles.
    after (str): The after parameter for pagination.

    Returns:
    list: The list of titles of all hot articles,
    or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'custom_user_agent'}
    params = {'limit': 100, 'after': after}

    try:
        response = requests.get(
                url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise HTTPError for bad responses

        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            hot_list.extend([post['data']['title'] for post in posts])
            after = data.get('after')

            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    except (requests.RequestException, ValueError):
        return None
