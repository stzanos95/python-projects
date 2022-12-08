from backend import Stockbrain


API_URL_BASE = "https://www.alphavantage.co/query?"
API_PARAMS = {
    "symbol": "U",
    "company": "Unity Software Inc.",
    "key": "VWKOZ17OZKD7UB8H",
    "function": "TIME_SERIES_INTRADAY",
    "interval": "60min"
}


def main():
    stock_brain = Stockbrain(API_URL_BASE,
                             API_PARAMS["function"],
                             API_PARAMS["symbol"],
                             API_PARAMS["interval"],
                             API_PARAMS["key"],
                             API_PARAMS["company"])
    stock_brain.print_latest_closing()


if __name__ == '__main__':
    main()
