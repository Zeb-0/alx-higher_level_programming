#!/bin/bash
# display all HTTP methods the server will accept using curl
curl -siX OPTIONS "$1"
