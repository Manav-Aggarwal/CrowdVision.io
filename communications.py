import serial
import time
from send_data import get_location
import json
path = 'locations.txt'
lastSeen = ''
with open(path, 'r') as f:
	lines = f.readlines()
	if lines:
		lastSeen = lines[-1]

vibration = "n"
with serial.Serial('/dev/cu.usbmodem14401',9600,timeout=10) as ser:
	while True:
		print(vibration)
		with open(path, 'r') as f:
			lines = f.readlines()
			if lines and lastSeen != lines[-1]:
				lastSeen = lines[-1]
				vibration = "y"
		if vibration == "y":
			ser.write(bytes('YES\n','utf-8'))
		elif vibration == "n":
			ser.write(bytes('NO\n','utf-8'))
		time.sleep(1)
		vibration = "n"
