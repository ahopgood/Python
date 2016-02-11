import dilbert
from datetime import date, timedelta, datetime
import time
import sys
import getopt

dateToContinueTo = getopt.getopt(sys.argv,  "-d:")[1][1]
print "Attempting to backfill until date [",dateToContinueTo,"]"

rollingDate = date.today()
if (len(getopt.getopt(sys.argv,  "-d:")[1]) < 2):
	dateToStartFrom = getopt.getopt(sys.argv,  "-d:")[1][2]	
	print "Starting from [",dateToStartFrom,"]"
	rollingDate = datetime.strptime(dateToStartFrom, "%Y-%m-%d").date()
else:
	print "Starting from today"
	

while str(rollingDate) > dateToContinueTo:
	dilbert.getDilbert(str(rollingDate))
	rollingDate = rollingDate - timedelta(days=1)
