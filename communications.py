import serial
with serial.Serial('/dev/cu.usbmodem14401',9600,timeout=10) as ser:
	while True:
		vibration = input("Vibrate?")
		if vibration == "y":
			ser.write(bytes('YES\n','utf-8'))
		elif vibration == "n":
			ser.write(bytes('NO\n','utf-8'))

 