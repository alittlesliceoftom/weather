import pickle
import pandas
import matplotlib.pyplot as plt
import numpy as np


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

def tmp_subplots(df):
    fig, axes = plt.subplots(3, 1, sharex=True)
    for i, name in enumerate(["tavg", "tmax", "tmin"]):
        # plot the selected field
        tmp_plot_group(df[[name,'year','time_of_year']],axes[i])
    plt.show()


# def tmp_plot_cmap(df):
#     # Plot line chart including average, minimum and maximum temperature

#     fig, axes = plt.subplots(3, 1, sharex=True)
#     for i, name in enumerate(["tavg", "tmax", "tmin"]):
#         temps = df.pivot(["month", "day_of_month"], columns="year", values=name)
#         palette = {
#             y: "red" if y == 2022 else f"{str(0.9-(y-2000)/40)}"
#             for y in df.year.unique()
#         }
#         temps.plot(color=palette, ax=axes[i], alpha = 0.7,legend=False)
#     plt.show()
#     plt.tight_layout()

def tmp_plot_group(df,ax):
    # use a group to get more control: 
    df_years = df.groupby('year')
    for i, (year, df_year) in enumerate(df_years):
        col = "red" if year == 2022 else 'grey'
        alpha = 0.1+i*0.6/len(df_years)
        df_year.set_index('time_of_year', inplace=True)
        print(df_year.head())

        df_year.drop(['year'],axis=1).plot(ax=ax, alpha=alpha, color = col,legend=False)
 
# def animate():

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)

if __name__ == "__main__":
    tmp_subplots(pre_process(load_from_pickle()))
