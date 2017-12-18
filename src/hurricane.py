from src.best_track_entry import BestTrackEntry


class Hurricane:
    """
    This class represents a Hurricane.

    As specified by the HURDAT2 standard. A Hurricane has:
        -Basin
        -ATCF Cyclone Number
        -Year of formation (or genesis)
        -Name
        -Best Track Entries
    """

    def __init__(self, header_row):
        """
        A Hurricane takes in a HURDAT2 header row to build itself

        :param header_row: a HURDAT2 header row as specified by the NOAA
        """
        entry = header_row[0]
        self.basin = entry[0:2]
        self.cyc_no = entry[2:4]
        self.year = entry[4:8]
        entry = header_row[1]
        self.name = entry.lstrip()
        entry = header_row[2]
        self.max_entries = int(entry)
        self.entries = []

    def add_entry(self, data_row):
        """
        Takes in a HURDAT2 data row to build and append a BestTrackEntry

        Throws AttributeError if an entry is added that would exceed the maximum number of entries for this storm
        :param data_row: a HURDAT2 data row as specified by the NOAA
        """

        if len(self.entries) == self.max_entries:
            raise AttributeError('Maximum number of entries for {0} is {1}!'.format(self.name, self.max_entries))
        else:
            entry = BestTrackEntry(data_row)
            self.entries.append(entry)

    def __str__(self):
        return "{0}\nYEAR: {1}\nBASIN: {2} \nATCF CYCLONE NUMBER: {3}\nNUM ENTRIES: {4}\n".format(self.name, self.year,
                                                                                                  self.basin,
                                                                                                  self.cyc_no,
                                                                                                  len(self.entries))

