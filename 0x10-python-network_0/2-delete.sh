#!/bin/bash
# send DELETE request to URL passed as 1st arg, display the body of the response
curl -sX DELETE "$1"
