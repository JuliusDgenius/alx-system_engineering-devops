#!/usr/bin/python3
"""
Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Function that returns the titles of the first 10 top hot
    posts for a given subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {"User-agent": 'Google Chrome Version 81.0.4044.129'}
    response = requests.get(url, headers=user_agent)

    try:
        res = response.json().get('data').get('children')
        for i in range(1, 11):
            print(res[i].get('data')['title'])
    except Exception:
        print(None)
