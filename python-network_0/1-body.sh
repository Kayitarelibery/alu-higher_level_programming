#!/usr/bin/env bash
# Sends a GET request to a URL and displays the body of the response
# only if the response status code is 200
response=$(curl -s -w "\n%{http_code}" "$1")
status_code=$(echo "$response" | tail -n1)
body=$(echo "$response" | sed '$d')

if [ "$status_code" -eq 200 ]; then
	echo "$body"
fi
