#!/usr/bin/env bash
# 1. stop crawler
docker-compose kill crawler
sleep 10

# 2. remove container
docker-compose rm crawler