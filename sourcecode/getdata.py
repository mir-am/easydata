__author__ = 'MiR.am'

# program name: EasyData
# developer: MiR.am
# date: June 14, 2015
# version: 0.4 Alpha
# License: GNU General Public License v3.0


# in this module we get data from chaharmahalmet website

# we use urllib to download content of webpage
# using parse package for parsing string
# we use beatifulsoup module for parsing the HTML
# os module imported for make directory
# time module imported for measuring running time

from colorama import Fore
from bs4 import BeautifulSoup
from datetime import datetime
from time import time as r_time
import urllib
import os
import misc
import excelfile


# download data from web page
def dl_data(urlname):

    try:

        return urllib.urlopen(urlname).read()

    except Exception as error:

        print (Fore.RED + "Error: Make sure that you are connected to the internet!\n"
               + str(error))


# get data from downloaded page
def parse_htmlpage(htmldoc):

    try:

        return BeautifulSoup(htmldoc).find_all('pre')[1].contents[0]

    except Exception as error:

        print (Fore.RED + "Error: Could not get data!\n" + str(error))


# saving data in textfile
def save_textfile(filename, content):

    try:

        open(filename, 'w').writelines(content + "\n")

    except Exception as error:

        print (Fore.RED + "Error: Could not save data in textfile!\n" + str(error))

# reading data from text file
def read_data(filename):

    try:

        return open(filename, 'r').readlines()

    except Exception as error:

        print (Fore.RED + "Error: Could not read data from text file!\n" + str(error))


# getting station name, lat, lon, elevation, years,
# mean and sd from string, actually we get long-term data. e.g 10 years data
def ext_lt_data(data):

    try:

        data_ext = {"stationname": None, "lat": None, "lon": None, "elevation": None,
                    "Mean": None, "SD": None, "years": 0}

        for line in data:

            if "STATION" in line:

                data_ext["stationname"] = line.strip()[line.index("STATION")
                                                          + 5: 25].strip()

            elif "LATITUDE" in line:

                # Converting to decimal degree
                # using round to make numbers only 2 digits
                data_ext["lat"] = round(float(line.split()[1:3][0]) + (float(line.split()[1:3][1])
                                                                       / 60), 2)

            elif "LONGITUDE" in line:

                data_ext["lon"] = round(float(line.split()[1:3][0]) + (float(line.split()[1:3][1])
                                                                       / 60), 2)

            elif "ELEVATION" in line:

                data_ext["elevation"] = float(line.split()[1])

            elif "MEAN" in line:

                # using try/except block for preventing error during run time
                try:

                    data_ext["Mean"] = float(line.split()[-1])

                except ValueError:

                    pass

            elif "SD" in line:

                data_ext["SD"] = float(line.split()[-1])

            # this section count number of aviable years for a station
            if line.rstrip():  # ingnoring blank lines

                # this if checks count number of years with data
                if line.strip().split()[0].isdigit():

                    data_ext["years"] += 1

        return data_ext

    except Exception as error:

        print (Fore.RED + "Could not extract long-term data from text file!\n" + str(error))


# getiing anually data from stations
def ext_data_anually(data):

    try:

        data_ext_anually = {"years": [], "data": []}

        for line in data:

            if line.rstrip():

                # storing a row of data
                row_data = line.strip().split()

                if row_data[0].isdigit():

                    # adding years to the list
                    data_ext_anually["years"].append(int(row_data[0]))

                    try:
                        # adding data to the list
                        data_ext_anually["data"].append(float(row_data[-1]))

                    except ValueError:

                        data_ext_anually["data"].append(row_data[-1])

        return data_ext_anually

    except Exception as error:

        print (Fore.RED + "Could not extract Anually data from text file!\n" + str(error))


# getting monthly data from stations
def ext_data_monthly(data):

    try:

        # for storing monthly data
        data_ext = None

        for line in data:

            if "MEAN" in line.strip()[0:4]:

                data_ext = line.strip().split()[1:-1]

                break

        # converting string to float numbers
        for data in range(data_ext.__len__()):

            try:

                data_ext[data] = float(data_ext[data])

            except ValueError:

                pass

        return data_ext

    except Exception as error:

        print (Fore.RED + "Could not extract Monthly from text file!\n" + str(error))


# extract full data from text files
def ext_full_data(data):

    try:

        data_ext = []

        for line in data:

            if "YEAR" in line:

                for line_new in data[data.index(line):]:

                    if line_new.rstrip():

                        list_temp = line_new.split()

                        for index in range(list_temp.__len__()):

                            try:

                                list_temp[index] = float(list_temp[index])

                            except ValueError:

                                pass

                        data_ext.append(list_temp)

                break

        return data_ext

    except Exception as error:

        print(Fore.RED + "Error: Could not extract full data from text file!\n" + str(error))


# make directories in file system
def make_dir(location):

    try:

        # storing path for saving text files and excel files
        save_path = []

        # make directories for saving files
        for path in [location + "\mydata-" + datetime.today().strftime("%Y-%m-%d-%H-%M"), location +
                    "\mydata-" + datetime.today().strftime("%Y-%m-%d-%H-%M") + "\\textfiles", location +
                    "\mydata-" + datetime.today().strftime("%Y-%m-%d-%H-%M") + "\excelfiles"]:

            os.makedirs(path)

            save_path.append(path)

        return save_path

    except Exception as error:

        print (Fore.RED + "Error: Could not make directories in your computer!\n" + str(error))


# save data as text files for user
def save_data_tf(st_code=[], user_var=[], save_loc=[]):

    try:

        for code in st_code:

            for var in user_var:

                # URL structure: http://www.chaharmahalmet.ir/stat/archive/
                # iran/provincename/stationname/variablename.asp

                path = save_loc[1] + "\\" + misc.stations[int(code)].keys()[0].capitalize() + "-" + var + ".txt"

                save_textfile(path,
                parse_htmlpage(dl_data("http://www.chaharmahalmet.ir/stat/archive/iran/%s/%s/%s.asp"
                % (misc.stations[int(code)].values()[0], misc.stations[int(code)].keys()[0], misc.variables[var]))))

        print (Fore.GREEN + "Data saved as text files!\n")

    except Exception as error:

        print (Fore.RED + "Error: Could not save data as text files!\n" + str(error))


# make long-term data ready for users
def ps_lt_data(st_code=[], user_var=[], save_loc=None):

    try:

        # stations long-term data will store in this variable
        stations_data = {"st_names": [], "lat": [], "lon": [], "elevation": [], "years": [], "tavg": [],
                         "tmin": [], "tmax": [], "rh": [], "pre": [], "dust": [], "wind": [], "sh": []}

        for code in st_code:

            # using this variable for previnting duplicate values for lists
            new_st = True

            for var in user_var:

                path = save_loc[1] + "\\" + misc.stations[int(code)].keys()[0].capitalize() + "-" + var + ".txt"

                store_data = ext_lt_data(read_data(path))

                if new_st:

                    stations_data["st_names"].append(store_data["stationname"])

                    stations_data["lat"].append(store_data["lat"])

                    stations_data["lon"].append(store_data["lon"])

                    stations_data["elevation"].append(store_data["elevation"])

                    stations_data["years"].append(store_data["years"])

                    new_st = False

                stations_data[var].append(store_data["Mean"])

        excelfile.ct_lt_excel(stations_data, save_loc[2])

        print (Fore.GREEN + "Long-term Excel data is now ready!\n")

    except Exception as error:

        print (Fore.RED + "Error: Could not Creating long-term excel files!\n " + str(error))


# make anually data ready for users
def ps_data_anually(st_code=[], user_var=[], save_loc=None):

    try:

        # stations anually
        # example: st_data_anually = {"NAEIN": {"year": [2003, 2004], "pre": [23.4, 120] },
        #  "YAZD": {"years": [2001, 2002], "tmax": [28, 32] } }
        st_data_anually = {}

        for code in st_code:

            st_data_anually[misc.stations[int(code)].keys()[0]] = {}

            new_st = True

            for var in user_var:

                path = save_loc[1] + "\\" + misc.stations[int(code)].keys()[0].capitalize() + "-" + var + ".txt"

                store_data = ext_data_anually(read_data(path))

                if new_st:

                    st_data_anually[misc.stations[int(code)].keys()[0]]["years"] = store_data["years"]

                    new_st = False

                st_data_anually[misc.stations[int(code)].keys()[0]][var] = store_data["data"]

        excelfile.ct_anually_excel(st_data_anually, save_loc[2])

        print (Fore.GREEN + "Anually data as excel files is now ready!\n")

    except Exception as error:

        print (Fore.GREEN + "Error: Could not creating anually data!\n" + str(error))


# make monthly data ready for users
def ps_data_monthly(st_code=[], user_var=[], save_loc=None):

    try:

        # monthly data
        # exmaple: st_data_monthly = {"ARAK": {"tmin": [10, 12]}}
        st_data_monthly = {}

        for code in st_code:

            st_data_monthly[misc.stations[int(code)].keys()[0]] = {}

            for var in user_var:

                path = save_loc[1] + "\\" + misc.stations[int(code)].keys()[0].capitalize() + "-" + var + ".txt"

                store_data = ext_data_monthly(read_data(path))

                st_data_monthly[misc.stations[int(code)].keys()[0]][var] = store_data

        excelfile.ct_monthly_excel(st_data_monthly, save_loc[2])

        print (Fore.GREEN + "Monthly data as excel files is now ready!\n")

    except Exception as error:

        print (Fore.GREEN + "Error: Could not creating Monthly data!\n" + str(error))


# make full data ready for users
def ps_full_data(st_code=[], user_var=[], save_loc=None):

    try:

        # storing full data
        # example: {"tabriz": {"pre": [[...], [...]] } }
        st_full_data = {}

        for code in st_code:

            st_full_data[misc.stations[int(code)].keys()[0]] = {}

            for var in user_var:

                path = save_loc[1] + "\\" + misc.stations[int(code)].keys()[0].capitalize() + "-" + var + ".txt"

                store_data = ext_full_data(read_data(path))

                st_full_data[misc.stations[int(code)].keys()[0]][var] = store_data

        excelfile.ct_fulldata_excel(st_full_data, save_loc[2])

        print(Fore.GREEN + "Full data as excel files is now ready!\n")

    except Exception as error:

        print("Error: Could not creating full data from text files\n" + str(error))

# prcoess user request
def process_user_rq(user_choices=[], st_code=[], user_var=[], save_loc=None):

    time = r_time()

    path = make_dir(save_loc)

    save_data_tf(st_code, user_var, path)

    # "1" is long-term data
    if "1" in user_choices:

        ps_lt_data(st_code, user_var, path)

    # "2" is Anually data
    if "2" in user_choices:

        ps_data_anually(st_code, user_var, path)

    # "3" is Monthly data
    if "3" in user_choices:

        ps_data_monthly(st_code, user_var, path)

    # "4" is full data
    if "4" in user_choices:

        ps_full_data(st_code, user_var, path)

    print (Fore.GREEN + "You can see your data at this address: %s\nyour request finished in %.2f"
           " seconds\n" % (path[0], r_time() - time))
