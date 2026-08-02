#!/usr/bin/env bash
# Displays all HTTP methods the server at the given URL will accept
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | cut -d ' ' -f2- | tr -d '\r'
