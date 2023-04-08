import pandas as pd
import numpy as np
import random as rnd
import matplotlib.pyplot as plot

#1
data = pd.read_csv('data.csv')
#2
stats = data.describe()

print(stats)
print()
#3
data["Duration"].fillna(data["Duration"].mean(), inplace=True)
data["Pulse"].fillna(data["Pulse"].mean(), inplace=True)
data["Maxpulse"].fillna(data["Maxpulse"].mean(), inplace=True)
data["Calories"].fillna(data["Calories"].mean(), inplace=True)
#4
print(stats["Pulse"])
print()
print(stats["Duration"])
print()

#5
filteredCalories = data.loc[(data['Calories'] > 500) & (data['Calories'] < 1000)]
print(filteredCalories)
print()
#6
filteredCaloriesAndPulse = data.loc[(data["Calories"] > 500) & (data["Pulse"] < 100)]
print(filteredCaloriesAndPulse)
print()
#7
modified_data = data[["Duration", "Pulse", "Calories"]].copy()
print(modified_data)
print()
#8
data.drop("Maxpulse", axis=1, inplace=True)
print(data)
print()

#9
data.astype({"Calories": "int32"})
print(data)
print()
#10
dfplot = data.plot.scatter(x="Duration", y="Calories")
plot.show()

#Titanic Data

