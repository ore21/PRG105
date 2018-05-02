"""Customer Interface"""

import tkinter


class Garage:
    def __init__(self):
        self.main_window = tkinter.Tk
        self.main_window.title('Garage Menu')
        self.main_window.geometry('400 * 400')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # choose item to look for
        self.inst1 = tkinter.Label(self.top_frame, text='Enter an item you want to look for: ')
        self.shirts = tkinter.Radiobutton(self.top_frame, text='Shirts ($10)',variable=self.radio_var, value=1)
        self.jeans = tkinter.Radiobutton(self.top_frame, text='Jeans ($15)',variable=self.radio_var, value=2)
        self.hats = tkinter.Radiobutton(self.top_frame, text='Hats ($5)', variable=self.radio_var, value=3)
        self.shoes = tkinter.Radiobutton(self.top_frame, text='Shoes ($25)', variable=self.radio_var, value=4)

        # choose color options for the items
        self.inst2 = tkinter.Label(self.top_frame, text='Choose any color options: ')

        self.red_var = tkinter.IntVar()
        self.red_var.set(0)
        self.red = tkinter.Checkbutton(self.top_frame, text='Red ($2)', variable=self.red_var)

        self.black_var = tkinter.IntVar()
        self.black_var.set(0)
        self.black = tkinter.Checkbutton(self.top_frame, text='Black ($3)', variable=self.black_var)

        self.brown_var = tkinter.IntVar()
        self.brown_var.set(0)
        self.brown = tkinter.Checkbutton(self.top_frame, text='Brown ($1)', variable=self.brown_var)

        self.white_var = tkinter.IntVar()
        self.white_var.set(0)
        self.white = tkinter.Checkbutton(self.top_frame, text='White ($5)', variable=self.white_var)

        self.gray_var = tkinter.IntVar()
        self.gray_var.set(0)
        self.gray = tkinter.Checkbutton(self.top_frame, text='Gray ($10)', variable=self.gray_var)
        # pack the items and color  buttons
        self.inst1.pack()
        self.shirts.pack(anchor='w', padx=20)
        self.jeans.pack(anchor='w', padx=20)
        self.hats.pack(anchor='w', padx=20)
        self.shoes.pack(anchor='w', padx=20)

        self.inst2.pack()
        self.red.pack(anchor='w', padx=20)
        self.black.pack(anchor='w', padx=20)
        self.brown.pack(anchor='w', padx=20)
        self.white.pack(anchor='w', padx=20)
        self.gray.pack(anchor='w', padx=20)

        # cost and info buttons
        self.cost_button = tkinter.StringVar()
        self.cost_label = tkinter.Label(self.bottom_frame, textvariable=self.cost_button)
        self.inst3 = tkinter.Label(self.bottom_frame, text='Check your total cost: ')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate total', command=self.calc_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # pack the buttons
        self.inst3.pack()
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def calc_menu(self):
        order_total = 0
        if self.radio_var.get() == 1:
            #item_cost_1 = 3
        order_total = 3

        elif self.radio_var.get() == 2: or self.radio_var.get() == 3:
            #item_cost_1 = 4
        order_total = 4
        elif self.radio_var.get() == 4:
        # item_cost_1 = 2
        order_total = 2


