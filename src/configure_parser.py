"""
Contains methods for configuring command line argument parsing using built-in module argparse
"""
import argparse


def std_argparser():
    """
    Reads in arguments using a standard parser and verifies they're the correct format

    This expects the input arguments to be an arbitrary number of .txt files containing NOAA Best Track Data (HURDAT2)
    :return: arguments
    """
    parser = argparse.ArgumentParser(description='Identify hurricanes that made landfall in Florida since 1900')
    parser.add_argument('hdata', help='Names of the HURDAT2 files to be processed',
                        type=str, nargs='+')
    parser.add_argument('--v', help='Whether or not to print verbosely', action='store_true')
    parser.add_argument('--dir', help='Specify the output directory', type=str, default='output')
    parser.add_argument('--save', help='Specify the file save name', type=str, default='florida_landfall_windspeeds')
    args = parser.parse_args()

    return args
