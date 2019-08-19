#!/usr/bin/env python

"""
Process...
1. collect data from files
2. generate lines and calculate...
    A. TotalUnits
    B. GrossRevenue
3. Create a report file
    A. Check for file and create if not present
    B. Write lines into the file
4. Log Everything (rough skeleton)

### Testing under construction ###
"""

import os
import re
import sys
import logging
from decimal import Decimal


def read_file_lines(file_path):
    """
    Load a file
    Loop through process_lines generator
    :param file_path:
    :return:
    Yield the output line to be processed
    """
    try:
        with open(file_path) as file:
            for out_line in process_lines(file):
                # processed line from file >
                yield out_line
    except (IOError, OSError):
        print("Error opening file")


def process_lines(file_object):
    """
    Lazy function (generator) to read a file line by line
    Then we user convert_line to check for...
        # A-Z           > pass
        # if '.'        > change to Decimal
        # if neither    > change to int
    """

    while True:
        file_line = file_object.readline()
        if file_line:
            clean_line = convert_line(file_line)
            if not clean_line:
                # This may be needed however the context manager should handle this
                # file_object.close()
                break
            yield clean_line
        else:
            break


def convert_line(raw_line):
    """
    Split up the string on "next line" char and select the first index
    Split on comma to create a list of
    Run through check for...
    # a-z/A-Z       > pass
    # if '.'        > change to Decimal
    # if neither    > change to int
    :param raw_line:
    :return:
    list object with index's prepared for calculation
    """

    out_list = raw_line.split('\n')[0].split(',')  # Change file str into list
    counter = 0
    for index in out_list:
        if re.search('[a-zA-Z]', index):
            pass
        elif '.' in index:
            out_list[counter] = Decimal(index)
        else:
            out_list[counter] = int(index)
        counter += 1
    return out_list


def process_files(products, sales):
    """
    Take in two file generators
    Step them both through calculation
    :param products:
    :param sales:

    :return:
    """

    p_list = list(read_file_lines(products))
    s_line = read_file_lines(sales)
    for sale_data in s_line:
        for prod_data in p_list:
            if sale_data[1] == prod_data[0]:
                units = calc_total_units(sale_data[3], prod_data[3])
                out_line = [prod_data[1], calc_gross_revenue(prod_data[2], units), units]
                # out_line = f'{prod_data[1]},{calc_gross_revenue(prod_data[2], units)},{units}'
                yield out_line


def calc_total_units(quantity, lot_size):
    """
     TotalUnits = Quantity * LotSize
    :param quantity:
    :param lot_size:

    :return:
    TotalUnits
    """

    return quantity * lot_size


def calc_gross_revenue(price, total_units):
    """
     GrossRevenue = Price * TotalUnits
    :param price:
    :param total_units:

    :return:
    GrossRevenue
    """

    return price * total_units


def open_file(directory, name):
    """
    Create a file object to interact with
    w+ : create the file if it does not exist with a unique file name
    :param directory:
    :param name:

    :return:
    File Object
    """
    return open(f'{directory}/{name}', "w+")


def merge_and_sort(rev_list):
    """
    We are going to look for name matches and add
        Gross Revenue
        Total Units
    Then delete the non-merged entry
    Move to next index
    Sorts the list in a descending manner
    """

    counter = 0
    for g_line in rev_list:
        inner_counter = 0
        for g_line_other in rev_list:
            if counter == inner_counter:
                pass
            else:
                if g_line[0] == g_line_other[0]:
                    gross_sum = g_line[1] + g_line_other[1]
                    total_units = g_line[2] + g_line_other[2]
                    rev_list[counter][1] = gross_sum
                    rev_list[counter][2] = total_units
                    del rev_list[inner_counter]

            inner_counter += 1
        counter += 1

    rev_list.sort(key=lambda x: x[1], reverse=True)  # Sort descending

    return rev_list  # Change file str into list


if __name__ == '__main__':

    # Create the Logger
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.WARNING)
    LOG_HANDLER = logging.FileHandler('gross_rev_log.log')
    LOG_HANDLER.setLevel(logging.WARNING)
    LOG_FORMATTER = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
    LOG_HANDLER.setFormatter(LOG_FORMATTER)
    LOGGER.addHandler(LOG_HANDLER)
    LOGGER.info('Logging reporting for total gross revenue')

    if len(sys.argv) == 4:
        P_FILE, S_FILE, OUT_FILE = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        sys.exit('There was an error in the length of your arguments')

    CURRENT_DIR = os.getcwd()
    FILE_HEADER = 'Name,GrossRevenue,TotalUnits\n'

    try:
        PROCESSED_LIST = list(process_files(P_FILE, S_FILE))
        SORTED_FINAL_LIST = merge_and_sort(PROCESSED_LIST)
        REPORT_FILE = open_file(CURRENT_DIR, OUT_FILE)  # CREATE REPORT FILE
        REPORT_FILE.write(FILE_HEADER)  # APPLY FILE HEADER
        LOGGER.warning(f'WRITING : {FILE_HEADER} >> {REPORT_FILE}')
        for g_rev in SORTED_FINAL_LIST:
            line = f'{g_rev[0]},{g_rev[1]},{g_rev[2]}\n'
            REPORT_FILE.write(line)
            LOGGER.warning(f'WRITING : {line} >> {REPORT_FILE}')
        REPORT_FILE.close()
    except Exception as error:
        print(f'{__name__} ERROR : {error}')
        LOGGER.exception(error)
        sys.exit(f'{error} : Plese see the logs')
