import csv

def csv_to_dict():
    """
    Convverts a .csv file into a key/value dictionary.
    
    Returns:
    -data: dictionary
    """   
    data = {}
    with open("out/result.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            data[i+1] = row

    return data
