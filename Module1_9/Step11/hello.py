#!/usr/bin/python3

def app(environ, start_response):

    data = list(map(lambda x: x + "\n", environ["QUERY_STRING"].split("&")))

    start_response("200 OK", [("Content-Type", "text/plain"),])

    return data
