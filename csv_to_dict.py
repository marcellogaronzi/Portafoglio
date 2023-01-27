import csv

def csv_to_dict():
    data = {}
    with open("csv/result.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i, row in enumerate(csv_reader):
            data[i+1] = row

    return data
