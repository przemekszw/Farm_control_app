import numpy as np
import time
import serial
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class WeatherPlotter:
    def __init__(self, serial_port='COM3', baud_rate=9600):
        self.arduino_data = serial.Serial(serial_port, baud_rate)
        time.sleep(1)
        self.x_vals = []
        self.humidity_data = []
        self.temperature_data = []
        self.soil_humidity_data = []
        self.rain_data = []
        self.pressure_data = []
        #self.altitude_data = []  # Na razie zakomentowane, ponieważ nie jest używane w kodzie
        self.light_data = []

    def read_data(self):
        data_packet = self.arduino_data.readline().decode('utf-8')
        data_split = data_packet.split(',')
        return [float(value) for value in data_split]

    def update_plot(self, frame):
        data = self.read_data()
        self.x_vals.append(time.time())

        for i, value in enumerate(data):
            if i == 0:
                self.humidity_data.append(value)
            elif i == 1:
                self.temperature_data.append(value)
            elif i == 2:
                self.soil_humidity_data.append(value)
            elif i == 3:
                self.rain_data.append(value)
            elif i == 4:
                self.pressure_data.append(value)
            #elif i == 5:
                #self.altitude_data.append(value)
            elif i == 6:
                self.light_data.append(value)

        plt.clf()  # Wyczyszczenie wykresu

        plt.subplot(3, 2, 1)
        plt.plot(self.x_vals, self.humidity_data, label='Wilgotnosc')
        plt.plot(self.x_vals, self.temperature_data, label='Temperatura')
        plt.legend()

        plt.subplot(3, 2, 2)
        plt.plot(self.x_vals, self.soil_humidity_data, label='Wilgotnosc Gleby')
        plt.legend()

        plt.subplot(3, 2, 3)
        plt.plot(self.x_vals, self.rain_data, label='Deszcz')
        plt.legend()

        plt.subplot(3, 2, 4)
        plt.plot(self.x_vals, self.pressure_data, label='Cisnienie')
        plt.legend()

        #plt.subplot(3, 2, 5)
        #plt.plot(self.x_vals, self.altitude_data, label='Wysokosc')
        #plt.legend()

        plt.subplot(3, 2, 6)
        plt.plot(self.x_vals, self.light_data, label='Swiatlo')
        plt.legend()

    def start_plotting(self):
        plt.ioff()
        fig, ax = plt.subplots()
        animation = FuncAnimation(fig, self.update_plot, frames=60, interval=2000)
        plt.show()
        
    def stop_plotting(self):
        plt.close('all')

if __name__ == "__main__":
    plotter = WeatherPlotter()
    plotter.start_plotting()
