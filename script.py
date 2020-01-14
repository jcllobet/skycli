from subprocess import call
import itertools
import time


origin_cities = ["BCN", "LOND", "MILA", "FRAN", "COPE", "PARI", "LIS", "ZRH"]
destin_cities = ["BCN", "LOND", "MILA", "FRAN", "COPE", "PARI", "LIS", "ZRH"]

trips = list(itertools.permutations(origin_cities, 2))

outbound_dates = ["2020-01-21", "2020-01-22", "2020-01-23", "2020-01-24", "2020-01-25"]
inbound_dates  = ["2020-01-23", "2020-01-24", "2020-01-25", "2020-01-26", "2020-01-27"]

class CallPy(object):

	def __init__(self,path='/home/jan/Code/skycli/skycli.py'):
		self.path = path

	def call_python_file(self, origin_city, destin_city, inbound_date, outbound_date, file):
		#">>", "./outputs/{}_{}_{}_{}.json".format(origin_city, destin_city, outbound_date, inbound_date)]
		call(["python3", "{}".format(self.path), "routes", origin_city, destin_city, outbound_date, inbound_date], stdout=file)

if __name__ == "__main__":
	c = CallPy()
	for trip in trips: 
		for i in range(len(outbound_dates)):
			print("Executing Trip from {} to {} leaving on {} and returning on {}".format(trip[0],trip[1], outbound_dates[i], inbound_dates[i]))
			#try:
			f = open("./outputs/{}_{}_{}_{}.json".format(trip[0],trip[1], outbound_dates[i], inbound_dates[i]), "w")
			c.call_python_file(origin_city=trip[0], destin_city=trip[1], outbound_date=outbound_dates[i], inbound_date=inbound_dates[i], file=f) 
			time.sleep(5)
			f.close()
			
			#except:
			#	print("Too many API Requests when executing Trip from Origin:{} to Destination:{} leaving on Outbound:{} and returning on 	time.sleep(15){}".format(trip[0],trip[1], outbound_dates[i], inbound_dates[i])) >> "./outputs/errors.txt"
			#	time.sleep(15)