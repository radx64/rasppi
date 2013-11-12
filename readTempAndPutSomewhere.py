import smbus
import time
import MySQLdb
import datetime

db = MySQLdb.connect(host="localhost", user="root", passwd="toor", db="temperatures")

querry = db.cursor()

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
	currentTemperature = "%d.%d" %(tempMSB, tempLSB)
	print "Temp: %s 'C" % currentTemperature  
	now = datetime.datetime.now()
	querry.execute("INSERT INTO temp_readings(date, temperature) VALUES(\""+now.strftime("%Y-%m-%d %H:%M:%S")+"\", "+currentTemperature+")")
	db.commit()
	time.sleep(1)

