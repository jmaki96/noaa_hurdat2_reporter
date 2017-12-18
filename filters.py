"""
This includes all filters that might be used to filter Hurricane objects

All filters take in a list of Hurricane objects and produce a filtered list of Hurricane objects, they can take in
additional arguments if needed
"""
from src.best_track_entry import RecordID


def made_landfall(entry, state):
    """
    Determines if this entry indicates that a hurricane has made landfall in a given state

    :param entry: a BestTrackEntry
    :param state: The string name of a state (currently only supports Florida)
    :return: True if this entry made landfall in the given state, False otherwise
    :raises: KeyError for any non-supported state
    """
    if entry.rec_ID != RecordID.LANDFALL:
        return False
    if state == 'Florida':
        florida_hemisphere_NS = 'N'
        florida_hemisphere_EW = 'W'
        # From google Maps
        florida_max_lat = 30.7
        florida_min_lat = 24.5
        florida_max_long = 87.5
        florida_min_long = 80.0
        lat = entry.lat
        long = entry.long
        if lat[-1:] != florida_hemisphere_NS:
            print(lat[-1:])
            return False
        if long[-1:] != florida_hemisphere_EW:
            print(long[-1:])
            return False
        if not (florida_min_lat <= float(lat[:-1]) <= florida_max_lat):
            return False
        if not (florida_min_long <= float(long[:-1]) <= florida_max_long):
            return False
    else:
        raise KeyError("{0} is not currently a supported state")

    return True


def landfall_filter(hurricanes, state):
    new_hurricanes = []
    for hurricane in hurricanes:
        for entry in hurricane.entries:
            if made_landfall(entry, state):
                new_hurricanes.append(hurricane)
                break
    return new_hurricanes


def date_filter(hurricanes, date):
    new_hurricanes = []
    for hurricane in hurricanes:
        for entry in hurricane.entries:
            if entry.date > date:
                new_hurricanes.append(hurricane)
                break

    return new_hurricanes

