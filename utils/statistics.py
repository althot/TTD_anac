import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

def statistics(df, perc_categorical=0.80):
    """
    Get input a dataframe and foreach column make statistics

    Parameters
    ---------
    df: pandas.Dataframe
    Dataframe objects of statistics
    perc_categorical: float
    Upper bound of unique record, under that percentage a fields is categorical

    Return
    ------
    pandas.Dataframe
    A data frame of statistics
    
    """
    n, m =df.shape
    result = pd.DataFrame(columns =('Fields', 'Unique Row','% Unique', 'N° Missing', '% Missing', 'Field Type','Max','Min','Mean','Var','Kurt'))
    cols = list(df.columns)
    # For each filed infer type
    for i in range (0,len(cols)):
        # Categorical: if unique elements are less than specific perc 
        # String: if a sum of column is a string
        # Numeric: Default
        cnt = len(df[cols[i]].value_counts(dropna=False))
        missing = df[cols[i]].isnull().sum()
        perc_cnt = float(cnt) /float(n)
        col_max = 0
        col_min = 0
        col_mean = 0
        col_var = 0
        col_kur = 0
        if  perc_cnt < perc_categorical:
            fields_type="Categorical"
        elif isinstance(df[cols[i]].sum(), str):
            fields_type="String"
        else:
            fields_type="Numeric"
            col_max=df[cols[i]].max()
            col_min=df[cols[i]].min()
            col_mean=df[cols[i]].mean()  
            col_var=df[cols[i]].var()
            col_kur=df[cols[i]].kurtosis()
        
        result.loc[i] = [cols[i], cnt, perc_cnt, missing, float(missing)/float(n), fields_type, col_max, col_min, col_mean, col_var, col_kur]
    return result

def optimize_width(X):
    """Get number of element of abscisssa and return optimal width of histogram"""
    i = 6
    while ((i/0.70)<len(X)):
        i+=1
    return i

def bar_chart_simple(col, title, p_xlabel='', p_ylabel='Frequenza'):
    """
    Print a bar chart

    Parameters
    ---------
    col: pandas.Series
        Series of data
    title: String
        Title of plot
    p_xlabel: String
        Label for x
    p_ylabel: String
        Label for y

    """
    x = [i for i in range(1,len(col.index)+1)]
    xlabels=list(col.index)
    y = col.values
    tot=col.sum()
    for i in range(0, len(y)):
        xlabels[i] = "%.2f\n%s" %(float(y[i])/float(tot), str(xlabels[i]).replace(" ","\n"))

    plt.figure(figsize=(optimize_width(x), 4))
    plt.bar(x,y, label=p_ylabel)
    plt.xlabel(p_xlabel)
    plt.xticks(x, xlabels)
    plt.ylabel(p_ylabel)
    plt.title(title)
    plt.legend()
    
    plt.show()