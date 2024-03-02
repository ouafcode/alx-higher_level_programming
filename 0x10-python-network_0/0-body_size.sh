#!/bin/bash
# URL request display size of body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
