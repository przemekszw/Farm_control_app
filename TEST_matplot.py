import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arduinoData=serial.Serial('COM3',9600)
time.sleep(1)

x_vals = []
wilgotnosc_data = []
temperatura_data = []

def read_data():
    # Pobranie wartości z Serial 
    dataPacket = arduinoData.readline().decode('utf-8')
    dataSplit = dataPacket.split(',')

    # Zdeklarowanie zmiennych dla czujników
    wilgotnosc = dataSplit[0]
    temperatura = dataSplit[1]
    
    
    x_vals.append(float(time.time()))
    wilgotnosc_data.append(float(wilgotnosc))
    temperatura_data.append(float(temperatura))
    print(temperatura)

def update_plot(frame):
    read_data()
    plt.cla()
    plt.plot(x_vals, wilgotnosc_data, label='Wilgotnosc')
    plt.plot(x_vals, temperatura_data, label='Temperatura')
    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.legend()

fig, ax = plt.subplots()

animation = FuncAnimation(fig, update_plot, interval=10, frames=1000)
plt.show()