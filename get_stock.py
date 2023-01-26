from datetime import datetime
import requests
import asyncio

EPOCH = datetime(1970, 1, 1)


def get_stock(stock, start, end=datetime.now(), interval="1mo", success=None, error=None):
    """
    Returns csv data of selected stock, between chosen period.

        Parameters:
            stock (str): Stock name
            start (datetime): Start date of period
            stop (datetime): End date of period (default is today)
            interval (str): Type of interval (1mo, 1da, ...)
            success (lambda): Success callback
            error (lanbda): Error callback
    """

    # Stock Period
    start = int((start - EPOCH).total_seconds())
    end = int((end - EPOCH).total_seconds())

    # Request
    URL = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={start}&period2={end}&interval={interval}&events=history&includeAdjustedClose=true"
    header = {
        'Connection': 'keep-alive',
        'Expires': '-1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
    }

    # Download csv from yahoo server
    res = requests.get(URL, headers=header)
    if res.status_code == 200:
        if success:
            success(res.text)
    else:
        if error:
            error(res.status_code)


def main():
    def on_success(string):
        with open("csv/result.csv", "w") as csv:
            csv.write(string)

    def on_error(code):
        print("Unable to fetch data. HTTP returned error", code)

    # Download data
    get_stock("PIRC.MI", datetime(2022, 1, 1), success=on_success, error=on_error)


if __name__ == "__main__":
    main()
