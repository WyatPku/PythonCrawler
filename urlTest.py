# coding=utf-8
# using python 2.7

import urllib2
from PkuLogin import pku_login


def main():
    try:
        outfile = open('test.html', 'w')
        """
        request = urllib2.Request("http://wuyue98.cn/owncloud")
        response = urllib2.urlopen(request)
        page = response.read()
        """
        page = pku_login()
        print >>outfile, page
        outfile.flush()
        outfile.close()
    except IOError:
        print("File Error")


# 用来打印
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
main()
