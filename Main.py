import time
import serial
from tkinter import *
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation

arduinoData=serial.Serial('COM3',9600)
time.sleep(1)

def read_data():
    # Pobranie wartości z Serial 
    dataPacket = arduinoData.readline().decode('utf-8')
    dataSplit = dataPacket.split(',')

    # Zdeklarowanie zmiennych dla czujników
    wilgotnosc = dataSplit[0]
    temperatura = dataSplit[1]
    wilgotnoscGleby = dataSplit[2]
    deszcz = dataSplit[3]
    cisnienie = dataSplit[4]
    wysokosc = dataSplit[5]
    swiatlo = dataSplit[6]
    pin = dataSplit[7]
        
    lbl_temperatura.config(text=f'Wilgotność: {wilgotnosc}')
    lbl_wilgotnosc.config(text=f'Temperatura: {temperatura}')
    lbl_wilgotnoscGleby.config(text=f'Wilgotność gleby: {wilgotnoscGleby}')
    lbl_deszcz.config(text=f'Czujnik desczu: {deszcz}')
    lbl_cisnienie.config(text=f'Ciśnienie: {cisnienie}')
    lbl_wysokosc.config(text=f'Wysokość: {wysokosc}')
    lbl_swiatlo.config(text=f'Naświetlenie: {swiatlo}')
    
    print(dataPacket)
    print(pin)
    
    window.after(2000, read_data)
    
def pumpOn():
 
    arduinoData.write(bytes('N', 'UTF-8'))
   
    
    
def simpleToggle():
    
    if btn_pump.config('text')[-1] == 'On':
        btn_pump.config(text='Off')
    else:
        btn_pump.config(text='On')
    
# Tkinter root window
window = Tk()
window.config(bg='grey')
window.title("Farm control app")
window.geometry('400x600')

# Labels
lbl_wilgotnosc = tk.Label(window, text='Waiting for data...')
lbl_wilgotnosc.pack()

lbl_temperatura = tk.Label(window, text='Waiting for data...')
lbl_temperatura.pack()

lbl_wilgotnoscGleby = tk.Label(window, text='Waiting for data...')
lbl_wilgotnoscGleby.pack()

lbl_deszcz = tk.Label(window, text='Waiting for data...')
lbl_deszcz.pack()

lbl_cisnienie = tk.Label(window, text='Waiting for data...')
lbl_cisnienie.pack()

lbl_wysokosc = tk.Label(window, text='Waiting for data...')
lbl_wysokosc.pack()

lbl_swiatlo = tk.Label(window, text='Waiting for data...')
lbl_swiatlo.pack()

btn_pump = tk.Button(window, text ="Off", command = simpleToggle)
btn_pump.pack()

btn_pumpOn = tk.Button(window, text ="Pompa", command = pumpOn)
btn_pumpOn.pack()


read_data()

window.mainloop()