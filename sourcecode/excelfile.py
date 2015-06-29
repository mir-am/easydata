__author__ = 'MiR.am'

# program name: EasyData
# developer: MiR.am
# date: June 14, 2015
# version: 0.4 Alpha
# License: GNU General Public License v3.0

# data will convert to excel file with help of this module.

# using xlsx writer to convert data to excel file
from datetime import datetime
from colorama import Fore
import xlsxwriter


# header names for excel file
headers_name = ("st_names", "lat", "lon", "elevation", "years", "pre", "tavg", "tmin", "tmax",
                "rh", "dust", "wind", "sh")


# month names for monthly data
month_names = ("Months", "JAN.", "FEB.", "MAR.", "APR.", "MAY", "JUNE", "JULY", "AUG.", "SEP.",
                  "OCT.", "NOV.", "DEC.")


# this method convert data to long-terem excel data
def ct_lt_excel(st_data={}, path=None):

    try:

        # creating an excel file
        workbook = xlsxwriter.Workbook(path + "\long-term-data" + datetime.today()
                                       .strftime("%Y-%m-%d-%H-%M") + ".xlsx")
        # creating a sheet
        worksheet = workbook.add_worksheet()

        global row
        column = 0

        for header in headers_name:

            # only variables with value should be written in excel file
            if st_data[header].__len__() > 0:

                # row should be zero when writing to the next column
                row = 0

                worksheet.write(row, column, header)

                row += 1

                for data in st_data[header]:

                    worksheet.write(row, column, data)

                    row += 1

                column += 1

        # file should be closed
        workbook.close()

    except Exception as error:

        print (Fore.RED + "Error: Could not convert long-term data to excel file!\n" + str(error))


# this method convert data to anually excel data
def ct_anually_excel(st_data={}, path=None):

    try:

        # creating an excel file
        workbook = xlsxwriter.Workbook(path + "\\anually-data" + datetime.today()
                                           .strftime("%Y-%m-%d-%H-%M") + ".xlsx")

        global row
        column = 0

        for st_name in st_data.keys():

            worksheet = workbook.add_worksheet(st_name.capitalize())

            for var in headers_name:

                if var in st_data[st_name].keys():

                    row = 0

                    worksheet.write(row, column, var)

                    row += 1

                    for data in st_data[st_name][var]:

                        worksheet.write(row, column, data)

                        row += 1

                    column += 1

            row = 0
            column = 0

        workbook.close()

    except Exception as error:

        print(Fore.RED + "Error: Could not convert anually data to excel file!\n" + str(error))


# this method convert data to monthly excel data
def ct_monthly_excel(st_data={}, path=None):

    try:

        # creating an excel file
        workbook = xlsxwriter.Workbook(path + "\\monthly-data" + datetime.today()
                                           .strftime("%Y-%m-%d-%H-%M") + ".xlsx")

        global row
        column = 0
        row = 0

        for st_name in st_data.keys():

            worksheet = workbook.add_worksheet(st_name.capitalize())

            for header in month_names:

                worksheet.write(row, 0, header)

                row += 1

            row = 0
            column = 1

            for var in st_data[st_name].keys():

                worksheet.write(row, column, var)

                row += 1

                for data in st_data[st_name][var]:

                    worksheet.write(row, column, data)

                    row += 1

                column += 1
                row = 0

        workbook.close()

    except Exception as error:

        print(Fore.RED + "Error: Could not convert monthly data to excel file!\n" + str(error))


# this method convert data to full data excel files
def ct_fulldata_excel(st_data={}, path=None):

    try:

        row = 0
        column = 0

        for st_name in st_data.keys():

            workbook = xlsxwriter.Workbook(path + "\\fulldata-" + st_name.capitalize() +
                                           datetime.today().strftime("%H-%M") + ".xlsx")

            for var in st_data[st_name].keys():

                worksheet = workbook.add_worksheet(var)

                for list_2d in st_data[st_name][var]:

                    for data in list_2d:

                        worksheet.write(row, column, data)

                        column += 1

                    row += 1
                    column = 0

                column = 0
                row = 0

    except Exception as error:

        print(Fore.RED + "Error: Could not convert full data to excel file!\n" + str(error))
