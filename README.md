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

## Contributors

- Bonomo Giovanni ([19036@studenti.marconiverona.edu.it](mailto:19036@studenti.marconiverona.edu.it))
- Garonzi Marcello ([19067@studenti.marconiverona.edu.it](mailto:19067@studenti.marconiverona.edu.it))
- Mazzurana Riccardo ([19118@studenti.marconiverona.edu.it](mailto:19118@studenti.marconiverona.edu.it))
- Serratore Federico ([19169@studenti.marconiverona.edu.it](mailto:19169@studenti.marconiverona.edu.it))

