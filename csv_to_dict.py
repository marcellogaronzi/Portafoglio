import csv

def csv_to_dict():
    with open("csv/result.csv", "r") as f:
        dict_reader = csv.DictReader(f)
        dict = list(dict_reader)
    
    return dict
