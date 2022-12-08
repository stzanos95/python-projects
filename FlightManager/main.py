import requests
import json


SHEET_URL = 'https://api.sheety.co/2369ee1ee04ed749b4e356cae9743fcd/flightDealer/prices'
HEADER = {'Authorization': 'Basic c3RhbV9mbGlnaHRzOjEyM2ZsaWdodHM0NTkx'}


def get_city_info(data: list) -> dict:
    return {city['city']: {'code': city['iataCode'], 'lowest': city['lowestPrice']} for city in data}

def main():
    r = requests.get(url=SHEET_URL, headers=HEADER)
    data_dict = get_city_info(r.json()['prices'])


if __name__ == '__main__':
    main()
