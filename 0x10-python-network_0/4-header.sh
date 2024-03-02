#!/bin/bash
# Sends a GET request to a URL with a header variable and value
curl -H "X-School-User-Id: 98" "$1"
