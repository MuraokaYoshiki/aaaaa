import serial
import requests
import time
def let(c):
    command = bytearray.fromhex(c)
    crc = 0xFFFF

    for i in range(len(command)):
        crc = crc ^ command[i]
        
        for j in range(8):
            flag = crc & 1
            crc = crc >> 1
            
            if(flag == 1):
                crc = crc^0xA001
    command += bytearray([crc & 0x00FF,crc >> 8])
    print(command.hex())
    return command.hex()

while True:
    sensor = serial.Serial("/dev/ttyUSB0",115200,serial.EIGHTBITS,serial.PARITY_NONE)
    sensor.write(bytearray.fromhex(let("52420500012150")))

    time.sleep(5)

    data = sensor.read(sensor.inWaiting())
    
    print(data.hex())
    temperature = (data[9] * 256 + data[8] )*0.01
    humidity = (data[11] * 256 + data[10])*0.01
    kiatsu = (data[17] * 256 *256 *256 + data[16]*256*256 + data[15] * 256 + data[14])*0.001
    light = (data[13] * 256 + data[12])*1
    noiz = (data[19] * 256 + data[18] )*0.01
    co = data[23] * 256 + data[22]
    pda = (data[32] * 256 + data[31])*0.1


    print("Light = {0} lx".format(light))
    print("Temp = {0} c".format(temperature))
    print("kiatsu = {0} hpa".format(kiatsu))
    print("shitsudo = {0} %".format(humidity))
    print("noiz = {0} dB".format(noiz))
    print("co = {0} ppm".format(co))
    print("pga = {0} gal".format(pda))

    body = {"id":0,"type":"temperature","value":temperature}
    response = requests.post("http://10.145.146.47:8080/value",json = body)
    print("Response = {0}".format(response.text))
    
    body = {"id":1,"type":"humidity","value":humidity}
    response = requests.post("http://10.145.146.47:8080/value",json = body)
    print("Response = {0}".format(response.text))
    
    body = {"id":2,"type":"light","value":light}
    response = rresponse = requests.post("http://10.145.146.47:8080/value",json = body)
    print("Response = {0}".format(response.text))