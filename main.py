#!python3

import time  # to show time execution

import scripts.core as core

__author__ = ["Bonomo Giovanni", "Garonzi Marcello",
              "Mazzurana Riccardo", "Serratore Federico"]
__copyright__ = "Copyright 2023"
__version__ = "2.0.0"
__maintainer__ = ["Bonomo Giovanni", "Garonzi Marcello",
                  "Mazzurana Riccardo", "Serratore Federico"]
__email__ = ["19036@studenti.marconiverona.edu.it",
             "19067@studenti.marconiverona.edu.it",
             "19118@studenti.marconiverona.edu.it",
             "19169@studenti.marconiverona.edu.it"]


def function3():
    """Default mode to csv only"""
    core.select_modality(True, False, False)


def function4():
    """Default mode to yaml only"""
    core.select_modality(True, False, True)


def function5():
    """Default mode to json only"""
    core.select_modality(True, True, False)


def function6():
    """Manual mode to csv only"""
    core.select_modality(False, False, False)


def function7():
    """Manual mode to yaml only"""
    core.select_modality(False, False, True)


def function8():
    """Manual mode to json only"""
    core.select_modality(False, True, False)


def inizializzazione_diz():
    """Initializes run options dictionary"""
    dictionary = {
        "1": {
            "default mode": core.default_mode,
        },
        "2": {
            "manual mode": core.manual_mode,
        },
        "3": {
            "default mode to csv only": function3,
        },
        "4": {
            "default mode to yaml only": function4,
        },
        "5": {
            "default mode to json only": function5,
        },
        "6": {
            "manual mode to csv only": function6,
        },
        "7": {
            "manual mode to yaml only": function7,
        },
        "8": {
            "manual mode to json only": function8,
        },
        "9": {
            "Clear output directory": core.clear_output_directory
        }
    }
    return dictionary


def callback(dictionary):
    """
    Launches code modes based on user choice

        Parameters:
            dictionary (dict): options dictionary
    """
    lista_key = dictionary.keys()
    scelta = 'Null'
    while scelta not in lista_key:

        print("--- Domain choices ---")

        for key in lista_key:
            print(f'{key}: {list(dictionary[key])[0]}')

        scelta = input("Choice: ").strip()
    print(f'key: {scelta}-> value: {list(dictionary[scelta])[0]}\n')

    return dictionary[scelta][list(dictionary[scelta])[0]]


def main():
    """Main"""
    app = inizializzazione_diz()
    function = callback(app)

    continue_choice = True
    while continue_choice:
        start_clock_time = time.process_time()
        start_time = time.time()

        function()

        print(
            f"---Total Time Execution: {round(time.time() - start_time, 3)} s")
        print(f"---Total CPU Time: {time.process_time() - start_clock_time} s")

        choice = input(
            "\n\nChoose another option [y/n]? ").strip().lower() == 'y'
        if not choice:
            return

        function = callback(app)


if __name__ == "__main__":
    main()
