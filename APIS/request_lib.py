import requests  # pip install requests
import sys
import json


def itunes_songs():
    url = "https://itunes.apple.com/search?entity=song&limit=50&term=weezer"
    try:
        response = requests.get(url)
        result = response.json()
        for item in result["results"]:
            # First 50 songs by weezer
            print(item["trackName"])
    except:
        print("Something went wrong with the server call")


itunes_songs()


def itunes_songs_two():
    url = "https://itunes.apple.com/search?entity=song&limit=10&term=weezer"
    try:
        response = requests.get(url)
        result = response.json()
        formatted_json_result = json.dumps(result, indent=2)
        print(formatted_json_result)
    except:
        print("Something went wrong with the server call")


itunes_songs_two()


def itunes_songs_three():
    if (len(sys.argv) != 2):
        sys.exit()
    url = f"https://itunes.apple.com/search?entity=song&limit=1&term={sys.argv[1]}"
    try:
        response = requests.get(url)
        print(type(response.json()))
        print(response.json())
    except:
        print("Something went wrong with the server call")
