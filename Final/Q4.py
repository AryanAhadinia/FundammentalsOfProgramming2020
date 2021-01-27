"""
Question 4: Tehran Air Polution
@author: Mohsen Hosseini
@author: Aryan Ahadinia
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# root = str(os.path.dirname(os.path.abspath(__file__))) + '\\'
# station = 'pirouzi'


def get_dataframe(root: str, station: str):
    return pd.read_csv(root + station + '.csv')


def filter91(root: str, station: str):
    d = pd.read_csv(station + '.csv')
    d['year'] = d['date'].apply(lambda x: x[:4]).astype(int)
    a = d[d['year'] > 1390]
    return a


def notnull_percent(root: str, station: str):
    a = filter91(station)
    values = dict()
    for item in a.columns[:-1]:
        values[item] = (int((a[item].count() / len(a[item]) * 100)))
    return values


def plots(root: str, station: str):
    a = filter91(station)

    a['number'] = range(1, len(a) + 1)

    plt.figure(dpi=100)
    plt.plot(a['number'], a['NO2'], alpha=0.8)
    plt.legend(['NO2'])
    plt.title(station)
    plt.show()

    plt.figure(dpi=100)
    plt.plot(a['number'], a['PM2.5'], alpha=0.8)
    plt.legend(['PM2.5'])
    plt.title(station)
    plt.show()

    plt.figure(dpi=100)
    plt.plot(a['number'], a['NO2'], alpha=0.7)
    plt.plot(a['number'], a['PM2.5'], alpha=0.7)
    plt.legend(['NO2', ['PM2.5']])
    plt.title(station)
    plt.show()


def change_percent(root: str, station: str):
    a = filter91(station)
    values = dict()
    for item in a.columns[1:-1]:
        second = a[(a['year'] >= 1397) & (~a[item].isna())][item].mean()
        first = a[(a['year'] < 1397) & (~a[item].isna())][item].mean()
        values[item] = round((second - first) / first * 100, 1)

    return values
