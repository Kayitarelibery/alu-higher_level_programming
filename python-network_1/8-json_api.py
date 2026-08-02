#!/usr/bin/python3
"""Sends a POST request to search_user with a letter, displays the result."""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": q})
    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
