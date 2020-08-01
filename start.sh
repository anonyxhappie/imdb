#!/bin/bash

# Rename settings.ini.example (update values in settings.ini)
mv settings.ini.example settings.ini

# Create local directory to mount with container
mkdir -p /tmp/imdbfiles

# Create docker image
docker build -t imdbapp:v1 .

# Run imdb api server
docker run -v /tmp/imdbfiles:/tmp/imdbfiles -it -p 8000:8000 imdbapp:v1