"""Miles Per Gallon Calculator"""


import tkinter


class GasMileageGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.mpg_frame = tkinter.Frame()

        self.prompt_label = tkinter.Label(self.top_frame,
                                          text='Enter a number of gas gallons it can hold :')
        self.GallonsOfGas_value_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label.pack(side='left')
        self.GallonsOfGas_value_entry.pack(side='left')

        self.describe_label = tkinter.Label(self.mid_frame, text='Enter the number of miles :')

        self.value = tkinter.StringVar()
        self.NumOfMiles_value_entry = tkinter.Entry(self.mid_frame, textvariable=self.value)

        self.describe_label.pack(side='left')
        self.NumOfMiles_value_entry.pack(side='left')

        self.MPG_value_button = tkinter.Button(self.bottom_frame, text='Calculate', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.MPG_value_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()


        tkinter.mainloop()

    def convert(self):
        gallons = float(self.GallonsOfGas_value_entry.get())
        miles = float(self.NumOfMiles_value_entry.get())
        mpg = gallons / miles
        mpg = format(mpg, '.2f')
        self.value.set(mpg)

MPG_converter = GasMileageGUI()


