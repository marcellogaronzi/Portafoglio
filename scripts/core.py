#!python3

import glob  # to do recursively operations inside the project
import os
import shutil  # to delete folder and its content
from datetime import datetime
from pathlib import Path

from scripts.code_metrics import calculate_code_metrics
from scripts.csv_to_dict import csv_to_dict
from scripts.dict_to_json import dict_to_json
from scripts.dict_to_yaml import dict_to_yaml
# functions imports
from scripts.get_stock import get_stock

CONVERT_TO_YAML = True
CONVERT_TO_JSON = True


def check_out_dir(stock):
    """
    check ../out/ directory existence

        Parameters:
            stock (str): stock name
    """
    global dir_path

    dir_path = os.path.dirname(__file__)
    dir_path = Path(dir_path).parent
    dir_path = os.path.join(dir_path, "out")

    out_folders = [
        os.path.join(dir_path, stock),
        os.path.join(dir_path, "code_metrics")
    ]

    print(f"   ---Dir_path: {dir_path}")
    if not os.path.exists(dir_path):
        print("   ---Create /out/ directory")
        os.mkdir(dir_path)
        for folder in out_folders:
            print(f"   ---Create {folder} directory")
            os.mkdir(folder)
    else:
        print(f"   ---Directory /out/ already exists")

        for folder in out_folders:
            if not os.path.exists(folder):
                print(f"   ---Create {folder} directory")
                os.mkdir(folder)
            else:
                print(f"   ---Directory {folder} already exists")


def clear_output_directory():
    """
    Clears output directory
    """
    # confirm request
    confirm = input(
        "Delete all the files generated [y/n]? ").strip().lower() == "y"

    if confirm:
        folder = 'out/'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            if os.path.isfile(file_path) or os.path.islink(file_path):
                # delete file or link
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # delete folder and all its content
                shutil.rmtree(file_path)


def elaborate_code_metrics_file():
    """
    Calculates and writes code metrics on output file
    """
    print("---Calculate code metrics")
    code_metrics_dict = {}

    for i, filename in enumerate(glob.glob(os.path.dirname(__file__) + "/*.py", recursive=True)):
        code_metrics_dict[i] = calculate_code_metrics(filename)
    print("---Code metrics calculated successfully")

    print("---Write code metrics' results on .json file")
    dict_to_json(code_metrics_dict, f"out/code_metrics/code_metrics.json")
    print("---out/code_metrics/code_metrics.json successfully created\n ")


def on_success(stock_data, stock, interval):
    """
    Handles download success

        Parameters:
            stock_data (str): csv data
            stock (str): stock name
            interval (str): stock data time interval
    """
    print("---Data downloaded\n")

    # get only the 16ths tuple for each month if interval = 1d
    if interval == "1d":
        split_stock = stock_data.split("\n")
        new_stock = split_stock[0] + "\n"

        for row in split_stock:
            if row.split(",")[0].endswith("-16"):
                new_stock += row + "\n"

        stock_data = new_stock

    # Write csv file
    print("---Write .csv file")
    csv_file = f"out/{stock}/{stock}.csv"
    with open(csv_file, "w") as csv:
        csv.write(stock_data)
    print(f"---{csv_file} succesfully created\n")

    # .csv to dict converter
    if CONVERT_TO_JSON or CONVERT_TO_YAML:
        print("---Convert .csv file to dict")
        data = csv_to_dict(csv_file)
        print("---Dict obtained successfully\n")

    # dict to .json converter
    if CONVERT_TO_JSON:
        print("---Convert dict to .json")
        dict_to_json(data, f"out/{stock}/{stock}.json")
        print("---.json file created successfully\n")

    # dict to .yaml converter
    if CONVERT_TO_YAML:
        print("---Convert dict to .yaml")
        dict_to_yaml(data, f"out/{stock}/{stock}.yaml")
        print("---.yaml file created successfully\n")

    # elaborate code metrics with lizard library
    elaborate_code_metrics_file()


def on_error(error):
    """
    Handles download error

        Parameters:
            error (int): HTTP error code
    """
    print("---Unable to download data. HTTP returned", error)


def call_etl(stock, start, end, interval):
    """
    Downloads stock data and generates 3 files: csv, json and yaml

        Parameters:
            stock (str): Stock name
            start (datetime): Start date of period
            end (datetime): End date of period (default is today)
            interval (str): Type of interval (1mo, 1wk, 1d)
    """

    # callbacks
    def success(data): on_success(data, stock, interval)

    def error(e): on_error(e)

    # out dir check
    print("---Check output directory")
    check_out_dir(stock)
    print("---Check completed\n")

    # yahoo API call
    print("---Downloading data from yahoo finance API")
    get_stock(stock, start, end, interval, success, error)


def default_mode():
    """
    Portafoglio core default mode
    """
    print("-------------------------------------------")
    print("---Pirelli & C. S.p.A MOTHLY STOCK PRICES")
    print("-------------------------------------------\n")

    stock = "PIRC.MI"
    start = datetime(2022, 1, 23, 7, 36, 43)
    end = datetime(2023, 1, 23, 7, 36, 43)
    interval = "1d"

    # Run ETL (download + conversion)
    call_etl(stock, start, end, interval)


def manual_mode():
    """
    Portafoglio core user-input mode
    """
    stock = input("Stock name: ")
    start = datetime(
        *map(int, input("Start date [yyyy-mm-dd]: ").strip().split("-")))
    end = datetime(
        *map(int, input("End date [yyyy-mm-dd]: ").strip().split("-")))
    interval = input("Interval [1mo, 1wk, 1d]: ")

    # Run ETL (download + conversion)
    call_etl(stock, start, end, interval)


def select_modality(is_default, convert_to_json, convert_to_yaml):
    """
    Core mode launcher

        Parameters:
            is_default (bool): run in default mode
            convert_to_json (bool): convert to json
            convert_to_yaml (bool): convert to yaml
    """
    global CONVERT_TO_JSON, CONVERT_TO_YAML

    CONVERT_TO_JSON = convert_to_json
    CONVERT_TO_YAML = convert_to_yaml

    if is_default:
        default_mode()
    else:
        manual_mode()


def main():
    """
    Main
    """
    # User choice
    default = input("Run in default mode [y/n]? ").lower() != "n"
    print()

    # Set request params
    if default:
        default_mode()
    else:
        manual_mode()


if __name__ == "__main__":
    main()
