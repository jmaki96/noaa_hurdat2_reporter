"""
Contains functions for reading various csv formats
"""
import csv
from src.hurricane import Hurricane


def check_header(row):
    """
    Parses a row and checks to see if it is a HURDAT2 Header Row

    Only checks that the entries are there, and the correct length so as to distinguish from a data row. Correct
    HURDAT2 formatting is assumed.
    :param row: A row read from a HURDAT2 csv
    :return: True if this is a header row, False otherwise
    """

    # A HURDAT header row has 3 entries, but the trailing ',' adds a fourth entry for the newline.
    # This first entry is 8 characters long (spaces 1-8)
    # The second entry is 19 characters long (spaces 9-28)
    # The third entry is 7 characters long  (spaces 29-36)
    # The final entry is the trailing ',' and should be empty
    return len(row) == 4 and len(row[0]) == 8 and len(row[1]) == 19 and len(row[2]) == 7 and len(row[3]) == 0


def read_hurdat2(filename):
    """
    Parses the HURDAT2 from the file into a list of Hurricanes

    Assumes that the csv is in the correct HURDAT2 format
    :param filename: the name of the csv
    :return: a list of Hurricanes
    """
    hurricanes = []
    hurricane  = None
    with open(filename, newline='') as csvfile:
        hur_reader = csv.reader(csvfile, delimiter=',')
        for row in hur_reader:
            if check_header(row):
                if hurricane is not None:
                    hurricanes.append(hurricane)
                hurricane = Hurricane(row)
            else:
                hurricane.add_entry(row)
        hurricanes.append(hurricane)

    return hurricanes



