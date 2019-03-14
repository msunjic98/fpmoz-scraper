#!/usr/bin/python

import json

SOURCES = {}
with open('sources.json') as sources_file:
    SOURCES = json.load(sources_file)