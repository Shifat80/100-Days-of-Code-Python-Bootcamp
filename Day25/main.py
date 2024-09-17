# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data) 


# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []

#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)




import pandas

data=pandas.read_csv("weather-data.csv")
data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)
print(data["temp"].mean())
print(data["temp"].max())



# get data in column 
print(data["condition"])
print(data.condition)

# print by column
print(data[data.day == "Monday"])

print(data[data.temp==data.temp.max()])
