import sys
import urllib.request
from time import sleep
import Adafruit_DHT as dht

def DHT22_data():
	# Reading from DHT22 and storing the temperature and humidity
	humi, temp = dht.read_retry(dht.DHT22, 4) 
	return humi, temp
while True:
	try:
		humi, temp = DHT22_data()
		# If Reading is valid
		if isinstance(humi, float) and isinstance(temp, float):
			# Formatting to two decimal places
			humi = '%.2f' % humi 					   
			temp = '%.2f' % temp
			print(humi)
			print(temp)


			f=urllib.request.urlopen("https://api.thingspeak.com/update?key=GXIZD2XSS09EQ38K&field1="+str(temp)+"&field2="+str(humi))
			print(f)
			
                        
		else:
			print (Error)
		# DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
		sleep(20)
	except:
		break


