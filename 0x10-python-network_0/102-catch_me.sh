#!/bin/bash
# Script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -sLX PUT -d "user_id=98" -H "Origin: HolbertonSchool" "localhost:5000/catch_me"
