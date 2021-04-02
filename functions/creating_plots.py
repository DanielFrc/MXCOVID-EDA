import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import functions.utilities as utilities
import lib.constants as constants

def plot_histogram(dataset,column_name,title,xlabel,ylabel,filename):
    """
    Generate a png with a histogram of a given dataset
        Params:
            dataset: Dataset for plotting histogram
            column_name: Column to plot histogram
            title: Title of the graph
            xlabel: label of the x-axis
            ylabel: label of the y-axis
            filename: name of the png file

    """
    #Setting styles
    sns.set()
    
    #Clear plt for clean graph
    plt.clf()

    try:
        #calculating beans for histogram
        n_beans_confirmed = utilities.calculate_bins(len(dataset[column_name]))
        #plotting hist
        _ = plt.hist(dataset[column_name], bins=(n_beans_confirmed))
        #Setting title
        _ = plt.title(title)
        #Setting y-label
        _ = plt.ylabel(ylabel)
        #Setting x-label
        _ = plt.xlabel(xlabel)
        #Saving to path
        _ = plt.savefig(constants.HISTOGRAM_PATH + filename + constants.PNG_EXTENSION)

    except Exception as e:
        print("Error trying to plot histogram: " + str(e))


def plot_boxplot (dic_dataframes, x_column, y_column, xlabel, ylabel, title, filename):
    """
    Generate a boxplot of a dataframe dictionary or dataframe
        Params:
            dic_dataframes: Dataset for plotting boxplot, can be a single df or a dict of dfs
            x_column: Column to plot on x-axis
            y_column: Column to plot on y-axis
            title: Title of the graph
            xlabel: label of the x-axis
            ylabel: label of the y-axis
            filename: name of the png file

    """

    #Setting styles
    sns.set()    
    #Clear plt for clean graph
    plt.clf()

    #Check if the dataset is a dict
    try:
        if isinstance(dic_dataframes, dict) :
            #Appending all the datasates in the dicctionary
            df_full = pd.DataFrame()
            df_full = df_full.append( [ v for (k,v) in dic_dataframes.items()] )
            #Plotting the catplot (boxplot)
            _ = sns.catplot(x=x_column,
                            y=y_column,
                            kind ='box',
                            data=df_full)
            #Plotting stripplot
            _ = sns.stripplot(x=x_column,
                            y=y_column,
                            color='b',
                            size=3,
                            data=df_full,
                            marker="D",
                            edgecolor="gray",
                            alpha=.5)
        else:
            _ = sns.catplot(x=x_column,
                            y=y_column,
                            kind ='box',
                            data=dic_dataframes)
            #Plotting stripplot
            _ = sns.stripplot(x=x_column,
                            y=y_column,
                            color='b',
                            size=3,
                            data=dic_dataframes,
                            marker="D",
                            edgecolor="gray",
                            alpha=.5)

        #Adding title
        _ = plt.title(title)
        #Adding x-label
        _ = plt.xlabel(xlabel)
        #Adding y-label
        _ = plt.ylabel(ylabel)
        #Saving to path
        _ = plt.savefig(constants.BOXPLOT_PATH + filename + constants.PNG_EXTENSION)
    
    except Exception as e:
        print("Error trying to plot the graph: " + str(e))
    
def plot_ecdf(dataset, column, legend, xlabel, ylabel, title, filename):
    """
    Generate ECDF plot of a dict of dataframes
    Params:
        dataset: Dataset for plotting ECDF
         legend: String array with the legend for ECDF
         xlabel: label of the x-axis 
         ylabel: label of the y-axis
          title: Title of the graph
        filename: Name of the png file
    """

    #Setting styles
    sns.set()    
    
    for k,v in dataset.items():
        #Clear plt for clean graph
        plt.clf()

        #Calculating ECDF for plots
        x,y = utilities.calculate_ecdf(v[column])

        #Making ECDF 
        _ = plt.plot(x, y, marker= ".", linestyle ="none")

        #Setting Legend
        #plt.legend(k, loc='lower right')
        
        #Setting Title
        _ = plt.title(k + " " + title)
        
        #Setting x-label
        _ = plt.xlabel(xlabel)
        #Setting y-label
        _ = plt.ylabel(ylabel)

        #Calculating percentiles
        percentile_array = [5,25,50,75,95]

        percentile_label, percentile_values =  utilities.calculate_percentiles(v[column],percentile_array)

        _ = plt.plot(percentile_values, percentile_label/100, marker='D',color='red', linestyle='none')

        #Saving to path
        _ = plt.savefig(constants.ECDF_PATH + k + "_" + filename + constants.PNG_EXTENSION)
    
    
    #Clear plt for clean graph
    plt.clf()

    for k,v in dataset.items():
        #Calculating ECDF for plots
        x,y = utilities.calculate_ecdf(v[column])

        #Making ECDF 
        _ = plt.plot(x, y, marker= ".", linestyle ="none")


        
    #Setting Legend
    plt.legend(legend, loc='lower right')
    
    #Setting Title
    _ = plt.title(title)
    
    #Setting x-label
    _ = plt.xlabel(xlabel)
    #Setting y-label
    _ = plt.ylabel(ylabel)
    
    #Saving to path
    _ = plt.savefig(constants.ECDF_PATH +  filename + constants.PNG_EXTENSION)
    

