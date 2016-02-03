import dilbert
import sys
import getopt

date = getopt.getopt(sys.argv,  "-d:")[1][1]
print "Attempting to use date[",date,"]"
dilbert.getDilbert(date)