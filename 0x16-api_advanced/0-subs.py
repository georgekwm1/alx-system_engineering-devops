#!/usr/bin/python3
"""
A Script that queries the Reddit API and returns the number of subscribers
 (not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """ Returns the total number of subscribers """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    user_agent = {"User-Agent": 'Python:script:subscribers:v1.0\
                    (by georgekwm1)'}
    response = requests.get(url, headers=user_agent,
                            allow_redirects=False, timeout=60)
    try:
        data = response.json()['data']['subscribers']
        return (data)

    except Exception:
        return (0)
