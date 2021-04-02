import pandas as pd

def get_dataset(url) :
    '''
    Returns a pandas dataset from a given url to a csv 
        Parameters:
            url (str): A url or path to a csv file.
        Returns
            dataset (pandas.DataFrame): Dataframe from csv file
    '''
    
    try:
        #Getting CSV file and convert to dataset
        dataset = pd.read_csv(url,low_memory=False)
    except:
        #Printing error when exception
        print("Incorrect url or not available resource")
    
    return dataset


def drop_columns(dataset,columns_to_drop=[]):
    '''
    Drop columns in place from a Pandas Dataframe
        Parameters:
            dataset (pandas.DataFrame): Dataset to drop columns
            columns_to_drop (str[]): Array of columns to drop, default empty
        Returns
            dataset (pandas.Dataframe): Dataset with dropped columns
    '''

    try:
        #Dropping columns
        dataset.drop(columns_to_drop, axis="columns",inplace=True)
    except:
        #Printing error when exception
        print("Error trying to drop columns. Verify that columns names are correct or exists")
    
    return dataset

def convert_to_datetime (dataset, date_column):
    '''
    Convert to date a column of a dataframe
        Parameters:
            dataset (pandas.Dataframe): Dataset to set index
            date_column (str): Column to convert to Date
        Returns
            dataset (pandas.Dataframe): Dataset with date column
    '''
    try:
        #converting column to date (inplace)
        dataset[date_column] = pd.to_datetime(dataset[date_column])
    except:
        #Printing error when exception
        print("Format column not recognize or mispeling column. Ensure is a recognized date format")
    return dataset


def create_index(dataset, index_column, is_date = True):
    '''
    Set index in a Dataset from a given column with date option
        Parameters: 
            dataset (pandas.Dataframe): Dataset to set index
            index_column (str): Column to be index
            is_date (Bool): Flag to indicate if the given column is in date format 
        Returns
            dataset (pandas.Dataframe): Dataset with index columns
    '''
    try:
        #Converting DateString to Pandas DateTime
        if(is_date):
            dataset = convert_to_datetime(dataset, index_column)

        #Converting column to Index
        dataset.set_index(index_column, inplace = True) 
    except:
        #Printing error when exception
        print("Error trying to set the index, verify the column. If is a date, verify the format")

    #return indexed dataset
    return dataset


def print_resume_dataset(dataset):
    '''
    Set index in a Dataset from a given column with date option
        Parameters: 
            dataset (pandas.Dataframe): Dataset to print resume
    '''

    #Printing types of the columns
    print(dataset.dtypes)
    
    #Printing Sumarized statistics
    print(dataset.describe())
    
    #Printing a sample of records
    print(dataset.head())

