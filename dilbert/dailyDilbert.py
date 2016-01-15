import dilbert
import schedule
import time

def job():
    dilbert.getDilbert(None)
    print("I'm working...")

schedule.every().day.at("09:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
	
#requires schedule and beautifulsoup modules
#pip install schedule
#pip install bs3

	
#schedule.every().day.at("09:00").do(dilbert.getDilbert(None))
