
#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
TESTING FOR BIGRAM FROM FILE PARSING
: DOCS : https://docs.python.org/3/library/unittest.html
"""

import os
import re
import sys
import logging
from decimal import Decimal
import unittest

from . import yield_gross_rev

PRODUCT_FILE = os.getcwd() + '/files/product_file.txt'
SALES_FILE = os.getcwd() + '/files/sales_file.txt'

YEILD_EXPECTED = """Name,GrossRevenue,TotalUnits
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
        self.assertIsInstance('', str)

    def test_is_dict(self):
        """
        test that the input is a dict
        """
        self.assertIsInstance('', dict)

    def test_is_list(self):
        """
        test that the input is a dict
        """
        self.assertIsInstance('', list)

    def test_expected_output(self):
        """
        test to see if the nltk returned object is the same as our expect ouput from the sample
        """
        self.assertEqual('', '')

    def test_len_input(self):
        """
        test that the number of words + 1
        that we find are equal to the number of bigrams
        """
        self.assertEqual('', '')

    def test_sum_bigrams(self):
        """
        test that the total count of bigrams found equals the total count of frequencies
        this should fail as we know there are LTR marks \u200e
        """
        self.assertEqual('', '')

    # def approach_delta(self):
    #     """
    #     compare the ouput of the nltk and non-nltk appraoches for funnzies and behavior notes
    #     """
    #     self.assert(nltk, non - nltk, msg=None)
    #
    #     # OR
    #     # assertDictEqual(expected, actual, msg=None)

if __name__ == '__main__':
    unittest.main()
