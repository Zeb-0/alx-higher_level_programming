#!/bin/bash
# send a request to a URL, display the size of the body of the response
curl -s "$1" | wc -c
