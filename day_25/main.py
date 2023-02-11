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

weather_data = pd.read_csv("weather_data.csv")

print(weather_data)