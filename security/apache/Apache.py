__author__ = 'Alexander'
import urllib
def checkStaticPage(hostaddress):
    try:
        urlHandle = urllib.urlopen(hostaddress)
        # print urlHandle.info()
        # print urlHandle.getcode()
        return urlHandle.getcode()
    except:
        print "Unable to connect to ", hostaddress
        return -1
