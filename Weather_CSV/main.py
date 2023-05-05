import pandas
# data = pandas.read_csv("weather-data.csv")
#
# print(type(data))
data = pandas.read_csv("Central-Park-Squirrel-Census-Squirrel-Data.csv")
fur_color = data["Primary Fur Color"]
hashmap = {}
for col in fur_color:
    if hashmap.get(col):
        hashmap[col] += 1
    else:
        hashmap[col] = 1

new_dict = {"fur_color": [],
            "count": []}
for key, value in hashmap.items():
    new_dict["fur_color"].append(key)
    new_dict["count"].append(value)

data_csv = pandas.DataFrame(new_dict)
data_csv.to_csv("new_csv_file.csv")

