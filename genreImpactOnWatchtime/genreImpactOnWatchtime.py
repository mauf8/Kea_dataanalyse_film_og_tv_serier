import pandas as pd
import matplotlib.pyplot as plt

readData = pd.read_csv("../ExcelMovieFile/flixpatrol.csv")

def genreImpactOnWatchTime():
    readData['Watchtime in Million'] = pd.to_numeric(readData['Watchtime in Million'].str.replace('M', ''))

    average_watchtime_per_genre = readData.groupby('Genre')['Watchtime in Million'].mean()

    plt.figure(figsize=(14, 8))
    average_watchtime_per_genre.sort_values().plot(kind='barh', color='skyblue')

    plt.title('Genre Impact on Watch Time')
    plt.xlabel('Average Watchtime in Million')
    plt.ylabel('Genre')
    plt.show()

# Call the function
genreImpactOnWatchTime()
