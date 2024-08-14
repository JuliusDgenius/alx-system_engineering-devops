#!/usr/bin/python3
"""
Module that queries the Reddit API and returns number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that returns all the subscribers of a given subreddit,
    not active users
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    result = response.json()

    if response.status_code in (301, 302, 303, 307, 308):
        return 0
    try:
        return result.get('data', {}).get('subscribers', 0)
    except (ValueError, KeyError):
        return 0
