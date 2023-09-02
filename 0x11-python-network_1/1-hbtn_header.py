#!/usr/bin/python3
"""
accepts a url and gets the x request ide response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    req = request.Request(argv[1])
    with request.urlopen(req) as r:
    print(r.headers.get('X-Request-Id'))
