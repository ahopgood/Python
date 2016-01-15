import urllib
from BeautifulSoup import *
import time
from datetime import date
import re


def getDilbert(dateInput):
	pictureDate = str(date.today())
	if (dateInput != None and len(dateInput) > 1 and re.search('[0-9]{4}-[0-9]|[1][0-2]-[0-9]{2}',dateInput)):
		pictureDate = dateInput
	print "using date ",pictureDate

	urlHandle = urllib.urlopen('http://dilbert.com/strip/'+pictureDate)

	for line in urlHandle:
		soup = BeautifulSoup(line)
		tags = soup.findAll("img", "img-comic")
		#print line.split()
		for tag in tags:
			url = tag.get('src', None)
			try:
				urllib.urlretrieve(url, pictureDate+".jpg")
			except:
				print url, "could not be located"
			print url
	return 
	
def run():
	dateInput = raw_input("Please provide a date for a dilbert cartoon [yyyy-mm-dd]:")
	getDilbert(dateInput)