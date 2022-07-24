import requests
import pandas as pd

def worldbank_indicator(indicator_name, indicator_code):
    url = 'http://api.worldbank.org/v2/country/all/indicator/{}?format=json&date=2015:2022&per_page=6000'
    response = requests.get(url.format(indicator_code))
    data = response.json()
    df = pd.json_normalize(data[1])
    df = df[['country.id','country.value', 'date', 'value']]
    df.columns = ['Country code', 'Country', 'Year', indicator_name]
    return df

