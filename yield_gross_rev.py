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


def read_file(file_path):
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
    # A-Z           > pass
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

    p_line = read_file(products)
    s_line = read_file(sales)
    for prod_line, sale_line in zip(p_line, s_line):
        units = calc_total_units(sale_line[3], prod_line[3])
        out_line = f'{prod_line[1]},{calc_gross_revenue(prod_line[2], units)},{units}'
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
    return open(f'{directory}/files/{name}', "w+")


if __name__ == '__main__':

    # Create the Logger
    LOGGER = logging.getLogger(__name__)
    LOGGER.setLevel(logging.WARNING)
    LOG_HANDLER = logging.FileHandler('gross_rev_log.log')
    LOG_HANDLER.setLevel(logging.WARNING)
    LOG_FORMATTER = logging.Formatter('%(asctime)s : %(name)s - %(levelname)s - %(message)s')
    LOG_HANDLER.setFormatter(LOG_FORMATTER)
    LOGGER.addHandler(LOG_HANDLER)
    LOGGER.info('Completed configuring logger()!')

    CURRENT_DIR = os.getcwd()
    FILE_HEADER = 'Name,GrossRevenue,TotalUnits\n'

    if len(sys.argv) == 4:
        P_FILE, S_FILE, OUT_FILE = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        sys.exit('There was an error in the length of your arguments')
    try:
        OUT_LINE = process_files(P_FILE, S_FILE)
        REPORT_FILE = open_file(CURRENT_DIR, OUT_FILE)
        REPORT_FILE.write(FILE_HEADER)
        for line in OUT_LINE:
            if line:
                print(line)
                REPORT_FILE.write(line + '\n')
                LOGGER.warning(f'WRITING:{line}>>{REPORT_FILE}')
            else:
                REPORT_FILE.close()
                break
    except Exception as error:
        print(f'MAIN ERROR : {error}')
        LOGGER.exception(error)
        sys.exit(f'{error} : Plese see the logs')
