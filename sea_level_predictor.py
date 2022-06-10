import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.figure(figsize=(5,5))
    plt.scatter(x,y)


    # Create first line of best fit
    result = linregress(x,y)
    x1 = pd.Series([year for year in range(x.min(), 2051)])
    y1 = result.slope*x1 + result.intercept
    plt.plot(x1,y1,"r")
    
    # Create second line of best fit
    df2 = df[df['Year'] >= 2000]
    result2 = linregress(df2['Year'] , df2['CSIRO Adjusted Sea Level'])
    x2 = pd.Series([year for year in range(2000, 2051)])
    y2 = result2.slope * x2 + result2.intercept
    plt.plot(x2,y2, "g")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title ('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()