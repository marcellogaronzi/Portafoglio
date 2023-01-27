import os

# functions imports
import scripts.get_stock as get_stock
import scripts.csv_to_dict as csv_to_dict
import scripts.dict_to_json as dict_to_json

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


def main():
    print("-------------------------------------------")
    print("---Pirelli & C. S.p.A MOTHLY STOCK PRICES")
    print("-------------------------------------------\n")

    # out dir check
    print("---Check output directory")
    check_out_dir()
    print("---Check completed\n")

    # yahoo API call
    print("---Download data from yahoo finance API")
    get_stock.main()
    print("---Data downloaded\n")

    # .csv to dict converter
    print("---Convert .csv file to dict")
    csv_to_dict.csv_to_dict()
    print("---Dict obtained succesfully\n")

    # dict to .yaml converter

    # dict to .json converter
    print("---Convert dict to .json")
    dict_to_json.dict_to_json()
    print("---.json file created succesfully\n")

    print("---Conversions completed")


if __name__ == "__main__":
    main()
