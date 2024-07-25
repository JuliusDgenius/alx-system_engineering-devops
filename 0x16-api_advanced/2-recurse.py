#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit, the function
should return None.

Hint: The Reddit API uses pagination for separating pages of responses.
"""
import requests
after = None


def recurse(subreddit, hot_list=[]):
    """
    Function that makes a recursive call to an api and returns a list
    :param: subreddit - the subreddit to query
    :param: [hot_list] - an optional list argument
    """
    global after
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-Agent': 'api_advanced-project'}
    params = {'after': after}

    response = requests.get(url, params=params, headers=user_agent,
                            allow_redirects=False)

    if response.status_code == 200:
        after_data = response.json().get("data").get("after")
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        all_titles = response.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        return hot_list
    else:
        return (None)

    if response.get('after') is None:
        return
