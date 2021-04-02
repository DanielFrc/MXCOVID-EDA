import numpy as np

def calculate_bins(series_lenght):
    """
    Calculate the number of bins for a hist plot
    """
    return int(np.sqrt(series_lenght))

def calculate_ecdf(data):
    """
    Compute ECDF for a one-dimensional array of measurements.
    """
    n = len(data)

    x = np.sort(data)

    y = np.arange(1, len(x) + 1) / n

    return x, y 

def calculate_mean(data):
    """
    Compute mean for a one-dimensional array of measurements
    Parameters:
        data (np.array): one-dimensional array to calculate mean
    Return:
        mean (float): mean of the array
    """
    #Calculate and return mean
    return np.mean(data)


def calculate_median(data):
    """
    Compute mean for a one-dimensional array of measurements
    Parameters:
        data (np.array): one-dimensional array to calculate mean
    Return:
        mean (float): mean of the array
    """
    #Calculate and return median
    return np.median(data)


def calculate_percentiles(data, percentiles):
    """
    Compute percentiles for a one-dimensional array of measurements
    Parameters:
        data (np.array): one-dimensional array to calculate percentiles
        percentiles (float[]): float array with the percentiles to calculate
    Return:
        p (np.array): label for percentiles
        p_data (np.array): Percentiles
    """
    #Converting to a np.array
    p = np.array(percentiles)
    
    #Generating percentiles
    p_data = np.percentile(data,p)

    #return percentiles and labels
    return p, p_data

def calculate_var_std (data):
    """
    Compute variation and standard deviation for a one-dimensional array of measurments
    Parameters:
        data (np.array): one-dimensional array to calculate median and standard deviation
    Return:
        var (float): Variance of the data array
        std (float): std of the data array
    """
    #Calculating variance with np.var
    var = np.var(data)

    #Calculating variance with np.std
    std = np.std(data)

    #returning values
    return var, std

def calculate_cov_cof (x,y):
    """
    Compute variation and standard deviation for a one-dimensional array of measurments
    Parameters:
        x (np.array): first one-dimensional array to calculate covariance
        x (np.array): second one-dimensional array to calculate covariance
    Return:
        cov (float): Covariance of the data array
        coef (float): Correlation Coeficient of the data array
    """
    #Calculating variance with np.var
    cov = np.cov(x,y)

    #Calculating variance with np.std
    coff = np.corrcoef(x,y)

    #returning values
    return cov[0,1], coff[0,1]