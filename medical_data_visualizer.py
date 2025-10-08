import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1) Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')

# 2) Add an overweight column
# BMI = weight(kg) / (height(m) ** 2). If BMI > 25 then overweight=1 else 0.
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# 3) Normalize data: make 0 always good and 1 always bad for cholesterol and gluc.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)


def draw_cat_plot():
    """
    Draw the categorical plot and return the Matplotlib figure object.
    """

    # 4) Create DataFrame for cat plot using pd.melt with the required columns.
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    )

    # 5) Group and reformat the data to get counts per (cardio, variable, value)
    df_cat = (
        df_cat
        .groupby(['cardio', 'variable', 'value'])
        .size()
        .reset_index(name='total')
    )

    # 6) Draw the categorical plot using seaborn.catplot
    catplot = sns.catplot(
        data=df_cat,
        x='variable',
        y='total',
        hue='value',
        col='cardio',
        kind='bar'
    )

    # 7) Get the figure for the output
    fig = catplot.fig

    # Do not modify the next two lines (project requirement)
    # fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    """
    Draw the heat map (correlation matrix) and return the Matplotlib figure object.
    """

    # Clean the data as required:

    # - Keep rows where ap_lo <= ap_hi (diastolic <= systolic).
    df_heat = df[df['ap_lo'] <= df['ap_hi']].copy()

    # - Remove height outliers outside 2.5th-97.5th percentiles:
    h_low = df_heat['height'].quantile(0.025)
    h_high = df_heat['height'].quantile(0.975)
    df_heat = df_heat[(df_heat['height'] >= h_low) & (df_heat['height'] <= h_high)]

    # - Remove weight outliers outside 2.5th-97.5th percentiles:
    w_low = df_heat['weight'].quantile(0.025)
    w_high = df_heat['weight'].quantile(0.975)
    df_heat = df_heat[(df_heat['weight'] >= w_low) & (df_heat['weight'] <= w_high)]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw the heatmap with seaborn
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt='.1f',
        vmax=0.3,
        center=0,
        square=True,
        linewidths=.5,
        cbar_kws={'shrink': .5}
    )

    # Do not modify the next two lines (project requirement)
    # fig.savefig('heatmap.png')
    return fig
