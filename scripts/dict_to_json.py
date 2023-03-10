#!python3

import json


def dict_to_json(data, filepath):
    """
    Converts a dict into json format and saves it on a file

        Parameters:
            data (dict): data to convert
            filepath (str): path to .json file
    """
    with open(filepath, 'w', newline="\n") as json_outputFile:
        json_outputFile.write(json.dumps(data, indent=4))
