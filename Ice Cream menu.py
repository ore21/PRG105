"""Ice Cream Menu"""
import tkinter


class IceCreamGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Ice Cream Menu')
        self.main_window.geometry('400 x 400')
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # choose a type  of ice cream

        self.inst1 = tkinter.Label(self.top_frame, text='Enter a type of ice cream you are looking for : ')
        self.banana_split = tkinter.Radiobutton(self.top_frame, text='Banana Split ($10)',
                                                variable=self.radio_var, value=1)
        self.sundae = tkinter.Radiobutton(self.top_frame, text='Sundae ($8)', variable=self.radio_var, value=2)
        self.ice_cream_cone = tkinter.Radiobutton(self.top_frame, text='Ice Cream Cone ($7)', variable=self.radio_var, value=3)
        self.frozen_yogurt = tkinter.Radiobutton(self.top_frame, text='Frozen Yogurt ($9)', variable=self.radio_var, value=4)

        # choose flavor options for the ice creams
        self.inst2 = tkinter.Label(self.top_frame, text='Choose a flavor : ')
        self.strawberry_var = tkinter.IntVar()
        self.strawberry_var.set(0)
        self.strawberry = tkinter.Checkbutton(self.top_frame, text='Strawberry ($2)', variable=self.strawberry_var)

        self.chocolate_var = tkinter.IntVar()
        self.chocolate_var.set(0)
        self.chocolate = tkinter.Checkbutton(self.top_frame, text='Chocolate ($1)', variable=self.chocolate_var)

        self.vanilla_var = tkinter.IntVar()
        self.vanilla_var.set(0)
        self.vanilla = tkinter.Checkbutton(self.top_frame, text='Vanilla ($1)', variable=self.vanilla_var)

        self.coffee_var = tkinter.IntVar()
        self.coffee_var.set(0)
        self.coffee = tkinter.Checkbutton(self.top_frame, text='Coffee ($3)', variable=self.coffee_var)

        self.butter_pecan_var = tkinter.IntVar()
        self.butter_pecan_var.set(0)
        self.butter_pecan = tkinter.Checkbutton(self.top_frame, text='Butter Pecan ($10)', variable=self.butter_pecan_var)

        # pack the ice creams and flavour  buttons

        self.inst1.pack()
        self.banana_split.pack(anchor='w', padx=20)
        self.sundae.pack(anchor='w', padx=20)
        self.ice_cream_cone.pack(anchor='w', padx=20)
        self.frozen_yogurt.pack(anchor='w', padx=20)

        self.inst2.pack()
        self.strawberry.pack(anchor='w', padx=20)
        self.chocolate.pack(anchor='w', padx=20)
        self.vanilla.pack(anchor='w', padx=20)
        self.coffee.pack(anchor='w', padx=20)
        self.butter_pecan.pack(anchor='w', padx=20)

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

        tkinter.mainloop()

    def calc_menu(self):
        order_total = 0
        if self.radio_var.get() == 1:
            # item_cost_1 = 3
            order_total = 3
        elif self.radio_var.get() == 2:
            order_total = 4
        elif self.radio_var.get() == 3:
            # item_cost_1 = 4
            order_total = 4
        elif self.radio_var.get() == 4:
            # item_cost_1 = 2
            order_total = 2

        if self.strawberry_var.get() == 1:
            order_total += 1
        if self.chocolate_var.get() == 1:
            order_total += 2
        if self.vanilla_var.get() == 1:
            order_total += 3
        if self.coffee_var.get() == 1:
            order_total += 4
        if self.butter_pecan_var.get() == 1:
            order_total += 2

            tkinter.mainloop()
        # send order total
        self.cost_button.set('Order Total: ${}'.format(order_total))


ice_cream_gui = IceCreamGUI()
