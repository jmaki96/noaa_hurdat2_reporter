from enum import Enum
from datetime import datetime

class RecordID(Enum):
    CLOSEST_APPROACH = 'C'
    GENESIS = 'G'
    INTENSITY_PEAK = 'I'
    LANDFALL = 'L'
    MINIMUM_PRESSURE = 'P'
    RAPID_CHANGE = 'R'
    STATUS_CHANGE = 'S'
    TRACK = 'T'
    MAXIMUM_WINDSPEED = 'W'
    STANDARD_SYNOPTIC = ''


class SystemStatus(Enum):
    TROPICAL_CYCLONE_DEPRESSION = 'TD'
    TROPICAL_CYCLONE_STORM = 'TS'
    TROPICAL_CYCLONE_HURRICANE = 'HU'
    EXTRATROPICAL_CYCLONE = 'EX'
    SUBTROPICAL_CYCLONE_DEPRESSION = 'SD'
    SUBTROPICAL_CYCLONE_STORM = 'SS'
    LOW_CYCLONE = 'LO'
    TROPICAL_WAVE = 'WV'
    DISTURBANCE = 'DB'


class BestTrackEntry:
    """
    A BestTrackEntry is a piece of information that records some event related to its master Hurricane.

    As specified by the HURDAT2 standard. A BestTrackEntry has:
        -Date (a datetime object precise to the minute)
        -Record ID (a record ID enum)
        -System status (a system status enum)
        -Latitude
        -Longitude
        -Maximum sustained windspeed (in knots)
        -Maximum pressure (in millibars)
        -34kt wind radii maximum extent in the format [NE, SE, SW, NW] (in nautical miles)
        -50kt wind radii maximum extent in the format [NE, SE, SW, NW] (in nautical miles)
        -60kt wind radii maximum extent in the format [NE, SE, SW, NW] (in nautical miles)
    """

    def __init__(self, data_row):
        """
        A BestTrackEntry takes in a HURDAT2 data row to build itself

        :param data_row: A HURDAT2 data row as specified by the NOAA
        """
        entry = data_row[0]
        year = int(entry[0:4])
        month = int(entry[4:6])
        day = int(entry[6:8])
        entry = data_row[1]
        hour = int(entry[0:3])
        minute = int(entry[3:5])
        self.date = datetime(year, month, day, hour, minute)
        self.rec_ID = RecordID(data_row[2].lstrip())
        self.status = SystemStatus(data_row[3].lstrip())
        self.lat = data_row[4].lstrip()
        self.long = data_row[5].lstrip()
        self.max_speed = int(data_row[6])
        self.max_pressure = int(data_row[7])
        self.low_kt = []
        for wind_radii in data_row[8:12]:
            self.low_kt.append(int(wind_radii))
        self.med_kt = []
        for wind_radii in data_row[12:16]:
            self.med_kt.append(int(wind_radii))
        self.high_kt = []
        for wind_radii in data_row[16:20]:
            self.high_kt.append(int(wind_radii))

    def __str__(self):
        return "DATE: {0} \nREC_ID: {1} \nSTATUS: {2}\nLATITUDE: {3} LONGITUDE: {4}\nMAX_SPEED: {5} (knots) " \
               "MAX_PRESSURE: {6} (millibars)\n34 KT: \n    NE: {7} (nautical miles)\n    SE: {8} (nautical miles)" \
               "\n    SW: {9} (nautical miles)\n    NW: {10} (nautical miles) " \
               "\n50 KT: \n    NE: {11} (nautical miles)\n    SE: {12} (nautical miles)" \
               "\n    SW: {13} (nautical miles)\n    NW: {14} (nautical miles)" \
               "\n64 KT: \n    NE: {15} (nautical miles)\n    SE: {16} (nautical miles)" \
               "\n    SW: {17} (nautical miles)\n    NW: {18} (nautical miles)".format(self.date, self.rec_ID.name,
                                                                                       self.status.name,
                                                                                       self.lat, self.long, self.max_speed,
                                                                                       self.max_pressure, self.low_kt[0],
                                                                                       self.low_kt[1], self.low_kt[2],
                                                                                       self.low_kt[3], self.med_kt[0],
                                                                                       self.med_kt[1], self.med_kt[2],
                                                                                       self.med_kt[3], self.high_kt[0],
                                                                                       self.high_kt[1], self.high_kt[2],
                                                                                       self.high_kt[3])
