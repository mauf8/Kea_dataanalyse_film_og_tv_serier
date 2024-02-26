import pandas as pd
import matplotlib.pyplot as plt

readData = pd.read_csv("../ExcelMovieFile/flixpatrol.csv")


def compareWatchTime():
    readData['Watchtime in Million'] = pd.to_numeric(readData['Watchtime in Million'].str.replace('M', ''))

    total_watchtime = readData.groupby('Type')['Watchtime in Million'].sum()

    plt.figure(figsize=(8, 8))
    plt.pie(total_watchtime, labels=total_watchtime.index, autopct='%1.1f%%', colors=['skyblue', 'orange'])

    plt.title('Comparison of Watch Time: TV Shows vs Movies')

    plt.show()


compareWatchTime()


