import pandas
data=pandas.read_csv("Squirrel_Data.csv")
gray=len((data[data["Primary Fur Color"]=="Gray"]))
cinnamon=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])

data_dic={
    "Fur Color":["gray", "cinnamon", "black"],
    "squ_count":[gray, cinnamon, black]
    }
final=pandas.DataFrame(data_dic)
print(final)
final.to_csv("sq_count.csv")
