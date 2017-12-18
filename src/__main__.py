import os
from datetime import datetime
from src.configure_parser import std_argparser
from src.configure_logger import configure_stdout_logger
from src.read_csv import read_hurdat2
from src.write_csv import write_csv
from src import filters


def main():

    """
    Step 1: Configure logger
    """
    logger = configure_stdout_logger()

    """
    Step 2: Parse arguments
    """
    logger.info("Parsing arguments...")
    args = std_argparser()
    hdata_files = []
    for file in args.hdata:
        if not file.endswith('.txt'):
            logger.error("File {0} is not a valid file format".format(file))
            return 1
        else:
            hdata_files.append(file)
    logger.info("Done.")

    """
    Step 3: Parse each file into some useful format
    Note: Here we have to assume each file is following the HURDAT2 standard. Any files that break standard will be
    discarded, and the logger will note this.
    """
    logger.info("Beginning to read csvs...")
    hurricanes = []
    for file in hdata_files:
        logger.info("Reading {0}".format(file))
        hurricanes.extend(read_hurdat2(file))
    if args.v:
        print(len(hurricanes))
    logger.info("Done.")

    """
    Step 4: Extract relevant entries into a new list
    """
    logger.info("Beginning to filter storms...")
    logger.info("Filtering by landfall in Florida")
    hurricanes = filters.landfall_filter(hurricanes, 'Florida')
    if args.v:
        print(len(hurricanes))
    logger.info("Filtering by date past 1900")
    hurricanes = filters.date_filter(hurricanes, date=datetime(1900, 1, 1, 1, 1))
    if args.v:
        print(len(hurricanes))
    logger.info("Done.")

    """
    Step 5: Generate report
    """
    OUTPUT_FILENAME = "florida_landfall_hurricanes.csv"
    OUTPUT_DIRECTORY = os.path.abspath("output")
    logger.info("Writing filtered hurricane events to {0}...".format(os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILENAME)))
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.mkdir(OUTPUT_DIRECTORY)
    write_csv(hurricanes, os.path.join(OUTPUT_DIRECTORY, "florida_landfall_hurricanes.csv"))
    logger.info("Done.")


if __name__ == "__main__":
    main()
