#!/usr/bin/python3
"""
This module provides a recursive
function to query the Reddit API, parse the title
of all hot articles, and print a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, counts=None, after=None):
    """
    Queries the Reddit API, parses the title of all
    hot articles, and counts given keywords.

    Args:
    subreddit (str): The name of the subreddit.
    word_list (list): A list of keywords to count.
    counts (dict): A dictionary to store the count of each keyword.
    after (str): The after parameter for pagination.

    Returns:
    None
    """
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

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
            for post in posts:
                title = post['data']['title'].lower().split()
                for word in word_list:
                    counts[word.lower()] += title.count(word.lower())

            after = data.get('after')
            if after:
                return count_words(
                        subreddit, word_list, counts, after)
            else:
                sorted_counts = sorted(
                        [(word, count) for word, count in counts.items()
                            if count > 0], key=lambda x: (-x[1], x[0]))
                for word, count in sorted_counts:
                    print(f"{word}: {count}")
        else:
            return None
    except (requests.RequestException, ValueError):
        return None
