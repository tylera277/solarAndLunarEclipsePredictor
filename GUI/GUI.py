from tkinter import *
from tkinter import messagebox


import os
from os import system as sys
from SolarEclipseCalculator import SolarEclipseCalculator
from LunarEclipseCalculator import LunarEclipseCalculator
from eclipsePlotter import EclipsePlotter
from PIL import ImageTk, Image

import traceback
import numpy as np

class MyWindow:


    def __init__(self, win):
        self.lbl_1 = Label(win, text='Select which you want:')
        self.lbl_1.place(x=50, y=50)

        self.lbl_2 = Label(win,text='Solar Eclipses')
        self.lbl_2.place(x=60, y=100)
        self.Var1 = IntVar()
        self.btn2 = Radiobutton(win, variable=self.Var1, value=0)
        self.btn2.place(x=150, y=100)

        self.lbl_3 = Label(win, text='Lunar Eclipses')
        self.lbl_3.place(x=60, y=130)
        self.btn3 = Radiobutton(win, variable=self.Var1, value=1)
        self.btn3.place(x=150, y=130)

        self.lbl_year = Label(win, text='Year:')
        self.lbl_year.place(x=60, y=180)
        self.year_entry = Entry(win)
        self.year_entry.place(x=130, y=180)

        self.lbl_month = Label(win, text='Month:')
        self.lbl_month.place(x=60, y=230)
        self.month_entry = Entry(win)
        self.month_entry.place(x=130, y=230)
        self.lbl_month_notice = Label(win, text='(Enter specific month or 13 for whole year)')
        self.lbl_month_notice.place(x=60,y=260)

        self.lbl_timestep = Label(win, text='Time Step:')
        self.lbl_timestep.place(x=60, y=300)
        self.timestep_entry = Entry(win)
        self.timestep_entry.place(x=130, y=300)
        self.lbl_timestep_notice = Label(win, text='(Suggested Time Step is 60)')
        self.lbl_timestep_notice.place(x=60, y=330)

        self.b7 = Button(win, text='Calculate', command=lambda: [self.check_values(),
                                                                 self.show_eclipse_times()])
        self.b7.place(x=80, y=380)

        self.reset_button = Button(win, text='Reset', command=lambda: self.reset())
        self.reset_button.place(x=180, y=380)

        self.plot_button = Button(win, text="Plot", command=lambda: self.plot())
        self.plot_button.place(x=290, y=465)

        self.output_listbox = Listbox(win)
        self.output_listbox.place(x=90, y=415)

        self.plot_image = Label(win)
        self.plot_image.place(x=350, y=200)

        #self.output = Text(win, height=10, width=30)
        #self.output.place(x=400, y=10)

    def check_values(self):
        try:
            year1 = int(self.year_entry.get())
            month1 = int(self.month_entry.get())
            timestep1 = int(self.timestep_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Didnt enter a number")


        if month1<1 or month1>12:
            if month1 != 13:
                messagebox.showerror("Error", "Months must be between 1 and 12, or 13")
        if timestep1>60 or timestep1<1:
            messagebox.showerror("Error", "Time Step must be between 1 and 60")
            self.reset()
        if year1<1550 or year1>2650:
            messagebox.showerror("Error", "Year must be between 1550 and 2650")
            self.reset()




    def show_eclipse_times(self):
        """
        For date user entered, calculates the start times when eclipse
        will happen.
        """
        global months, year

        eclipse_check = int(self.Var1.get())
        if eclipse_check == 0:
            solar_eclipse_check = 1
            lunar_eclipse_check = 0
        elif eclipse_check == 1:
            solar_eclipse_check = 0
            lunar_eclipse_check = 1
        else:
            print("No eclipse selected")

        year = int(self.year_entry.get())
        month = int(self.month_entry.get())
        timestep = int(self.timestep_entry.get())

        counter = 0
        # Solar eclipse only calculator
        if solar_eclipse_check == 1 and lunar_eclipse_check == 0:


            eclipse_dates, months = SolarEclipseCalculator(year, month, timestep).DetermineTimes()

            for i in range(1,13,1):
                if eclipse_dates[i][0] != 0:
                    self.output_listbox.insert(END, eclipse_dates[i][0])
                    counter += 1
                else:
                    pass
            if counter == 0:
                self.output.insert(END, '{}\n'.format("None Found for that month/year!"))

        # Lunar Eclipse only calculator
        elif solar_eclipse_check == 0 and lunar_eclipse_check == 1:

            eclipse_dates, months = LunarEclipseCalculator(year, month, timestep).DetermineTimes()

            counter = 0
            for i in range(1, 13, 1):
                if eclipse_dates[i][0] != 0:
                    self.output_listbox.insert(END, eclipse_dates[i][0])
                    counter += 1
                else:
                    pass
            if counter == 0:
                self.output.insert(END, '{}\n'.format("None Found for that month/year!"))

    def reset(self):
        """ Clears the entry fields."""
        self.year_entry.delete(0, 'end')
        self.month_entry.delete(0, 'end')
        self.timestep_entry.delete(0, 'end')
        #self.Var1.set("")
        self.Var1.set(0)
        self.output_listbox.delete(0, 'end')

    def plot(self):
        """
        Generates a plot of the trace of the solar eclipse as it travels
        across the earth's surface.
        """

        for i in self.output_listbox.curselection():
            selected_month = months[i]

        eclipse_dates, _ = SolarEclipseCalculator(year, selected_month, 10)\
                                                                    .DetermineTimes()

        lat, lon = EclipsePlotter(eclipse_dates, month=selected_month).latANDlonFinder()

        # Class which plots those points onto a graph
        _ = EclipsePlotter(eclipse_dates, month=selected_month).plotter(lat, lon)
        # self.output.insert(END, selected_month)

        # Plotting of the generated image
        earth_image = Image.open('./generated_plot.png')
        earth_image = earth_image.resize((400, 200))
        self.img = ImageTk.PhotoImage(earth_image)
        self.plot_image.configure(image=self.img)


window=Tk()
mywin=MyWindow(window)
window.title('Eclipse Calculator')
window.geometry("800x600")
window.mainloop()
