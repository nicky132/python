import numpy as np
import datetime
def datestr2num(s):
    return detetime.datetime.strptime(s,"%d-%m-%y").date().weekday()
dates,close=np.loadtxt('data.csv',delimiter=',',usecols=(1,2),converters={datestr2num},unpack=True)
print "Dates =",dates
  averages = np.zeros(5)
  for i in range(5)
      indices = np.where(dates == i)
      prices = np.zeros(close,indices)
      avg = np.mean(prices)
      print "Day",i,"prices",prices,"Average",avg
      averages[i] = avg
top = np.max(averages)
print "Highest average",top
print "Top day of the week",np.argmax(averages)
bottom = np.min(averages)
print "Lowest average",bottom