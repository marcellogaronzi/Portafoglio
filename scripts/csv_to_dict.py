#!python3

import csv


def csv_to_dict(filepath):
    """
    Converts a .csv file into a key/value dictionary.

        Returns:
            data (dict): dictionary
    """
    data = {}
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            data[i + 1] = row

    return data
