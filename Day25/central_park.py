import pandas

data=pandas.read_csv("2018-central-park.csv")

gray_color=data[data["Primary Fur Color"]=="Gray"]
red_color=data[data["Primary Fur Color"]=="Cinnamon"]
black_color=data[data["Primary Fur Color"]=="Black"]
print(len(gray_color))
print(len(red_color))
print(len(black_color))

data_dict={
    "Fur Color":{"Gray","Red","Black"},
    "COunt":{len(gray_color),len(red_color),len(black_color)}
}

df=pandas.DataFrame(data_dict)

df.to_csv("Fur_color.csv")
