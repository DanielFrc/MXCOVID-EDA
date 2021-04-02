import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import functions.clean_covid_dataset as clean_dataset
import functions.dataset_utilities as dataset_utilities
import functions.utilities as utilities
import functions.creating_plots as creating_plots
import lib.constants as constants

"""
Cleaning and filter the covid dataset
"""

#Columns with NA values to Drop
columns_to_drop = ["Recovered","Active","Delta_Recovered","People_Tested","People_Hospitalized","Province_State","FIPS"]

#Columns with zero value for drop
column_zero_values = "Delta_Confirmed"

#Columns with zero value for drop
column_index = "Report_Date_String"

#getting the covid dataset clean
covid_dataset = clean_dataset.get_clean_dataset(constants.URL_COVID_DATASET,
                                                columns_to_drop,
                                                column_zero_values,
                                                column_index)


dataset_utilities.

#Getting dataset for countries with similar population:
#    ETH
#    JPN
#    MEX
#    RUS
#    BGD
countries=["ETH","JPN","MEX","RUS","BGD"]

#Getting a dictionary with the datasets per country list
countries_dataframes = clean_dataset.get_dataset_per_country(covid_dataset,countries)


#Histograms

#Creating histograms for confirmed cases in plot/histograms/ 

for c in countries:
    creating_plots.plot_histogram(
        countries_dataframes[c],
        "Delta_Confirmed",
        c + " - Confirmed cases per day",
        "Confirmed cases",
        "Count(days)",
        c + "_confirmed_hist")

#Creating histograms for deaths in plot/histograms/ 
for c in countries:
    creating_plots.plot_histogram (
        countries_dataframes[c],
        "Delta_Deaths",
        c + " - Deaths per day",
        "Deaths",
        "Count(days)",
        c + "_deaths_hist")

#Boxplots

#Creating boxplots for confirmed cases in plot/boxplot/ 
creating_plots.plot_boxplot (
    countries_dataframes,
    'Delta_Confirmed',
    'Country_Region',
    "Confirmed cases",
    "Countries",
    "Boxplot - Confirmed cases per day (delta)"
    ,"confirmed_boxplot")

#Creating boxplots for deaths in plot/boxplot/ 
creating_plots.plot_boxplot (
    countries_dataframes,
    'Delta_Deaths',
    'Country_Region',
    "Deaths",
    "Countries",
    "Boxplot - Deaths per day (delta)",
    "deaths_boxplot")



#ECDF

#Creating ECDF for confirmed cases in plot/ecdf/ 
creating_plots.plot_ecdf(
    countries_dataframes,
    "Delta_Confirmed",
    countries,
    "Delta confirmed",
    "ECDF",
    "ECDF - Confirmed Cases",
    "confirmed_ecdf")

#Creating ECDF for deaths in plot/ecdf/ 
creating_plots.plot_ecdf(
    countries_dataframes,
    "Delta_Deaths",
    countries,
    "Delta confirmed",
    "ECDF",
    "ECDF - Deaths",
    "deaths_ecdf")



#Ignorar

"""
filter_dataset = covid_dataset[['iso3','Country_Region','Delta_Confirmed','Delta_Deaths']]

agg = filter_dataset.groupby(['iso3','Country_Region']).sum()

agg.reset_index(inplace=True)

gdp_df = dataset_utilities.get_dataset('data/gdp_csv.csv')[['Country Name','Country Code','2019']]

pop_df = dataset_utilities.get_dataset('data/covid19_country_population.csv')

dens_pop_df = dataset_utilities.get_dataset('data/population-density.csv')

dens_pop_df = dens_pop_df[dens_pop_df["Year"] == 2017]

dens_pop_df.dropna(subset=['Code','Population density (people per sq. km of land area)'], inplace=True)

#dataset_utilities.print_resume_dataset(dens_pop_df)

merged_df = agg.merge(gdp_df, how="left",left_on=["iso3"], right_on = ['Country Code'], suffixes=('','_gdp'))


merged_df = merged_df.merge(pop_df, how="left", left_on=["Country Code"], right_on = ["CountryAlpha3Code"])


merged_df = merged_df.merge(dens_pop_df, how="left", left_on=["Country Code"], right_on = ["Code"])

merged_df.dropna(inplace=True)

#dataset_utilities.print_resume_dataset(merged_df)

#merged_df.to_csv('merged_df.csv')

#Setting styles
sns.set()
    
    #Clear plt for clean graph
_=  plt.clf()

_= plt.plot(merged_df["Delta_Confirmed"]/1000000, merged_df["2019"]/1000000, marker='.', linestyle='none')

_= plt.xlabel("Confirmed Cases")
_= plt.ylabel("GDP")

plt.show()

"""