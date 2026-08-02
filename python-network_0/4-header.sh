#!/usr/bin/env bash
# Sends a GET request to a URL with the header X-HolbertonSchool-User-Id: 98
# and displays the body of the response
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
