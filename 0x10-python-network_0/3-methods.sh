#!/bin/bash
#Lists the HTTP methods a server accepts
curl -X OPTIONS -I "$1"
