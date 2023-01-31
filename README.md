# Portafoglio

![Language](https://img.shields.io/badge/Language-Python-blue?style=flat)
![Build Status](https://img.shields.io/badge/Status-Develop-lightgreen?style=flat)
![Version](https://img.shields.io/badge/Version-v2.0-red?style=flat)
![License](https://img.shields.io/badge/License-MIT-lightblue.svg?style=flat)

Python app to operate on monthly stock prices. Downloads data from [yahoo finance](https://finance.yahoo.com/) and converts it into csv, json and yaml. Stock and period of prices are selectable, as for interval.

![](https://images.unsplash.com/photo-1642790551116-18e150f248e3?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=700&q=80)


## Requirements

- python 3.9
- pipenv (`pip install pipenv`)


## Installation

This app is built using `pipenv`. Before running be sure to install all packages and their dependences with:

```
pipenv install
```

## Execution

- Windows
  ```
  pipenv run python main.py
  ```
  or
  ```
  pipenv shell
  python main.py
  ```
  
- Linux
  ```
  pipenv run python3 main.py
  ```
  or
  ```
  pipenv shell
  python3 main.py
  ```
  
>
> The program will generate 3 files in the `out/` directory, each containing stocks data downloaded from the user.
>

  
## Contributing

You're free to clone the repository and collaborate.

[https://github.com/marcellogaronzi/Portafoglio.git](https://github.com/marcellogaronzi/Portafoglio.git)


## Contributors

- Bonomo Giovanni
- Garonzi Marcello
- Mazzurana Riccardo
- Serratore Federico
