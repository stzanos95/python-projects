import http.client

def main():

    conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "c13c7c011emsheecdd31d8583050p13ab78jsna02edae167e8",
        'X-RapidAPI-Host': "api-nba-v1.p.rapidapi.com"
    }

    conn.request("GET", "/seasons", headers=headers)
    res = conn.getresponse()
    data = res.read()

    print(data.decode("utf-8"))


if __name__ == '__main__':
    main()
