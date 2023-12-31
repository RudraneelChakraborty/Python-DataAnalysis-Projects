import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

#Squirrel Fur Color
grey_squirrel = data[data['Primary Fur Color'] == 'Gray']
grey_squirrel_count = len(grey_squirrel)

red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

Dict_On_Fur_Color = {
        "Fur Color" : ["Grey" , "Cinnamon", "Black"],
        "Count": [grey_squirrel_count,red_squirrel_count,black_squirrel_count]
    }

df = pd.DataFrame(Dict_On_Fur_Color)
df.to_csv('squirrel_fur_count.csv')

#Age of Squirrels Count
Adult_count = len(data[data['Age'] == 'Adult'])
Juvenile_count = len(data[data['Age'] == 'Juvenile'])

Dict_On_Age = {
        "Age" : ["Adult" , "Juvenile"],
        "Count": [Adult_count,Juvenile_count]
    }

df = pd.DataFrame(Dict_On_Age)
df.to_csv('squirrel_Age_count.csv')
