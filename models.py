#!/usr/bin/env python

"""
Models for info if needed
"""


class Product:
    """
    A class for
     ProductId – an integer uniquely identifying the Product
     Name – a string name for the Product
     Price – a floating point price at which the Product is sold (per unit, not per lot)
     LotSize – an integer representing how many of the product are sold in a single lot

    The numerical fields may be assumed to be positive.
    The string fields are not quoted and may be assumed not
    to contain commas or non-ASCII characters.
    The file does not contain a header. An example file is as follows:
    """

    def __init__(self, product_id, name, price, lot_size):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.lot_size = lot_size


class Sales:
    """
    The Sales file is a comma-separated text file where
    each line contains information about a unique sale.
    The fields of the file are as follows:

     SaleId – an integer uniquely identifying the sale
     ProductId – an integer identifying the Product (matches the ProductId from the Product Master)
     TeamId – an integer identifying the Sales Team (matches the TeamId from the Team Map)
     Quantity – an integer representing how many lots of the product were sold

    All of the numerical fields may be assumed to be positive.
    The file does not contain a header with the field names. An example file is as follows:
    """

    def __init__(self, sale_id, product_id, team_id, quantity):
        self.sale_id = sale_id
        self.product_id = product_id
        self.team_id = team_id
        self.quantity = quantity


class Report:
    """
    Product Report
    The Product Report file is a comma-separated text file where each line summarizes the
    sales of a single Product and contains four values as follows:

     Name – name of the Product
     GrossRevenue – gross revenue of sales of the Product
     TotalUnits – total number of units sold in the Product

    The file should contain a header with the field names, and the products
    should be provided in descending order of their gross revenue.
    """

    def __init__(self, name, gross_revenue, total_units):
        self.name = name
        self.gross_revenue = gross_revenue
        self.total_units = total_units
