#!/usr/bin/env python


class UrlPattern(object):
    def __init__(self, url):
        self.url = url

    def __getattribute__(self, item):
        print "in __getattribute"
        return super(UrlPattern, self).__getattribute__(item)

    def __getattr__(self, item):
        if item == "get" or item == "post":
            return self.url
        return UrlPattern("{}/{}".format(self.url, item))


def main():
    pattern = UrlPattern("http://www.mucfc.com")
    url = pattern.post
    print url


if __name__ == '__main__':
    main()