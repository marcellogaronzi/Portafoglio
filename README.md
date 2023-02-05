# Portafoglio

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat)
![Build Status](https://img.shields.io/badge/Status-Develop-lightgreen?style=flat)
![Version](https://img.shields.io/badge/Version-v2.0-red?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightblue.svg?style=flat)

Python app to download stock prices from [yahoo finance](https://finance.yahoo.com/) and convert them into csv, json and
yaml. Stock and period of prices are selectable, as for interval.

![](https://images.unsplash.com/photo-1642790551116-18e150f248e3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=700&q=80)

## Requirements

Some things that you may need to install in order to run correctly the app.

- python 3.9: you can download python 3.9.13 interpreter
  from [here](https://www.python.org/downloads/release/python-3913/)
- pipenv: it's a packaging tool for python, used to resolve packages. You can install it with:
  ```commandline
  pip install pipenv
  ```

## Installation

After downloading the source files be sure to install all packages and their dependencies with:

```commandline
pipenv install
```

## Execution

- Windows
  ```commandline
  pipenv run python main.py
  ```
  or
  ```commandline
  pipenv shell
  python main.py
  ```

- Linux
  ```commandline
  pipenv run python3 main.py
  ```
  or
  ```commandline
  pipenv shell
  python3 main.py
  ```

This app has different running modes, you can choose between them. The default mode downloads data of `PIRC.MI` (
Pirelli) and generates 3 files: one for CSV format, one for JSON and one for YAML.

## Contributing

You're free to fork the repository and collaborate. A pull request may be needed in order to apply your changes.
¯\_(ツ)_/¯

[https://github.com/marcellogaronzi/Portafoglio.git](https://github.com/marcellogaronzi/Portafoglio.git)

## Testing

The following tests can be run using the doctest library in Python to verify the correctness and functionality of all functions.

Run the tests with the command:
```commandline
python -m dotenv README.md
```

This will run the tests and report any failures to the console. Empty output means everything has gone well. You can add `-v` to the command in order to see single test results.

For more information on the doctest library, please see the official Python documentation: [https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html)

**Tests:**

```python
# file: scripts/get_stock.py

>>> from scripts.get_stock import get_stock
>>> from datetime import datetime
>>> get_stock("PIRC.MI", datetime(2022, 1, 15), datetime(2022, 1, 20), "1d", print, print)
Date,Open,High,Low,Close,Adj Close,Volume
2022-01-17,6.676000,6.730000,6.628000,6.628000,6.391600,1446547
2022-01-18,6.612000,6.616000,6.500000,6.550000,6.316382,1843261
2022-01-19,6.550000,6.600000,6.534000,6.568000,6.333740,976130

>>> get_stock("INVALID STOCK", datetime(2022, 1, 15), datetime(2022, 1, 20), "1d", print, print)
404

```

```python
# file scripts/csv_to_dict.py

>>> from scripts.csv_to_dict import csv_to_dict

>>> csv_to_dict("out/PIRC.MI/PIRC.MI.csv")
{1: {'Date': '2022-02-16', 'Open': '6.002000', 'High': '6.060000', 'Low': '5.860000', 'Close': '5.868000', 'Adj Close': '5.658707', 'Volume': '1735712'}, 2: {'Date': '2022-03-16', 'Open': '4.740000', 'High': '4.940000', 'Low': '4.713000', 'Close': '4.902000', 'Adj Close': '4.727161', 'Volume': '4326966'}, 3: {'Date': '2022-05-16', 'Open': '4.704000', 'High': '4.740000', 'Low': '4.610000', 'Close': '4.706000', 'Adj Close': '4.538152', 'Volume': '885772'}, 4: {'Date': '2022-06-16', 'Open': '4.181000', 'High': '4.203000', 'Low': '4.010000', 'Close': '4.030000', 'Adj Close': '4.030000', 'Volume': '1378418'}, 5: {'Date': '2022-08-16', 'Open': '4.311000', 'High': '4.315000', 'Low': '4.245000', 'Close': '4.275000', 'Adj Close': '4.275000', 'Volume': '1613160'}, 6: {'Date': '2022-09-16', 'Open': '3.711000', 'High': '3.764000', 'Low': '3.676000', 'Close': '3.728000', 'Adj Close': '3.728000', 'Volume': '2664565'}, 7: {'Date': '2022-11-16', 'Open': '4.171000', 'High': '4.175000', 'Low': '4.070000', 'Close': '4.120000', 'Adj Close': '4.120000', 'Volume': '1865038'}, 8: {'Date': '2022-12-16', 'Open': '4.051000', 'High': '4.077000', 'Low': '3.984000', 'Close': '3.994000', 'Adj Close': '3.994000', 'Volume': '2113833'}, 9: {'Date': '2023-01-16', 'Open': '4.613000', 'High': '4.666000', 'Low': '4.578000', 'Close': '4.640000', 'Adj Close': '4.640000', 'Volume': '1141934'}}

```

```python
# file scripts/code_metrics.py

>>> from scripts.code_metrics import calculate_code_metrics

>>> calculate_code_metrics("scripts/code_metrics.py")
{'filename': 'scripts/code_metrics.py', 'nloc': 9, 'function_list': [{'cyclomatic_complexity': 2, 'nloc': 8, 'token_count': 57, 'name': 'calculate_code_metrics', 'long_name': 'calculate_code_metrics( filePath )', 'start_line': 4, 'end_line': 15, 'full_parameters': ['filePath'], 'filename': 'scripts/code_metrics.py', 'top_nesting_level': 0, 'fan_in': 0, 'fan_out': 0, 'general_fan_out': 0}], 'token_count': 60}

```

## Contributors

- Bonomo Giovanni ([19036@studenti.marconiverona.edu.it](mailto:19036@studenti.marconiverona.edu.it))
- Garonzi Marcello ([19067@studenti.marconiverona.edu.it](mailto:19067@studenti.marconiverona.edu.it))
- Mazzurana Riccardo ([19118@studenti.marconiverona.edu.it](mailto:19118@studenti.marconiverona.edu.it))
- Serratore Federico ([19169@studenti.marconiverona.edu.it](mailto:19169@studenti.marconiverona.edu.it))

