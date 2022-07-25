import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
from bs4 import BeautifulSoup
import pycountry
import pycountry_convert as pc
import country_converter as coco
cc = coco.CountryConverter()
import warnings
warnings.filterwarnings('ignore')

def choropleth(df):
    fig = px.choropleth(df, locations="Country",
                        locationmode="country names",
                        color="Happiness Score", 
                        hover_name="Country", # column to add to hover information
                        color_continuous_scale=px.colors.sequential.Plasma,
                        animation_frame="Year",
                        title="Happiness Score in the World (2015-2022)")
    return fig.show()

def plot_yearly_index_continents(df):
    df_continent = pd.DataFrame(df.groupby(['Continent','Year'])['Happiness Score'].mean()).reset_index()
    df_year = pd.DataFrame(df.groupby('Year')['Happiness Score'].mean()).reset_index()
    df_year['Continent'] = 'Global'
    df_grouped = pd.concat([df_continent, df_year])
    fig = px.line(df_grouped, x="Year", y="Happiness Score", color='Continent', title="Happiness Score yearly evolution by continent (2015-2022)", markers=True)
    fig.update_traces(patch={"line": {"color": "black", "width": 4, "dash": 'dot'}}, selector={"legendgroup": "Global"}) 
    return fig.show()

def plot_happiness_pollution(df):
    happiness = pd.DataFrame(df.groupby('Country')['Happiness Score'].mean()).reset_index()
    df['Pollution'] = df['Pollution'].replace('-',np.nan).astype(float)
    pollution = pd.DataFrame(df.groupby('Country')['Pollution'].mean()).reset_index()
    df_grouped = pd.merge(happiness,pollution, on='Country')
    fig = px.scatter(df_grouped, x='Happiness Score', y='Pollution', color='Country', title="Happiness Score related to Air Pollution")
    fig.update_traces(marker=dict(size=10))
    return fig.show()

def plot_happiness_schooling(df):
    happiness = pd.DataFrame(df.groupby('Country')['Happiness Score'].mean()).reset_index()
    schooling = pd.DataFrame(df.groupby('Country')['Avg. Schooling Years'].mean()).reset_index()
    df_grouped = pd.merge(schooling,happiness, on='Country')
    fig = px.scatter(df_grouped, x='Happiness Score', y='Avg. Schooling Years', color='Country', title="Happiness Score related to Avg. Schooling Years")
    fig.update_traces(marker=dict(size=10))
    return fig.show()

def plot_happiness_literacy(df):
    happiness = pd.DataFrame(df.groupby('Country')['Happiness Score'].mean()).reset_index()
    df['Literacy Rate'] = df['Literacy Rate'].replace('-',np.nan).astype(float)
    literacy = pd.DataFrame(df.groupby('Country')['Literacy Rate'].mean()).reset_index()
    df_grouped = pd.merge(happiness,literacy, on='Country')
    fig = px.scatter(df_grouped, x='Happiness Score', y='Literacy Rate', color='Country', title="Happiness Score related to Literacy Rate")
    fig.update_traces(marker=dict(size=10))
    return fig.show()

def heatmap_happiness_index(df):
    variables = df[['Happiness Score', 'Economy (GDP per Capita)',
       'Family (Social Support)', 'Health (Life Expectancy)', 'Freedom',
       'Trust (Government Corruption)', 'Generosity']]
    variables = variables.replace(',','.', regex=True)
    variables = variables.astype(float)
    corr = variables.corr().round(2)
    fig = px.imshow(corr, text_auto=True, title="Correlation matrix of variables that compose the Happiness Score")
    return fig.show()

def heatmap_happiness_index_newvariables(df):
    variables = df[['Literacy Rate','Avg. Schooling Years', 'Population', 'Pollution', 'Happiness Score']]
    variables['Population'] = variables['Population'].replace(',','',regex=True)
    variables['Population'] = variables['Population'].astype(float)
    corr = variables.corr().round(2)
    fig = px.imshow(corr, text_auto=True, title="Correlation matrix of selection of extra variables")
    return fig.show()