import requests
import json
from datetime import datetime, timedelta


class Stockbrain:

    def __init__(self, url: str, func: str, symb: str, intr: str, key: str, company: str):
        r = requests.get("{}function={}&symbol={}&interval={}&apikey={}".format(url, func, symb, intr, key))
        meta_data_raw = r.json()["Meta Data"]
        time_series_raw = r.json()["Time Series ({})".format(intr)]
        self.company = company
        self.meta_data = {key.replace("{}. ".format(key[0]), ""): value
                          for key, value in meta_data_raw.items()}
        self.time_series = {}
        for date, subdict_raw in time_series_raw.items():
            subdict = {key.replace("{}. ".format(key[0]), ""): value
                       for key, value in subdict_raw.items()}
            self.time_series[date] = subdict

    def print_meta_data(self):
        print(json.dumps(self.meta_data, indent=4))

    def print_time_series(self):
        print(json.dumps(self.time_series, indent=4))

    def print_latest_closing(self, period="day"):
        last_refreshed = self.meta_data["Last Refreshed"]
        date = [int(i) for i in last_refreshed[0:last_refreshed.index(" ")].split("-")]
        date_time = [int(i) for i in last_refreshed[last_refreshed.index(" ") + 1:-1].split(":")]
        last_refreshed_datetime = datetime(*date, *date_time)
        if period == "month":
            days = 30
        elif period == "year":
            days = 365
        else:
            days = 1
        prev_last_refreshed_datetime = str(last_refreshed_datetime - timedelta(days=days))
        last_closing = float(self.time_series[last_refreshed]["close"])
        prev_closing = float(self.time_series[prev_last_refreshed_datetime]["close"])
        print("Stock data for", self.company, "\n")
        print("Prices were last refreshed: {}\n".format(last_refreshed))
        print("Last closing price in {}: ".format(prev_last_refreshed_datetime), last_closing)
        print("Previous {} closing price: ".format(period), prev_closing)
        if last_closing > prev_closing:
            print("Stocks went up by >>>>> {}%.".format(round(last_closing / prev_closing, 2)))
        elif last_closing < prev_closing:
            print("Stocks went down by >>>>> {}%".format(round(prev_closing / last_closing, 2)))
        else:
            print("Stock price has not changed in the last {}.".format(period))

    def print_latest_news(self):
        pass
