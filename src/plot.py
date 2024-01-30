import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px


def correlation_matrix(df):
    corr = df.corr()
    cm = sns.heatmap(corr, annot = True,cmap = 'viridis')
    plt.show()
    return corr, cm

def listAll(df, max_plots=16):

    # Calculate the number of plots to display (up to 16)
    num_plots = min(len(df.columns), max_plots)

    nrows = int(np.ceil(num_plots / 4))
    ncols = min(num_plots, 4)

    fig, axes = plt.subplots(nrows, ncols, figsize=(4 * ncols, 4 * nrows))
    fig.suptitle('Different feature distributions')

    # if only one plot, convert to list
    if num_plots == 1:
        axes = [axes]

    # Flatten the axes array
    axes = axes.flatten()

    # Display the histograms
    for i, column in enumerate(df.columns[:num_plots]):
        sns.histplot(ax=axes[i], data=df, x=column)

    # Hide additional subplots
    for ax in axes[num_plots:]:
        ax.axis('off')

    plt.tight_layout()
    plt.show()

import plotly.express as px

def count_Y(df, Y_name, mapping = None):
    """
    Display the distribution of the target variable in a pie chart using matplotlib.
    Applies a mapping to the labels if provided.

    Args:
    df (DataFrame): The DataFrame containing the data.
    Y_name (str): The name of the target variable.
    mapping (dict, optional): A dictionary to map the target variable's values.
    """
    if Y_name in df.columns and df[Y_name].nunique() >= 1:
        
        mapped_data = df[Y_name].map(mapping[Y_name]) if mapping and Y_name in mapping else df[Y_name]
        value_counts = mapped_data.value_counts()
        
        print(value_counts)
        plt.figure(figsize=(8, 8))
        plt.pie(value_counts, labels=value_counts.index, startangle=90, autopct='%1.1f%%')
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f'Distribution of {Y_name}')
        plt.show()