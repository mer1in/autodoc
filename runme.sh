#!/bin/bash

echo "Setup env"

[ -d venv ] || (
    python3 -m venv ./venv
    . ./venv/bin/activate
    pip3 install -r requirements.txt
)

echo "Start the server"
. ./venv/bin/activate
python3 main.py &
sleep 1

echo "Run with requests"
echo "pass, admin can do everything"
curl -s -b "role=admin" http://localhost:8080/some/qq | jq -c
echo "pass, valid user"
curl -s -b "role=user" http://localhost:8080/some/qq | jq -c
echo "fails, method not allowed"
curl -s -X POST -b "role=viewer" http://localhost:8080/some/err | jq -c
echo "fails, forbidden for user viewer"
curl -s -b "role=viewer" http://localhost:8080/some/qq | jq -c
echo "fails, anonymous is not allowed"
curl -s http://localhost:8080/some/qq | jq -c
echo "pass, allow get for viewer"
curl -s -b "role=viewer" http://localhost:8080/other/abc | jq -c
echo "fails, viewer cannot post "
curl -s -X POST -b "role=viewer" http://localhost:8080/other/bcd | jq -c
echo "pass, admin allowed even if not listed"
curl -s -X POST -b "role=admin" http://localhost:8080/other/cde | jq -c
echo "pass, anonymous matches every role"
curl -s -b "role=viewer" http://localhost:8080/help | jq

echo "Stop the server"
PID=`netstat -tulnep | grep 8080 | awk '{print($NF)}' | sed 's#/python3##'`
[ -z $PID ] || kill -HUP $PID
