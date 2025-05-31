FROM python:3.9-slim

# add apache bench (ab) tool


WORKDIR /seed

COPY . .

# create POST data files with ab friendly formats
RUN python ./higher.py


