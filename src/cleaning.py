import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import numpy as np
import pycountry_convert as pc
import country_converter as coco
cc = coco.CountryConverter()
import warnings
warnings.filterwarnings('ignore')

def clean_df(df):
    # Dropping duplicated cols after mergin, Country code will be the index
    df = df.drop(['Unnamed: 0', 'Country_x', 'Country_y'], axis=1)
    # Change order of the columns, put country code in position 1
    df = df.iloc[:, [10,0,1,2,3,4,5,6,7,8,9,11,12,13,14]]
    # Add country name col with country_converter()
    iso2_names = list(df['Country code'])
    country_names = cc.convert(names = iso2_names, src = 'ISO2', to = 'name_short')
    df.insert(1,'Country', country_names )
    # Replace "," by "." in 'Happiness Score'and convert column to type(float)
    df['Happiness Score'] = df['Happiness Score'].str.replace(",", ".")
    df['Happiness Score'] = df['Happiness Score'].apply(lambda x: float(x) if type(x) == str else x)
    return df

def tag_countries_continent(df):
    df['Country code'] = df['Country code'].fillna('')
    continents = []
    for i in df['Country code']:
        try:
            continent = pc.country_alpha2_to_continent_code(i) 
            continent = pc.convert_continent_code_to_continent_name(continent)
            continents.append(continent)
        except:
            continents.append(np.nan)
    df['Continent'] = continents
    return df