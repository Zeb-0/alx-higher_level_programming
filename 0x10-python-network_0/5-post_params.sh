#!/bin/bash
# send POST request to the passed URL curl, display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
