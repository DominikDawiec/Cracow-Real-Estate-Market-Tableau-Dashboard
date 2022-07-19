# -*- coding: utf-8 -*-

# -- Sheet --

# downloading required packages
import numpy as np
import pandas as pd

# downloading the dataset
df = pd.read_csv("HousePrices.csv", encoding='latin-1')

# renaming column names 
df.rename(columns = {'floor':'Floor', 'id':'ID', 'price':'Price', 
                     'rooms':'Rooms', 'sq':'Square Meters', 'year':'Build year'}, 
                    inplace = True)

# data narrowing to the city of Krakow
df = df[df['city'] == 'Kraków'] 

# removing unnecessary columns
df.drop(['Unnamed: 0', 'address', 'city'], inplace=True, axis=1)

# veryfing missing values
import missingno as msno
ax = msno.matrix(df)

ax = msno.bar(df)

# making new column for Price per Square Meter
df['Price per Square Meter'] = round(df['Price']/df['Square Meters'], 2)

df

df.to_csv('Houses.csv', index = False)

