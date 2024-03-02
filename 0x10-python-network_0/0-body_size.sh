#!/bin/bash
#takes in a URL, sends a request to that URL,and displays the size of the body of the response
#curl -I -w "%{size_download}" "$1"
curl -I "$1" | wc -c | grep -o '[0-9]*'
