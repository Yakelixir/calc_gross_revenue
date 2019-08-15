#!/usr/bin/env python

"""
### Testing under construction ###

1. collect data from files
2. generate lines and calculate...
    A. TotalUnits
    B. GrossRevenue
3. Create a report file
    A. Check for file and create if not present
    B. Write lines into the file
    C. Close the file when completed
4. Log Everything
"""


def read_lines_gen(file_object):
    """
    Lazy function (generator) to read a file line by line
    """

    while True:
        clean_line = convert_line(file_object.readline())
        if not clean_line:
            file_object.close()
            break
        yield clean_line

def read_file(file_path):
    """
    Load a file
    How do we want to handle this for input?
    # This should be turned into a generator [Future]
    """
    try:
        with open(file_path) as file:
            for out_line in read_lines_gen(file):
                # process line
                yield out_line
    except (IOError, OSError):
        print("Error opening / processing file")


def convert_line(str_line):
    """

    :param str_line:
    :return:
    """
    if str_line:
        out_list = str_line.split('\n')[0].split(',')  # Change file str into list
        counter = 0
        for index in out_list[counter:]:
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


def output_file(directory, name):
    """
    Create a file object to interact with
    create the file if it does not exist with a unique file name

    """
    return open(f'{directory}/files/{name}', "w+")


if __name__ == '__main__':

    import os
    import re
    import sys
    import logging
    from decimal import Decimal

    if len(sys.argv) == 4:
        P_FILE, S_FILE, OUT_FILE = sys.argv[1], sys.argv[2], sys.argv[3]
    else:
        sys.exit('There was an error in the length of your arguments')

    LOG_FILE = ''.join([os.getcwd(), '.log'])
    LOGGER = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG,
                        filename=LOG_FILE,
                        filemode='w+',  # over write for single use currently default is append
                        format='%(asctime)s : %(name)s - %(levelname)s - %(message)s')
    logging.warning('This will get logged to a file')

    CURRENT_DIR = os.getcwd()

    try:
        OUT_LINE = process_files(P_FILE, S_FILE)
        REPORT_FILE = output_file(CURRENT_DIR, OUT_FILE)
        REPORT_FILE.write(f'Name,GrossRevenue,TotalUnits\n')
        for line in OUT_LINE:
            if line:
                REPORT_FILE.write(line + '\n')
            else:
                REPORT_FILE.close()
                break
    except Exception as error:
        print(f'MAIN TRY ERROR : {error}')
        LOGGER.exception(error)
        sys.exit(f'{error} : Plese see the logS')
