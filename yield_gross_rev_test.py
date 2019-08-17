
#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
TESTING FOR BIGRAM FROM FILE PARSING
: DOCS : https://docs.python.org/3/library/unittest.html

I will set up basic testing here.
In the essence of time I won't go into exception handling testing

"""

import os
import io
import re
import sys
import logging
from decimal import Decimal
import unittest

from . import yield_gross_rev as ygr

PRODUCT_FILE = os.getcwd() + '/files/product_file.txt'
SALES_FILE = os.getcwd() + '/files/sales_file.txt'

PRODUCT_EXPECTED = """
1,Minor Widget,0.25,250
2,Critical Widget,5.00,10
3,Complete System (Basic),500,1
4,Complete System (Deluxe),625,1
"""

SALES_EXPECTED = """
1,1,2,10
2,1,1,1
3,2,1,5
4,3,4,1
5,3,5,2
"""

YIELD_EXPECTED = """
Name,GrossRevenue,TotalUnits
Minor Widget,625.00,2500
Critical Widget,50.00,10
Complete System (Basic),2500,5
Complete System (Deluxe),625,1
"""



class TestbigramParse(unittest.TestCase):
    """
    Testing for bigramft.py and bgparse.py
    """

    def test_is_str(self):
        """
        test that the input is a str
        """
        self.assertIsInstance(ygr., str)

    def test_is_dict(self):
        """
        test that the input is a dict
        """
        self.assertIsInstance('', dict)

    def test_is_list(self):
        """
        test that the input is a list
        """
        self.assertIsInstance('', list)

    def test_expected_output(self):
        """
        test to see if the returned object is the same as our expect output
        """
        self.assertEqual('', '')

    def test_len_input(self):
        """
        test that the number + 1
        """
        self.assertEqual('', '')

    def test_reading_of_data_from_file(self):
        """

        :return:
        """
        testStream = io.StringIO()
        testStream.write('')
        testStream.seek(0)
        assert('T.M.', readInitialsFromFileStream(testStream))

    def test_writing_of_data_to_file(self):
        """

        :return:
        """

if __name__ == '__main__':
    unittest.main()
