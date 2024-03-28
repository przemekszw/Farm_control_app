import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

arduinoData = serial.Serial('COM3', 9600)
time.sleep(1)

x_vals = []
# listy do przechowywania danych
wilgotnosc_data = [] # 0
temperatura_data = [] # 1

def read_data():
    
    dataPacket = arduinoData.readline().decode('utf-8')
    dataSplit = dataPacket.split(',')
    wilgotnosc = dataSplit[0]
    temperatura = dataSplit[1]

    return float(wilgotnosc), float(temperatura)

def update_plot(frame):
    
    wilgotnosc, temperatura = read_data()
    x_vals.append(time.time())
    wilgotnosc_data.append(wilgotnosc)
    temperatura_data.append(temperatura)


    plt.clf() # Wyczyszczenie wykresu
    
    # Wykres wilgotnosci i temperatury
    plt.subplot(2,2,1)
    plt.plot(x_vals, wilgotnosc_data, label='Wilgotnosc')
    plt.plot(x_vals, temperatura_data, label='Temperatura')
    plt.legend()
    
    
plt.ioff()  # Wyłącz tryb interaktywny, jeśli nie jest potrzebny

fig, ax = plt.subplots()
animation = FuncAnimation(fig, update_plot,frames=60, interval=2000)  # Zmniejszenie częstotliwości odświeżania
plt.show()