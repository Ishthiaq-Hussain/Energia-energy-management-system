import serial
import datetime,time
import csv
csv_filename='toaster.csv'


ser=serial.Serial('/dev/ttyACM0',9600)
while True:
    with open(csv_filename, 'a') as myfile:
        wr = csv.writer(myfile)
        p=ser.readline()
        data=p.split()
        current_date=datetime.datetime.now()
        current_voltage=data[0]
        current_current=data[1]
        mydata=[current_date,current_voltage,current_current]
        wr.writerow(mydata)
        print(mydata)
        myfile.close()








