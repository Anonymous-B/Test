# coding=utf-8
import serial, time, math

__author__ = 'yangzhan'

# String number, baud rate based on actual settings Note the content is sent
# modem = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
modem = serial.Serial('COM5', 9600, timeout=1)

# modem.write("AT+CGNSPWR=1\r")
# modem.readline()
# status = modem.readline()
# time.sleep(1)
# modem.write("AT+CGNSSEQ=\"RMC\"\r")
# modem.readline()
# status = modem.readline()
# time.sleep(1)
# modem.write("AT+CGNSTST=1\r")
# modem.readline()
# status = modem.readline()

# time.sleep(1)


print("Start reading GPS values")
while True:
    try:
        line = modem.readline()
        if line.startswith("$GPGGA"):
            index = line.split(",")
            print(index)
            tempNdata = float(index[2]) / 100.0
            tempEdata = float(index[4]) / 100.0
            Ndata = math.floor(tempNdata)
            Edata = math.floor(tempEdata)
            tempNdata = (tempNdata - Ndata) * 100.0
            tempEdata = (tempEdata - Edata) * 100.0
            Ndata += tempNdata / 60
            Edata += tempEdata / 60
            print('Got it! N: %s and E: %s', (Ndata, Edata))
        time.sleep(1)
    except:
        print("quitting")
    # modem.write("AT+CGNSTST=0\r")
    # modem.readline()
    # exit(0)
