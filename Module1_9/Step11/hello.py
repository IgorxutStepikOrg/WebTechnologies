#!/usr/bin/python3

def app(environ, start_response):

    data = ""

    for line in environ["QUERY_STRING"].split("&"):
        data = data + line + "\n"

    start_response("200 OK", [("Content-Type", "text/plain"), ("Content-Length", str(len(data)))])

    return [data]
