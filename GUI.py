from tkinter import *
from tkinter import ttk
from SolarEclipseCalculator import SolarEclipseCalculator
from LunarEclipseCalculator import LunarEclipseCalculator
from PIL import ImageTk, Image

import tkinter
import numpy as np

class MyWindow:
    def __init__(self, win):
        self.lbl_1 = Label(win, text='Select which you want:')
        self.lbl_1.place(x=50,y=50)

        self.lbl_2 = Label(win,text='Solar Eclipses')
        self.lbl_2.place(x=60,y=100)
        self.Var1 = StringVar()
        self.btn2 = Radiobutton(win, variable=self.Var1, value=1)
        self.btn2.place(x=150, y=100)

        self.lbl_3 = Label(win, text='Lunar Eclipses')
        self.lbl_3.place(x=60, y=130)
        self.Var2 = StringVar()
        self.btn3 = Radiobutton(win, variable=self.Var2, value=1)
        self.btn3.place(x=150, y=130)

        self.lbl_year = Label(win, text='Year:')
        self.lbl_year.place(x=60, y=180)
        self.year_entry = Entry(win)
        self.year_entry.place(x=130, y=180)

        self.lbl_month = Label(win, text='Month:')
        self.lbl_month.place(x=60, y=230)
        self.month_entry = Entry(win)
        self.month_entry.place(x=130, y=230)

        self.lbl_timestep = Label(win, text='Timestep:')
        self.lbl_timestep.place(x=60, y=280)
        self.timestep_entry = Entry(win)
        self.timestep_entry.place(x=130, y=280)

        self.b7 = Button(win, text='Calculate', command=lambda:self.show_eclipse_times())
        self.b7.place(x=80, y=330)

        self.reset_button = Button(win, text='Reset', command=lambda:self.reset())
        self.reset_button.place(x=180, y=330)

        self.plot_button = Button(win, text="Plot", command=lambda:self.plot())
        self.plot_button.place(x=260, y=330)

        self.output_listbox = Listbox(win)
        self.output_listbox.place(x=90, y=400)
        self.output = Text(win, height=10, width=30)
        self.output.place(x=400, y=10)

        image = Image.open('./testPlot.png')
        image = image.resize((400,200))
        self.img = ImageTk.PhotoImage(image)
        self.panel = Label(win, image=self.img)
        self.panel.place(x=350, y=200)

        #self.b1=Button(win, text='Add', command=self.add)
        #self.b2=Button(win, text='Subtract', command=self.sub)

    def show_eclipse_times(self):
        try:
            solar_eclipse_check = int(self.Var1.get())
        except:
            solar_eclipse_check = 0

        try:
            lunar_eclipse_check = int(self.Var2.get())
        except:
            lunar_eclipse_check = 0

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
                self.output.insert(END, '{}\n'.format("None Found for that year!"))

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
                self.output.insert(END, '{}\n'.format("None Found for that year!"))

    def reset(self):
        self.year_entry.delete(0, 'end')
        self.month_entry.delete(0, 'end')
        self.timestep_entry.delete(0, 'end')
        self.Var1.set("")
        self.Var2.set("")
        #self.output.delete("1.0", "end")
        self.output_listbox.delete(0, 'end')

    def plot(self):
        pass


    def add(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self):
        self.t3.delete(0, 'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
mywin=MyWindow(window)
window.title('Eclipse Calculator')
window.geometry("800x600")
window.mainloop()
