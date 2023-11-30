#!/bin/bash
# Send req to a URL arg passed, displays only the status code of the response.
curl -s -o /dev/null -w %{http_code} $1
