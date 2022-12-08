#
#
# nutritionix API with google sheets
#
# stamnoob@gmail.com

import requests
import json


API_ID = '5c0e8b28'
API_KEY = 'b7f22f90677b787c8b718b2f47381fc2'
ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/nutrients'
API_HEADER = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY
}
REQUEST_BODY = {
        'gender': 'male',
        'weight_kg': '84',
        'height_cm': '177',
        'age': '27'
}

def main():
    reply = input('Enter a food: \n')
    r = requests.post(url=ENDPOINT, json={'query': reply}, headers=API_HEADER)
    print(json.dumps(r.json(), indent=4))


if __name__ == '__main__':
    main()
