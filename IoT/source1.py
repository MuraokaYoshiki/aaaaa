import serial
import time
sensor = serial.Serial("/dev/ttyUSB0", 115200, serial.EIGHTBITS,serial.PARITY_NONE)
command = bytearray.fromhex("52420a000211510100ffffff")
time.sleep(0.2)
def Loop(command):
    crc = 0xFFFF
    for i in range(len(command)):
        crc = crc^command[i]
        for i in range(8):
            flag = crc & 1
            crc = crc >> 1
            if flag == 1:
                crc = crc ^ 0xA001
    print(format(crc, 'x'))
    print(format(crc, '>16b'))
    command += bytearray([crc & 0x00FF,crc >> 8])
    sensor.write(command)
    Loop(command)
#red
command = bytearray.fromhex("52420a000211510100ff0000")
time.sleep(1.0)
Loop(command)
#green
command = bytearray.fromhex("52420a00021151010000ff00")
time.sleep(1.0)
Loop(command)
#blue
command = bytearray.fromhex("52420a0002115101000000ff")
time.sleep(1.0)
Loop(command)
#something color (maroon)
command = bytearray.fromhex("52420a000211510100800000")
time.sleep(1.0)
Loop(command)
#quit
command = bytearray.fromhex("52420a000211510000ff0000")
time.sleep(1.0)
Loop(command)
print(command.hex())
data = sensor.read(sensor.inWaiting())
print(data.hex())