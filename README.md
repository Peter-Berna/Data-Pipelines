<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# II-Data-Pipelines
*Peter Berna Williams*

*[Data Analytics FT, Barcelona & July 2022]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [How to run the various files](#organization)
- [Links](#links)

## Project Description
The aim of this project was to build a data pipeline to enrich an existing dataset. For this goal, an open source dataset was selected and completed with relevant variables through web scraping and API requests. Then, the resulting dataset enableb an Exploratory Data Analysis of the different variables.

## Hypotheses
1. Air pollution negatively correlates with the happiness score (the more pollution, less happiness).
2. Access to education, measured in schooling years and literacy rate, positively correlates with having happier societies.
3. The global average Happiness Score decreased in 2020-2021 as a consequence of the COVID-19 pandemic.

## Dataset
The "World Happiness Report 2015-2022" dataset was retrieved from Kaggle. The World Happiness Report uses global survey data to report how people evaluate their own lives in more than 150 countries worldwide. The happiness score is measured out of 10 points, with the best possible life being a 10 and the worst possible life being a 0.

The dataset is a compilation and aggregation of the yearly World Happiness Reports by the Kaggle user: MAY ZAN NILAR THEIN. It is composed by 1229 rows and 12 columns.

## Workflow
- First, the web of IQ Air was scraped to obtain a DataFrame fromt the table "Most polluted country and region ranking based on annual average PM2.5 concentration (μg/m³)"
- Then two more DataFrames were built through API requests to World Bank Indicators API: 
    1. Mean years of schooling (ISCED 1 or higher), population 25+ years, both sexes
    2. Literacy rate, adult total (% of people ages 15 and above)
- Then the 4 DataFrames were merged into one.
- After cleaning the resulting dataset, a series of 7 plots where made to visualize the data and to test the hypotheses.
- Finally, some conclusions.

## How to run the various files
    - Import dataset from 'Input' directory
    - import functions scraper.py, api_extract.py, cleaning.py, merge.py and vizualization.py
    - See the main notebook at src/Data-Pipelines-Projects.ipynb

## Links
[Repository](https://github.com/Peter-Berna/shark-attacks-data-cleaning)  
[Dataset](https://www.kaggle.com/datasets/teajay/global-shark-attacks?resource=download)  
[Presentation](https://docs.google.com/presentation/d/12VcBD9KBDXUFwCYwdO_X_LFq9WiiRH9xSjg4mIzZblM/edit?usp=sharing)