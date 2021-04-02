import pandas as pd
import functions.dataset_utilities as dataset_utilities



def remove_zero_values(dataset,column_name):
    '''
    Remove records with zero values in a column. 
        Parameters:
            dataset (pandas.DataFrame): The covid Dataset
            column_name (str): The column with zero values to remove

        Returns
            dataset (pandas.DataFrame): Dataframe modified.
    '''
    return dataset[(dataset[column_name]>0)]


def filter_dataset(dataset, column_filter, filter_value):
    '''
    Filter a dataset by a column equals to a given value
        Parameters:
            dataset (pandas.DataFrame): The covid Dataset
            column_filter (str): The column to filter
            filter_value (str): Value to filter
        Returns
            dataset (pandas.DataFrame): Dataframe filtered
    '''
    #Filtering dataset with the given parameters
    return dataset[(dataset[column_filter]==filter_value)]

def fillna_dataset(dataset):
    '''
    Filter a dataset by a column equals to a given value
        Parameters:
            dataset (pandas.DataFrame): The covid Dataset
        Returns
            dataset (pandas.DataFrame): Dataframe without NA values
    '''
    #Filtering dataset with the given parameters
    for col in dataset.columns:
        dataset[col] = dataset[col].fillna(0)
    return dataset


def get_clean_dataset(url, columns_to_drop,column_zero_values,index_column):
    '''
    Filter and clean the covid dataset
        Parameters:
            url (str): URL of the dataset 
            columns_to_drop (str[]): List of columns to drop from the covid dataset
            column_zero_values (str): Name of the column with xer values
            index_column (str): Name of the index column, date of the data/
        Returns
            dataset (pandas.Dataframe): Dataframe cleaned
    '''

    #getting the covid dataset
    covid_dataset = dataset_utilities.get_dataset(url)

    #Fill na values
    covid_dataset = fillna_dataset(covid_dataset)
    
    #dropping unnecesary columns
    covid_dataset = dataset_utilities.drop_columns(covid_dataset, columns_to_drop)

    #remove rows with zero values in column "Delta_Confirmed"
    covid_dataset = remove_zero_values(covid_dataset,column_zero_values)

    #creating index
    covid_dataset = dataset_utilities.create_index(covid_dataset,index_column)

    #printing summary of the new dataset
    dataset_utilities.print_resume_dataset(covid_dataset)

    return covid_dataset



def get_dataset_per_country(dataset, countries_list=[], column_name="iso3"):
    """
    Returns a dicctionary with datasates of a multiple countries
        Parameters:
            dataset (pandas.Dataframe): A dataframe with multiple countries
            column_name (str): The name of the column with country names.
            countries_list (str[]): A list of the countrie names to extract for the main dataset
        Returns
            countries_dataframes: Diccionary with the datasets filtered by country.
    """

    countries_dataframes = {}

    try: 
        for country in countries_list:
            p = filter_dataset(dataset,column_name,country)
            countries_dataframes[country] = p
    except:
        print("There was an error trying to filter the dataset, verify the column name and the country name")
    finally:        
        return countries_dataframes
        

