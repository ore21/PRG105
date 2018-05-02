import tkinter
import tkinter.messagebox
import pickle


class CrudGUI:
    def __init__(self, master, cust):
        self.master = master
        self.master.title('Welcome Menu')
        self.customer_list = cust
        self.radio_var = 0

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',

                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',

                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',

                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',

                                          variable=self.radio_var, value=4)
        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons

        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Save & QUIT', command=self.master.save)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            search = LookGUI(self.master, self.customer_list)

        elif self.radio_var.get() == 2:
            add = AddGUI(self.master, self.customer_list)

        elif self.radio_var.get() == 3:
            change = ChangeGUI(self.master, self.customer_list)

        elif self.radio_var.get() == 4:
            delete = DeleteGUI(self.master, self.customer_list)

        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')

    def save(self):
        print('The info has been updated.')
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customer_list, save_file)
        save_file.close()
        self.master.destroy()


class LookGUI:
    def __init__(self, master, look_cust):
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')
        self.customer_list = look_cust

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customer_list.get(name, 'Not found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:
    def __init__(self, master, add_cust):
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Add a customer')
        self.customer_list = add_cust

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.info_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.add_label = tkinter.Label(self.top_frame, text='Add customer name: ')
        self.add_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.add_label.pack(side='left')
        self.add_entry.pack(side='left')

        # info frame for results
        self.info_label = tkinter.Label(self.info_frame, text='Add info')
        self.info_entry = tkinter.Entry(self.info_frame, widht=15)

        # pack info/middle frame
        self.info_label.pack(side='left')
        self.info_entry.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add', command=self.add)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.info_frame.pack()
        self.bottom_frame.pack()

    def add(self):
        name = self.add_entry.get()
        info = self.info_entry.get()
        if name not in self.customer_list:
            self.customer_list[name] = info
            self.look.destroy()
            tkinter.messagebox.showinfo('List', 'Name has been added')
        else:
            tkinter.messagebox.showinfo('List', 'Name is already in the list')

    def back(self):
        self.look.destroy()


class ChangeGUI:
    def __init__(self, master, change_cust):
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Change a customer')
        self.customer_list = change_cust

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.change_label = tkinter.Label(self.top_frame, text='Change a customer name: ')
        self.change_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.change_label.pack(side='left')
        self.change_entry.pack(side='left')

        # middle frame
        self.info_label = tkinter.Label(self.middle_frame, text='Enter a name to change: ')
        self.info_entry = tkinter.Label(self.middle_frame, width=15)

        # pack Middle frame
        self.info_label.pack(side='left')
        self.info_entry.pack(side='left')

        # buttons for bottom frame
        self.change_button = tkinter.Button(self.bottom_frame, text='Change', command=self.change)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def change(self):
        name = self.change_entry.get()
        info = self.info_entry.get()
        if name not in self.customer_list:
            self.customer_list[name] = info
            self.look.destroy()
            tkinter.messagebox.showinfo('List', 'Name has been changed')
        else:
            tkinter.messagebox.showinfo('List', 'Name cannot be changed changed')

    def back(self):
        self.change.destroy()


class DeleteGUI:
    def __init__(self, master, delete_cust):
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Delete a customer')
        self.customer_list = delete_cust

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.delete_label = tkinter.Label(self.top_frame, text='Delete a customer name: ')
        self.delete_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.delete_label.pack(side='left')
        self.delete_entry.pack(side='left')

        # buttons for bottom frame
        self.delete_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.delete_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def delete(self):
        name = self.delete_entry.get()
        if name not in self.customer_list:
            del self.customer_list[name]
            self.look.destroy()
            tkinter.messagebox.showinfo('List', 'Name has been Deleted')
        else:
            tkinter.messagebox.showinfo('List', 'Name cannot be deleted')

    def back(self):
        self.delete.destroy()


def main():
    try:
        input_file = open("customer_file.dat", 'rb')
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        customers = {}

    # create a window
    root = tkinter.Tk()

    # call the GUI and send it the root menu
    menuGui = CrudGUI(root, customers)

    # control the mainloop from main instead of the class
    root.mainloop()


main()
