import pandas
import time


def create_squirrel_data():
    squirrel_data = pandas.read_csv("Squirrel_Data.csv")
    fur_colors = squirrel_data["Primary Fur Color"].to_list()
    fur_data_dict = {
        "Fur Color": [],
        "Entries": []
    }
    for fur_color in fur_colors:
        if isinstance(fur_color, str):
            if fur_color not in fur_data_dict["Fur Color"]:
                fur_data_dict["Fur Color"].append(fur_color)
                fur_data_dict["Entries"].append(1)
            else:
                idx = fur_data_dict["Fur Color"].index(fur_color)
                fur_data_dict["Entries"][idx] += 1
    pandas.DataFrame(fur_data_dict).to_csv("Squirrel_Fur_Data.csv")


def create_squirrel_data_opt1():
    squirrel_data = pandas.read_csv("Squirrel_Data.csv")
    fur_data_dict = {
        "Fur Color": [],
        "Entries": []
    }
    for fur_color in squirrel_data["Primary Fur Color"].to_list():
        if isinstance(fur_color, str):
            if fur_color not in fur_data_dict["Fur Color"]:
                fur_data_dict["Fur Color"].append(fur_color)
                fur_data_dict["Entries"].append(len(squirrel_data[squirrel_data["Primary Fur Color"] == fur_color]))
    pandas.DataFrame(fur_data_dict).to_csv("Squirrel_Fur_Data_opt1.csv")

