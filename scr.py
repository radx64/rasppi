import smbus
import time
bus = smbus.SMBus(1)
address = 0x48

bus.write_byte_data(address, 0xac, 0x00) #tryb ciaglego pomiaru
bus.write_byte(address, 0xee)	 #rozpoczyna pomiar

while(True):
	temp = bus.read_word_data(address, 0xaa)  #odbiera dane w kodzie U2
	tempMSB = temp % 256 
	tempLSB = 0
	if (temp > 0xFF):
		tempLSB=5
	print "Temp: %d.%d 'C" % (tempMSB, tempLSB)  

	time.sleep(1)

