# python-network_1

## Description

This project is part of the ALU Higher-Level Programming curriculum. It covers the basics of network programming in Python: sending HTTP requests, reading response bodies and headers, handling errors, and consuming the GitHub API — first using the low-level `urllib` package, then the higher-level `requests` package.

## Learning Objectives

- How to fetch and read data from a URL in Python
- The difference between `urllib` and `requests`
- How to send a `GET` and a `POST` request
- How to read the headers of a response
- How to manage `urllib.error` / `requests` HTTP error status codes
- How to use JSON data from a response
- How to use Basic Authentication with a personal access token to query the GitHub API

## Requirements

- Ubuntu 20.04 LTS
- Python 3 (`python3` interpreter)
- Scripts must pass `pycodestyle` (version 2.x)
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- All files must be executable
- README.md at the root of the project folder is mandatory

## Files

| File | Description |
| --- | --- |
| `0-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` using `urllib` and prints the body's type, raw content, and UTF-8 decoded content |
| `1-hbtn_header.py` | Takes a URL, sends a request with `urllib`, and displays the `X-Request-Id` header value |
| `2-post_email.py` | Takes a URL and an email, sends a POST request with `urllib` (email sent as the `email` parameter), and prints the response body |
| `3-error_code.py` | Takes a URL, sends a request with `urllib`, prints the decoded body, and handles `urllib.error.HTTPError` by printing `Error code: <status>` |
| `4-hbtn_status.py` | Fetches `https://alu-intranet.hbtn.io/status` using `requests` and prints the body's type and content |
| `5-hbtn_header.py` | Takes a URL, sends a request with `requests`, and displays the `X-Request-Id` header value |
| `6-post_email.py` | Takes a URL and an email, sends a POST request with `requests` (email sent as the `email` parameter), and prints the response body |
| `7-error_code.py` | Takes a URL, sends a request with `requests`, prints the body, and prints `Error code: <status>` if the status is `>= 400` |
| `8-json_api.py` | Takes a letter, sends a POST request to `search_user` with the letter as the `q` parameter, and prints `[<id>] <name>` from the JSON response (or `No result` / `Not a valid JSON`) |
| `10-my_github.py` | Takes a GitHub username and personal access token, uses Basic Authentication against the GitHub API, and prints the user's id |

## Usage

Each script is executable and takes its arguments from the command line, for example:

```bash
./0-hbtn_status.py
./1-hbtn_header.py https://alu-intranet.hbtn.io
./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./3-error_code.py http://0.0.0.0:5000/status_401
./4-hbtn_status.py
./5-hbtn_header.py https://alu-intranet.hbtn.io
./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
./7-error_code.py http://0.0.0.0:5000/status_401
./8-json_api.py a
./10-my_github.py <username> <personal_access_token>
```

## Author

Libery
