import requests
import argparse
from datetime import datetime

PXLA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "stamnoob"
PWD = "m0n0mlkiaple0n"
HEADER = {"X-USER-TOKEN": PWD}

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Post a coding hours pixel in the pixela \"code-graph\".")
    parser.add_argument("-H", "--hours",
                        required=True, type=float,
                        help="Today's coding hours (float)")
    return parser.parse_args()

def create_user(pwd: str, username: str) -> None:
    request_body = {
        "token": pwd,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    r = requests.post(url=PXLA_ENDPOINT, json=request_body)
    print("Creating new user with username: {}".format(USERNAME))
    print_response(r)

def create_graph(graph_id: str, name: str, unit: str, unit_type: str, color: str) -> None:
    graph_body = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": unit_type,
        "color": color
    }
    r = requests.post(url="{}/{}/graphs".format(PXLA_ENDPOINT, USERNAME), json=graph_body, headers=HEADER)
    print("Creating new graph with ID:", graph_id)
    print_response(r)

def update_pixel(hours: float, graph_id: str) -> None:
    today_date = datetime.today()
    date_string = "{}{}{}".format(today_date.year, today_date.month, today_date.day)
    pixel_body = {
        "date": date_string,
        "quantity": str(hours)
    }
    r = requests.post(url="{}/{}/graphs/{}".format(PXLA_ENDPOINT,
                                                   USERNAME,
                                                   graph_id),
                      json=pixel_body,
                      headers=HEADER)
    print_response(r)

def print_response(resp: requests.Response) -> None:
    print(resp.json()["message"], "\n")

def main() -> None:
    # create_user(PWD, USERNAME)
    # create_graph("code-graph", "Coding Graph", "Hours", "float", "sora")
    update_pixel(arg_parser().hours, "code-graph")
    print("URL: https://pixe.la/v1/users/{}/graphs/{}".format(USERNAME, "code-graph"))


if __name__ == "__main__":
    main()
