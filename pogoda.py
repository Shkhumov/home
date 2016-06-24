import urllib
import urllib2
import pickle
#import schedule
import time
import json
from pprint import pprint
import yaml


sity = "Lviv"

def main():
	response = urllib2.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ sity +"&appid=f69f7dd713845517316a0aa6896c3840&units=metric")
	text = response.read()

	weather = yaml.load(text)
	#pprint(weather)
	spase = ("The weather for", weather['name'])
	tempr = (weather['main']['temp'])
	coco = (weather['weather'][0]['description'])


	#with open('pogoda', 'wb+') as f:
	#	f.writelines(str(weather['main']['temp']))
	#	f.writelines(str(weather['weather'][0]['description']))
	#	f.writelines(str( weather['name']))


	lis = []
	lis.append(spase)
	lis.append(tempr)
	lis.append(coco)
	
	for i in lis:
		print(i)

	with open('pogoda', 'wb+') as f:
		f.writelines(str(lis))

if __name__ == '__main__':
	main()
print('Orest finished home work')
