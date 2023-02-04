#!python3

import time  # to show time execution

import scripts.core as core

__author__ = ["Bonomo Giovanni", "Garonzi Marcello", "Mazzurana Riccardo", "Serratore Federico"]
__copyright__ = "Copyright 2023"
__version__ = "2.0.0"
__maintainer__ = ["Bonomo Giovanni", "Garonzi Marcello", "Mazzurana Riccardo", "Serratore Federico"]
__email__ = ["19036@studenti.marconiverona.edu.it",
             "19067@studenti.marconiverona.edu.it",
             "19118@studenti.marconiverona.edu.it",
             "19169@studenti.marconiverona.edu.it"]


def function3():
    core.select_modality(True, False, True)


def function4():
    core.select_modality(True, True, False)


def function5():
    core.select_modality(False, False, True)


def function6():
    core.select_modality(False, True, False)


def inizializzazioneDiz():
    dict = {
        "1": {
            "default mode": core.default_mode,
        },
        "2": {
            "manual mode": core.manual_mode,
        },
        "3": {
            "default mode to yaml only": function3,
        },
        "4": {
            "default mode to json only": function4,
        },
        "5": {
            "manual mode to yaml only": function5,
        },
        "6": {
            "manual mode to json only": function6,
        },
        "7": {
            "Clear output directory": core.clear_output_directory
        }
    }
    return dict


def callback(dict):
    listaKey = dict.keys()
    scelta = 'Null'
    while scelta not in listaKey:

        print("--- Dominio scelte ---")

        for key in listaKey:
            print(f'{key}: {list(dict[key])[0]}')

        scelta = input("Choice: ").strip()
    print(f'key: {scelta}-> value: {list(dict[scelta])[0]}\n')

    return dict[scelta][list(dict[scelta])[0]]


def main():
    app = inizializzazioneDiz()
    function = callback(app)

    continue_choice = True
    while continue_choice:
        start_clock_time = time.process_time()
        start_time = time.time()

        function()

        print(f"---Total Time Execution: {round(time.time() - start_time, 3)} s")
        print(f"---Total CPU Time: {time.process_time() - start_clock_time} s")

        choice = input("\n\nChoose another option [y/n]? ").strip().lower() == 'y'
        if (not choice):
            return

        function = callback(app)


if __name__ == "__main__":
    main()
