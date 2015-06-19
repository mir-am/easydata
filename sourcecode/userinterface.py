__author__ = 'MiR.am'

# program name: EasyData
# developer: MiR.am
# date: June 14, 2015
# version: 0.4 Alpha

# userinterface of program created in this module
# Console program


# using colorma for producing colored terminal text
from colorama import init, deinit, Fore
import ctypes
import sys
import Tkinter
import tkFileDialog
import os
import misc
import getdata


def program_ui():

    # storing address for saving file
    global save_location

    # store the variables of user
    global users_variables

    # store stations' code
    global station_code

    # stroring user's choices
    global user_choice

    init(autoreset=True)

    ctypes.windll.kernel32.SetConsoleTitleA("EasyData By MiR.am")

    # show program's info
    print(Fore.YELLOW + """ - EasyData Program
 - Version: 0.4 Alpha (June 14, 2015)
 - Program Developer: MiR.am (mir-am@hotmail.com)
 - License: GNU General Public License v3.0

 - If you encouter any error or have questions,
   send an email to the developer

 - Please read help and make sure that you are connected to intetnet\n  before using the program

 **************************************************
 """)

    while True:

        raw_input('Press Enter to start program... ')

        print "**\nplease see help of the program to write down names of variables\n and stations\n**\n"

        # Step 1:
        while True:

            print "Step 1: You should select a directory to save data\n"

            raw_input("Press Enter to save data...\n")

            # using Tkinter module for showing user a Griphical interface
            # for choosing a folder
            top_win = Tkinter.Tk()

            top_win.withdraw()

            save_location = tkFileDialog.askdirectory()

            top_win.destroy()

            if os.path.exists(save_location):

                print(Fore.GREEN + "Your Data will store at this address: %s\n") % save_location

                break

            else:

                print(Fore.RED + "Error: Invalid Address or you choose not a folder!\n")

        # Step 2:
        while True:

            print "Step 2: You should choose an option or several options. eg 1\n"

            print "1- Long-term Data\n2- Anually Data\n3- Monthly Data\n4- Full Data(" \
                  "all years + all months)"

            user_choice = raw_input("-> ").split(" ")

            if user_choice.__len__() <= 4:

                # count number of valid choice
                valid_choice = 0

                for choice in ["1", "2", "3", "4"]:

                    if choice in user_choice:

                        valid_choice += 1

                if user_choice.__len__() == valid_choice:

                    print (Fore.GREEN + "Valid Choice!\n")

                    break  # user can go next step

                else:

                    print (Fore.RED + "Error: Invalid Choice! try again!\n")

            else:

                print (Fore.RED + "Error: Invalid Choice! try again!\n")

        # Step 3:
        while True:

            while True:

                print "Step 3: Type the names of variables with a space between them.\n" \
                      " e.g pre tmax\n"

                users_variables = raw_input("-> ").split(" ")

                if list(set(misc.variables.keys()).intersection(users_variables)).__len__()\
                        == users_variables.__len__():

                    print (Fore.GREEN + "All Variables' names was valid!\n")

                    break  # if names of variables is valid. user can go next step

                else:

                    print (Fore.RED + "Error: Invalid Variables! Try agian!\n")

            misc.print_var(users_variables)

            print "are you sure that you want these variables? 'yes' or 'no' \n"

            if raw_input('-> ').lower() == 'yes':

                break  # user can go next step

        # Step 4:
        while True:

            while True:

                print "Step 4: Type Stations' code with a space between them. e.g 2 3\n" \
                      "Please see help of the program for stations' codes \n"

                station_code = raw_input("-> ").split(" ")

                # check vaildity of stations' code
                # number of stations should be lower than 30
                if station_code.__len__() <= 30:

                    # count number of valid stations' code
                    valid_st_code = 0

                    for st_code in station_code:

                        if st_code.isdigit() and (0 <= int(st_code) <= 201):

                            valid_st_code += 1

                    if station_code.__len__() == valid_st_code:

                        print (Fore.GREEN + "All stations' code was valid!\n")

                        break  # if all st_code is valid, user can go next step.

                    else:

                        print (Fore.RED + "Error: Stations' code is not valid! Try again!\n")

                else:

                    print (Fore.RED + "Error: number of stations should be lower than 30!."
                                      " Try again!\n")

            misc.print_st_names(station_code)

            print "are you sure that you want these stations? 'yes' or 'no' \n"

            if raw_input("-> ").lower() == "yes":

                break  # user can go next step

        # Step 5: Processing data request

        print "Step 5: Precessing data request.\nPlease wait...\n The program is getting your data from Charharmahl" \
              " and converting it to textfiles\n"

        getdata.process_user_rq(user_choice, station_code, users_variables, save_location)

        print "Do you want to get data agian? 'yes' or 'no'\n"

        if raw_input("-> ").lower() == "no":

            break

    # stopping colorma module!
    deinit()

    # program will terminate with this statement
    sys.exit()