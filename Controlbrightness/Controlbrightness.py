import serial
import os
import serial.tools.list_ports  # For listing available serial ports

dev = serial.tools.list_ports.comports()

ports = []

for d in dev:
    ports.append((d.device, d.serial_number))

print('Detected serial ports:')

for d in ports:
    print("Port:" + str(d[0]) + "\tSerial Number:" + str(d[1]))

print('\n포트 번호를 입력주세요')
port = input()
ser = serial.Serial(port="COM"+port, baudrate=9600, )

os.system(os.path.dirname(os.path.realpath(__file__)) + "\\First_Brightness.bat")

cb = 100

while True:
    if ser.readable():
        res = ser.readline()
        print(res.decode()[:len(res) - 1])
        if int(res.decode()[:len(res) - 1]) <= 70:
            if cb < 100:
                while cb != 100:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 70 < int(res.decode()[:len(res) - 1]) <= 120:
            if cb > 90:
                while cb > 90:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 90:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 120 < int(res.decode()[:len(res) - 1]) <= 170:
            if cb > 80:
                while cb > 80:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 80:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 170 < int(res.decode()[:len(res) - 1]) <= 220:
            if cb > 70:
                while cb > 70:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 70:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 220 < int(res.decode()[:len(res) - 1]) <= 270:
            if cb > 60:
                while cb > 60:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 60:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 270 < int(res.decode()[:len(res) - 1]) <= 320:
            if cb > 50:
                while cb > 50:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 50:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 320 < int(res.decode()[:len(res) - 1]) <= 370:
            if cb > 40:
                while cb > 40:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 40:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 370 < int(res.decode()[:len(res) - 1]) <= 420:
            if cb > 30:
                while cb > 30:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 30:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 420 < int(res.decode()[:len(res) - 1]) <= 470:
            if cb > 20:
                while cb > 20:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 20:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 470 < int(res.decode()[:len(res) - 1]) <= 520:
            if cb > 10:
                while cb > 10:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
            else:
                while cb < 10:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Increase_Brightness.bat")
                    cb += 10
        if 520 < int(res.decode()[:len(res) - 1]):
            if cb > 0:
                while cb > 0:
                    os.system(os.path.dirname(os.path.realpath(__file__)) + "\\Decrease_Brightness.bat")
                    cb -= 10
