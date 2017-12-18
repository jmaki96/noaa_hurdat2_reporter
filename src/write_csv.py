"""
This contains all functions for writing out data to a csv
"""
import csv
from src.filters import made_landfall


def write_csv(hurricanes, filename):
    """
    Writes out all hurricanes as specified in the KCC case study to a csv

    Format: NAME DATE_OF_LANDFALL MAX_WIND_SPEED
    :param hurricanes: a list of filtered Hurricane objects
    :param filename: name of csv to write too
    """

    with open(filename, 'w', newline='') as csvfile:
        hurricane_writer = csv.writer(csvfile, delimiter=',', dialect='excel')
        hurricane_writer.writerow(['NAME', 'DATE OF LANDFALL', 'MAX WIND SPEED (knots)'])
        for hurricane in hurricanes:
            for entry in hurricane.entries:
                if made_landfall(entry, 'Florida'):
                    hurricane_writer.writerow([hurricane.name, entry.date, entry.max_speed])
