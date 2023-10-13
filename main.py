import csv
import pandas

data = []
csv_data = []
temperatures = []
temp = 0

file = open("weather_data.csv")
# data.append(file.readlines())
csv_data = csv.DictReader(file)
print(csv_data)
for row in csv_data:
    print(row)
    temperatures.append(int(row.get("temp")))
file.close()

print(temperatures)

data = pandas.read_csv("weather_data.csv")
data_list = data["temp"].to_list()

idx = 0
sum = 0
for temp in data_list:
    sum += temp
    idx += 1

avg = sum / idx
print(avg)

avg = 0

avg = data["temp"].mean()
max = data["temp"].max()
print(avg)
print(max)
# print(data_list)

