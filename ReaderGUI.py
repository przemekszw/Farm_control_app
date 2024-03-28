from tkinter import *
import tkinter as tk
from ReaderClass import WeatherPlotter

class SensorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sensor Plotter")

        self.plotter = None

        self.start_button = tk.Button(master, text="Start Plotting", command=self.start_plotting)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Plotting", command=self.stop_plotting, state=tk.DISABLED)
        self.stop_button.pack()

    def start_plotting(self):
        self.plotter = WeatherPlotter()
        self.plotter.start_plotting()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_plotting(self):
        if self.plotter:
            self.plotter.stop_plotting()
            self.plotter = None
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

root = Tk()
app = SensorGUI(root)
root.mainloop()