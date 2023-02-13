# WORKING WITH CSV DATA AND THE PANDAS LIBRARY

# with open("weather_data.csv") as file:
#     weather_data = file.readlines()

# print(weather_data)

# import csv

# with open("weather_data.csv") as file:
#     weather_data = csv.reader(file)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas as pd

# weather_data = pd.read_csv("weather_data.csv")

# print(weather_data[weather_data["temp"] == max(weather_data["temp"])]["day"])


sq_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey = len(sq_data[sq_data["Primary Fur Color"] == "Gray"])
red = len(sq_data[sq_data["Primary Fur Color"] == "Cinnamon"])
black = len(sq_data[sq_data["Primary Fur Color"] == "Black"])

color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}

color_df = pd.DataFrame(color_dict)


print(color_df)
