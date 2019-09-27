# Return formatted date of 3 days from now(no arguments)

from datetime import date,timedelta



def formatDate3Days():
    todaysDate=date.today()
    laterdate=todaysDate+timedelta(days=3)
    return laterdate


thedate=formatDate3Days()
print(thedate)
