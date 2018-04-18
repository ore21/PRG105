"""Name and Address"""
import tkinter


class MyInfo:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.name_value = tkinter.StringVar()
        self.street_value = tkinter.StringVar()
        self.czs_value = tkinter.StringVar()

        self.info_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.name_label = tkinter.Label(self.info_frame,
                                        textvariable=self.name_value)
        self.street_label = tkinter.Label(self.info_frame,
                                          textvariable=self.street_value)
        self.czs_label = tkinter.Label(self.info_frame,
                                       textvariable=self.czs_value)

        self.name_label.pack()
        self.street_label.pack()
        self.czs_label.pack()

        self.show_info_button = tkinter.Button(self.button_frame,
                                               text='Show Info',
                                               command=self.show)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)

        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='right')

        self.info_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def show(self):
        self.name_value.set('Brandon Gonzalez')
        self.street_value.set('8900, sum rd')
        self.czs_value.set('Il, 60055')


my_info = MyInfo()
