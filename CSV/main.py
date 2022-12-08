# with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
# print(data)

# import csv


# with open("../resources/section25/weather_data.csv") as weather_file:
#    data = csv.reader(weather_file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#    print()

import pandas


PATH_WEATHER_DATA = "../resources/section25/weather_data.csv"

data = pandas.read_csv(PATH_WEATHER_DATA)
# print(data.to_dict())
# print(data["temp"].to_list())

# Average temperature calculation
# temperatures = data["temp"].to_list()
# avg_temperature = sum(temperatures) / len(temperatures)
# avg_temperature_pandas = data["temp"].mean()
# print(avg_temperature_pandas)

# Maximum
# print(data["temp"].max())
# print(data.temp.max())

# Row of data
# print(data[data.day == "Monday"])

# Row of maximum temperature
# print(data[data.temp == data.temp.max()])

# Monday's temperature in Fahrenheit
# monday = data[data.day == "Monday"]
# print(float(monday.temp) * 9/5 + 32)

# Create a dataframe
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("new_data.csv", index=False)
