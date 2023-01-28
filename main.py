import os
from datetime import datetime

# functions imports
from scripts.get_stock import get_stock
from scripts.csv_to_dict import csv_to_dict
from scripts.dict_to_json import dict_to_json
from scripts.dict_to_yaml import dict_to_yaml

__author__ = ["Bonomo Giovanni", "Garonzi Marcello",
              "Mazzurana Riccardo", "Serratore Federico"]
__copyright__ = "Copyright 2023"
__version__ = "1.0.0"
__maintainer__ = ["Bonomo Giovanni", "Garonzi Marcello",
                  "Mazzurana Riccardo", "Serratore Federico"]
__email__ = ["19036@studenti.marconiverona.edu.it",
             "19067@studenti.marconiverona.edu.it", "19118@studenti.marconiverona.edu.it", "19169@studenti.marconiverona.edu.it"]


def check_out_dir():
    """
    check /out/ directory existance
    """

    dir_path = os.path.join(os.path.dirname(__file__), "out")
    print(f"   ---Dir_path: {dir_path}")
    if (not os.path.exists(dir_path)):
        print("   ---Create /out/ directory")
        os.mkdir(dir_path)
    else:
        print(f"   ---Directory /out/ already exists")


def on_success(stock_data):
    """
    Handles download success

        Parameters:
            stock_data (str): csv data
    """
    print("---Data downloaded\n")

    # Write csv file
    with open("out/result.csv", "w") as csv:
        csv.write(stock_data)

    # .csv to dict converter
    print("---Convert .csv file to dict")
    data = csv_to_dict("out/result.csv")
    print("---Dict obtained succesfully\n")

    # dict to .yaml converter
    print("---Convert dict to .json")
    dict_to_json(data, "out/result.json")
    print("---.json file created succesfully\n")

    # dict to .json converter
    print("---Convert dict to .yaml")
    dict_to_yaml(data, "out/result.yaml")
    print("---.yaml file created succesfully\n")

    print("---Conversions completed")


def on_error(error):
    """
    Handles download error
    """
    print("---Unable to download data. HTTP returned", error)


def etl(stock, start, end, interval, success, error):
    """
    Downloads stock data and generates 3 files: csv, json and yaml

        Parameters:
            stock (str): Stock name
            start (datetime): Start date of period
            stop (datetime): End date of period (default is today)
            interval (str): Type of interval (1mo, 1wk, 1d)
            success (lambda): Success callback
            error (lambda): Error callback
    """
    # out dir check
    print("---Check output directory")
    check_out_dir()
    print("---Check completed\n")

    # yahoo API call
    print("---Download data from yahoo finance API")
    get_stock(stock, start, end, interval, success, error)


def main():
    def mode_0():
        global stock, start, end, interval

        print("-------------------------------------------")
        print("---Pirelli & C. S.p.A MOTHLY STOCK PRICES")
        print("-------------------------------------------\n")

        stock = "PIRC.MI"
        start = datetime(2022, 1, 23, 7, 36, 43)
        end = datetime(2023, 1, 23, 7, 36, 43)
        interval = "1mo"

    def mode_1():
        global stock, start, end, interval
        
        stock = input("Stock name: ")
        start = datetime(*map(int, input("Start date [yyyy-mm-dd]: ").strip().split("-")))
        end = datetime(*map(int, input("End date [yyyy-mm-dd]: ").strip().split("-")))
        interval = input("Interval [1mo, 1wk, 1d]: ")

    # User choice
    default = input("Run in default mode [y/n]? ").lower() != "n"
    print()

    # Set request params
    if default:
        mode_0()
    else:
        mode_1()
        
    # Run ETL (download + conversion)
    success = on_success
    error = on_error
    etl(stock, start, end, interval, success, error)


if __name__ == "__main__":
    main()
