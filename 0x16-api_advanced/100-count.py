#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count
of given keywords (case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not).
"""
import requests
recurse = __import__('2-recurse').recurse


def count_words(subreddit, word_list, after="", count=[]):
    """
    Function that returns the count of given keywords
    :param: subreddit - the subreddit to query.
    :param: word_list - list of words
    :param: after - the next page
    :param: count - the count for each given word
    """
    if after == "":
        count = [0] * len(word_list)

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': 'api_advanced-project'}
    param = {'after': after}

    r = requests.get(url,
                     params=param,
                     headers=user_agent,
                     allow_redirects=False)
    if r.status_code == 200:
        data = r.json()

    for hotpost in data.get('data').get('children'):
        for word in hotpost.get('data').get('title').split():
            for i in range(len(word_list)):
                if (word_list[i]).lower() == word.lower():
                    count[i] += 1

    after = data.get('data').get('after')
    if after is None:
        save = []
        for i in range(len(word_list)):
            for j in range(i + 1, len(word_list)):
                if word_list[i].lower() == word_list[j].lower():
                    save.append(j)
                    count[i] += count[j]

        for i in range(len(word_list)):
            for j in range(i, len(word_list)):
                if (count[j] > count[i] or (word_list[i] > word_list[j] and
                                            count[j] == count[i])):
                    aux = count[i]
                    count[i] = count[j]
                    count[j] = aux
                    aux = word_list[i]
                    word_list[i] = word_list[j]
                    word_list[j] = aux

            for i in range(len(word_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(word_list[i].lower(), count[i]))
    else:
        count_words(subreddit, word_list, after, count)
