__author__ = 'Alexander Hopgood'

from apache import checkStaticPage

class test_Penetration_Home():


#Scaffolding class for testing liveness of a domain with multiple sub domains
    def domain(self, domain, subdomains):
        resultDict = dict()
        outputStr = "Checks for domain ["+domain+"]:"
        for name,subdomain in subdomains.items():
            # print "name "+name+" subdomain"+subdomain
            result = checkStaticPage("http://"+subdomain+domain)
            # print result
            outputStr = outputStr+" "+name+" "+str(result)
            resultDict.setdefault("http://"+subdomain+domain, result)
        # print outputStr
        return resultDict

    def combineDictionaries(self, dict1, dict2):
        # for key, value in dict2.items():
        dict = {}
        dict.update(dict1)
        dict.update(dict2)
        return dict

if __name__ == '__main__':
    test = test_Penetration_Home()
    baseSubDomains = {"root":"", "www":"www."}
    subdomains = test.combineDictionaries(baseSubDomains, {"cv":"cv.", "blog":"blog.", "kanboard":"kanboard." })

    print test.domain("alexanderhopgood.com", subdomains)
    print test.domain("alexhopgood.co.uk", subdomains)
    print test.domain("alexanderhopgood.net", subdomains)

    print test.domain("altairbob.com", test.combineDictionaries(baseSubDomains, {}))
    print test.domain("altairbob.co.uk", test.combineDictionaries(baseSubDomains, {}))
    print test.domain("altairbob.net", test.combineDictionaries(baseSubDomains, {}))

    print test.domain("katherinemorley.co.uk", test.combineDictionaries(baseSubDomains,{"blog":"blog."}) )
    #@,www,blog
    print test.domain("katherinemorley.net", test.combineDictionaries(baseSubDomains,{"blog":"blog."}) )
    #blog,www, @

    print test.domain("katherinemorley.net", test.combineDictionaries(baseSubDomains,{"blog":"blog."}) )

    #Static resouces on Apache web pages are accessible, I'm not sure if this is a good thing (tm)
    print "cv.alexanderhopgood.com/CvResources/"+" "+str(checkStaticPage("http://cv.alexanderhopgood.com/CvResources/"))
    print "cv.alexanderhopgood.com/CvResources/isca-logo.png"+" "+str(checkStaticPage("http://cv.alexanderhopgood.com/CvResources/isca-logo.png"))