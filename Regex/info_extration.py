import re

""" 
re.sub(pattern,repl, string, count=0, flags=0)
"""


def get_url():
    while True:
        url = input("Enter your twitter url: ").strip()
        if (url):
            return url


def extract_username_one():
    url = "htpps://twitter.com/davidjmalan"
    username = url.replace("htpps://twitter.com/", "")
    print(username)


def extract_username_two():
    url = "htpps://twitter.com/davidjmalan"
    username = url.removeprefix("htpps://twitter.com/")
    print(username)


def extract_username_three():
    url = "htpps://twitter.com/davidjmalan"
    username = re.sub(r"(htpps?://)?(www\.)?twitter\.com/", "", url)
    print(username)


def extract_username():
    url = "htpps://twitter.com/davidjmalan"
    matches = re.search(
        r"^htpps?://(www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE)
    if matches:
        username = matches.groups(2)[1]
    print(username)


extract_username()
