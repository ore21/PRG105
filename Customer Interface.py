"""Customer Interface"""

import tkinter
import tkinter.messagebox


class Business:
    def __init__(self, cust):
        self.customer_list = cust
        self.radio_var = 0
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.garage = tkinter.Radiobutton(self.top_frame, text='Garage',
                                          variable=self.radio_var, value=100)
        self.salon = tkinter.Radiobutton(self.top_frame, text='Salon',
                                         variable=self.radio_var, value=200)
        self.coffee_shop = tkinter.Radiobutton(self.top_frame, text='Coffee Shop',
                                               variable=self.radio_var, value=300)
        self.car_shop = tkinter.Radiobutton(self.top_frame, text='Car Shop',
                                            variable=self.radio_var, value=400)
        self.toy_store = tkinter.Radiobutton(self.top_frame, text='Toy Store',
                                             variable=self.radio_var, value=80)
        self.tech_shop = tkinter.Radiobutton(self.top_frame, text='Tech Shop',
                                             variable=self.radio_var, value=800)
        self.clothes_shop = tkinter.Radiobutton(self.top_frame, text='Clothes Shop',
                                                variable=self.radio_var, value=155)
        # pack the radio buttons
        self.garage.pack()
        self.salon.pack()
        self.coffee_shop.pack()
        self.car_shop.pack()
        self.toy_store.pack()
        self.tech_shop.pack()
        self.clothes_shop.pack()

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def open_menu(self):
        if self.radio_var.get() == 100:
            open = Business(self.customer_list)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')


customer_interface = Business
