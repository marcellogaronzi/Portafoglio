#!python3

import yaml


def dict_to_yaml(dictionary, filepath):
    """
    Converts a dict into yaml format and saves it on a file

        Parameters:
            dictionary (dict): data to convert
            filepath (str): path to file
    """
    with open(filepath, 'w') as outfile:
        yaml.dump(dictionary, outfile)
