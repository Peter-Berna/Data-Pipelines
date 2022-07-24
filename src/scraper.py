def scrape_column(obj, attrs, soup):
    """
    Finds the column in the soup
    Args: the object and attribute of the soup
    Returns: list of the elements of the column
    """
    from bs4 import BeautifulSoup

    find = soup.find_all(obj, attrs=attrs)
    return [i.getText().strip() for i in find]

def generate_df(rank, country, year_2018, year_2019, year_2020, year_2021, population):
    """
    Creates a df from the scraped cols
    Args: the 7 scraped cols
    Returns: unpivot df = the 4 year cols in one
    """
    import pandas as pd

    pollution_country = {
    "Rank":rank,
    "Country":country,
    "2018":year_2018,
    "2019":year_2019,
    "2020":year_2020,
    "2021":year_2021,
    "Population":population
}
    df = pd.DataFrame(pollution_country)
    df_unpivot = pd.melt(df, id_vars=['Country', 'Population'], value_vars=['2018', '2019', '2020', '2021'], var_name='Year', value_name='Pollution')
    return df_unpivot 

def scrape_iqair():
    """
    Scrapes IQ Air website
    Returns: outputs data in pandas df
    """
    import pandas as pd
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.iqair.com/world-most-polluted-countries"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    rank = scrape_column('td', {"class":"mat-cell cdk-cell table--cell__rank cdk-column-rank mat-column-rank ng-star-inserted"}, soup)
    country = scrape_column('div', {"class":"country-name"}, soup)
    year_2018 = scrape_column('td', {"class":"mat-cell cdk-cell table--cell__year__country has-single-badge is-radius-left is-radius-right cdk-column-avg2018 mat-column-avg2018 ng-star-inserted"}, soup)
    year_2019 = scrape_column('td', {"class":"mat-cell cdk-cell table--cell__year__country has-single-badge is-radius-left is-radius-right cdk-column-avg2019 mat-column-avg2019 ng-star-inserted"}, soup)
    year_2020 = scrape_column('td', {"class":"mat-cell cdk-cell table--cell__year__country has-single-badge is-radius-left is-radius-right cdk-column-avg2020 mat-column-avg2020 ng-star-inserted"}, soup)
    year_2021 = scrape_column('td', {"class":"mat-cell cdk-cell table--cell__year__country has-single-badge is-radius-left is-radius-right cdk-column-avg2021 mat-column-avg2021 ng-star-inserted"}, soup)
    population = scrape_column('td', {"class":"mat-cell cdk-cell is-radius-left is-radius-right table--cell__population cdk-column-population mat-column-population ng-star-inserted"}, soup)
    df = generate_df(rank, country, year_2018, year_2019, year_2020, year_2021, population)
    return df

