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
wilgotnoscGleby_data = [] # 2
deszcz_data = [] # 3
cisnienie_data = [] # 4
#wysokosc_data = [] # 5
swiatlo_data = [] # 6


def read_data():
    
    dataPacket = arduinoData.readline().decode('utf-8')
    dataSplit = dataPacket.split(',')
    wilgotnosc = dataSplit[0]
    temperatura = dataSplit[1]
    wilgotnoscGleby = dataSplit[2]
    deszcz = dataSplit[3]
    cisnienie = dataSplit[4]
    #wysokosc = dataSplit[5]
    swiatlo = dataSplit[6]
    return float(wilgotnosc), float(temperatura), float(wilgotnoscGleby), float(deszcz), float(cisnienie), float(swiatlo)

def update_plot(frame):
    
    wilgotnosc, temperatura, wilgotnoscGleby, deszcz, cisnienie, swiatlo = read_data()
    x_vals.append(time.time())
    wilgotnosc_data.append(wilgotnosc)
    temperatura_data.append(temperatura)
    wilgotnoscGleby_data.append(wilgotnoscGleby)
    deszcz_data.append(deszcz)
    cisnienie_data.append(cisnienie)
    swiatlo_data.append(swiatlo)

    plt.clf() # Wyczyszczenie wykresu
    
    # Wykres wilgotnosci i temperatury
    plt.subplot(2,2,1)
    plt.plot(x_vals, wilgotnosc_data, label='Wilgotnosc')
    plt.plot(x_vals, temperatura_data, label='Temperatura')
    plt.legend()
    
    # Wykres światła
    plt.subplot(2,2,2)
    plt.plot(x_vals, swiatlo_data, label='Światło')
    plt.legend()
    
    # Wykres ciśnienia
    plt.subplot(2,2,3)
    plt.plot(x_vals, cisnienie_data, label='Ciśnienie')
    plt.legend()
    
    # Wykres Deszczu i wilgotności gleby
    plt.subplot(2,2,4)
    plt.plot(x_vals, wilgotnoscGleby_data, label='Wilgotnosc Gleby')
    plt.plot(x_vals, deszcz_data, label='Czujnik Deszczu')
    plt.legend()

plt.ioff()  # Wyłącz tryb interaktywny, jeśli nie jest potrzebny

fig, ax = plt.subplots()
animation = FuncAnimation(fig, update_plot,frames=60, interval=2000)  # Zmniejszenie częstotliwości odświeżania
plt.show()