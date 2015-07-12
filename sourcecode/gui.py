__author__ = 'MiR.am'

# program name: EasyData
# developer: MiR.am
# date: July 11, 2015
# version: 0.5 Alpha
# License: GNU General Public License v3.0

# in this module, Graphical user interface created

# Tkinter module used for creating GUI
from Tkinter import *
from threading import Thread
import tkFileDialog
import tkMessageBox as tkmsg
import tkFont
import ctypes
import sys
import misc
import getdata


ctypes.windll.kernel32.SetConsoleTitleA("EasyData By MiR.am")

# information about program
about = """ EasyData Program\n
 Version: 0.5 Alpha (July 11, 2015)
 Program Developer: MiR.am (mir-am@hotmail.com)
 License: GNU General Public License v3.0

 If you encouter any error or have questions,
   send an email to the developer

 You can download soruce code and latest version of\n  program at github:
   https://github.com/mir-am/easydata
   """


class TopWin(Toplevel):

    def __init__(self, master, title, message, width, height, wm_del=False):

        Toplevel.__init__(self, master, width=width, height=height)

        self.title(title)
        self.resizable(0, 0)
        self.grab_set()
        self.transient()

        if wm_del:

            self.protocol("WM_DELETE_WINDOW", self.close_win)

        Message(self, text=message, width=320,
                font=tkFont.Font(family="Arial", size=9, weight=tkFont.BOLD)).pack(side=TOP)

    def close_win(self):

        tkmsg.showwarning('Warning!', 'The Program has not fineshed its job yet!')


# widgets created in this function
def program_gui():

    #  creating Top-Level Window

    top_level_win = Tk()
    top_level_win.title("Easy Data By MiR.am")
    top_level_win.minsize(580, 405)
    top_level_win.maxsize(580, 405)
    top_level_win.resizable(0, 0)

    # creaing menu for top-level window

    top_win_menu = Menu(top_level_win)
    top_level_win.config(menu=top_win_menu)

    main_menu = Menu(top_win_menu, tearoff=0)

    main_menu.add_command(label='About', underline=0, command=lambda: TopWin(top_level_win,
                                                        "About Program", about, 420, 250))
    main_menu.add_command(label='Exit', underline=0, command=sys.exit)

    top_win_menu.add_cascade(label="Main Menu", underline=0, menu=main_menu)

    # creating a label for helping users
    help_label = Label(top_level_win, text="Select Stations with Ctrl or Shift key\n"
                                           " Make sure that you are connected to the internet!",
                       font=tkFont.Font(family="Arial", size=9, weight=tkFont.BOLD))
    help_label.grid(row=0, column=1, pady=5)

    # creating Label Frame for Stations
    st_label = LabelFrame(top_level_win, text="Stations")
    st_label.grid(row=1, column=0, rowspan=2, padx=3, pady=3)

    st_list = Listbox(st_label, width=20, height=20, selectmode=EXTENDED)  # list box for inserting stations

    scroll_bar = Scrollbar(st_label, orient=VERTICAL)  # scroll bar for list box

    scroll_bar.config(command=st_list.yview)
    st_list.config(yscrollcommand=scroll_bar.set)

    st_list.grid(row=1, column=0, padx=4, pady=4)
    scroll_bar.grid(row=1, column=1, sticky=NE + SE)

    # inserting stations names in list box
    for label in range(misc.stations.__len__()):

        st_list.insert(label, misc.stations[label].values()[0] + " - " +misc.stations[label].keys()[0])


    # creating label frame for variables
    var_label = LabelFrame(top_level_win, text="Select Variable")
    var_label.grid(row=1, column=1, padx=3, pady=3, sticky=N)

    cb_var_list = []

    for cb_box in range(misc.var_names.__len__()):

        cb_values = IntVar()

        Checkbutton(var_label, text=misc.var_names[cb_box + 1],
                    variable=cb_values, onvalue=cb_box + 1).grid(row=cb_box, column=0, sticky=W)

        cb_var_list.append(cb_values)

    # creating label frame for data types

    data_label = LabelFrame(top_level_win, text="Data Types")
    data_label.grid(row=1, column=2, padx=3, pady=3, sticky=N)

    cb_dt_list = []

    for c_box in range(misc.data_type_name.__len__()):

        cb_values = IntVar()

        Checkbutton(data_label, text=misc.data_type_name[c_box], variable=cb_values,
                    onvalue=c_box + 1).grid(row=c_box, column=0, sticky=W)

        cb_dt_list.append(cb_values)

    # creating label frame for save location

    save_label = LabelFrame(top_level_win, text="Save Location")
    save_label.grid(row=2, column=1, sticky=NW)

    # a button for choosing a path for saving data
    # a variable for user path
    global save_path
    save_path = None

    def ask_dir():

        global save_path
        save_path = tkFileDialog.askdirectory().replace('/', "\\")
        address_label.config(text= "Address: " + save_path)

    save_button = Button(save_label, text="Save", width=10, height=1, command=ask_dir)
    save_button.grid(row=0, column=0, padx=8, pady=8)

    address_label = Label(save_label)
    address_label.grid(row=1, column=0, padx=5, pady=5)

    # creating label frame for processing data section

    pd_label = LabelFrame(top_level_win, text="Getting Data")
    pd_label.grid(row=2, column=2)

    # a list for saving user data
    global user_data_type
    user_data_type = []

    # a list for saving user variables
    global user_var_list
    user_var_list = []

    # get data for user
    def get_data():

        if not misc.get_data_flag:

            global user_data_type
            global user_var_list
            user_data_type = []
            user_var_list = []

            for value in cb_dt_list:

                if value.get() != 0:

                    user_data_type.append(str(value.get()))

            for value in cb_var_list:

                if value.get() != 0:

                    user_var_list.append(value.get())

            # check that user select options
            if (0 < st_list.curselection().__len__() <= 30) and \
                user_var_list.__len__() != 0 and user_data_type.__len__() != 0\
                    and save_path is not None:

                if tkmsg.askyesno("Validation", "Are you sure that you want to get data with"
                                                " these options?"):

                    pd_thread = Thread(target=getdata.process_user_rq, args=(user_data_type, st_list.curselection(),
                                                                             user_var_list, save_path))

                    pd_thread.start()

                    tkmsg.showinfo("Please Wait...", "The Program is making your data ready!\n The Windows"
                                   " Explorer will open your data when the data is ready")


                else:

                    user_data_type = []
                    user_var_list = []

            else:

                tkmsg.showwarning("Warning!", "You should select all options such as stations,\n"
                                  " variables, data types and save location")

        else:

            tkmsg.showwarning("Warning!", "Please Wait...\n The Program is busy now! "
                                          "Because of your last data reqeust!")

    # creating a button for getting data from get data module
    gd_button = Button(pd_label, text="Start!", width=10, height=1, command=get_data)
    gd_button.grid(row=0, column=0, padx=5, pady=5)

    top_level_win.mainloop()
