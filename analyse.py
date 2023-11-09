import pickle
import pandas
import matplotlib.pyplot as plt
import numpy as np
import plotnine
import plotly.express as px


def load_from_pickle():
    with open("bristol_daily.p", "rb") as f:
        data = pandas.read_pickle(f)
    return data


def pre_process(df):
    # Plot just October
    df = df.reset_index()
    df["month"] = df["time"].map(lambda x: x.month)
    df["year"] = df["time"].map(lambda x: x.year)
    df["day_of_month"] = df["time"].map(lambda x: x.day)
    df['time_of_year'] = df['time'].map(lambda x: x.strftime('%Y-%m'))
    return df

def tmp_subplots(df,fields=["tavg", "tmax", "tmin"]):
    fig, axes = plt.subplots(len(fields), 1, sharex=True)
    for i, name in enumerate(fields):
        ax = axes[i] if len(fields)>1 else axes
        # plot the selected field
        tmp_plot_group(df[[name,'year','time_of_year']],ax)
        ax.set_title(name)
    plt.show()

def tmp_plot_group(df,ax):
    # use a group to get more control: 
    df_years = df.groupby('year')
    for i, (year, df_year) in enumerate(df_years):
        col = "red" if year == 2022 else 'grey'
        alpha = 0.1+i*0.6/len(df_years)
        df_year.set_index('time_of_year', inplace=True)

        df_year.drop(['year'],axis=1).plot(ax=ax, alpha=alpha, color = col,legend=False)

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def tmp_subplots_animate(df,fields=["tavg", "tmax", "tmin"], frames=None):
    # create the figure and the subplots
    fig, axes = plt.subplots(len(fields), 1, sharex=True)

    # create the function that will be called each time the animation is updated
    def update(num):
        # iterate over the subplots
        for i, name in enumerate(fields):
            ax = axes[i] if len(fields)>1 else axes
            # clear the subplot
            ax.clear()
            # plot the data for the current frame
            tmp_plot_group(df[[name,'year','time_of_year']].iloc[frames[num]], ax)
            ax.set_title(name)

    # create the animation
    animation = FuncAnimation(fig, update, frames=range(len(frames)), interval=100)
    plt.show()

if __name__ == "__main__":
    tmp_subplots_animate(pre_process(load_from_pickle()), frames=range(50))
