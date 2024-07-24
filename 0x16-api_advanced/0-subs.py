#!/usr/bin/python3
"""
Function that queries the Reddit API and returns number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that returns all the subscribers of a given subreddit,
    not active users
    """

    user_agent = {"User-agent": 'Google Chrome Version 81.0.4044.129'}

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=user_agent)
    data = response.json()
    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0
