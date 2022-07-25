import pandas as pd
import numpy as np
import pycountry
import pycountry_convert as pc
import country_converter as coco
cc = coco.CountryConverter()
import warnings
warnings.filterwarnings('ignore')
import scraper as scr
import api_extract as api

pollution = scr.scrape_iqair()
schooling_years = api.worldbank_indicator(indicator_name='Avg. Schooling Years', indicator_code='UIS.EA.MEAN.1T6.AG25T99')
literacy = api.worldbank_indicator(indicator_name='Literacy Rate', indicator_code='SE.ADT.LITR.ZS')

# Checks similar values, in order to get more matching countries
def do_fuzzy_search(country):
    try:
        result = pycountry.countries.search_fuzzy(country)
        return result[0].alpha_2
    except:
        return np.nan


def merge_datasets(df):
    # Preparing the data to optimize the merge 
    df["Country code"] = df["Country"].apply(lambda country: do_fuzzy_search(country))
    pollution["Country code"] = pollution["Country"].apply(lambda country: do_fuzzy_search(country))
    pollution['Year'] = pollution['Year'].astype(int)
    literacy['Year'] = literacy['Year'].astype(int)
    schooling_years['Year'] = schooling_years['Year'].astype(int)
    # Left merge 
    df = pd.merge(df, literacy, on=["Year", "Country code"], how="left")
    df = pd.merge(df, schooling_years, on=["Year", "Country code"], how="left")
    df = pd.merge(df, pollution, on=["Year", "Country code"], how="left")
    
    return df