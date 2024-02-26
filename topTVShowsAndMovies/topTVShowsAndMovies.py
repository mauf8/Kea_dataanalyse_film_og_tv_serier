import pandas as pd
import matplotlib.pyplot as plt

readData = pd.read_csv("../ExcelMovieFile/flixpatrol.csv")

def plotTopTVShowsAndMovies(): 
    # Convert 'Watchtime in Million' to numeric values
    readData['Watchtime in Million'] = pd.to_numeric(readData['Watchtime in Million'].str.replace('M', ''))

    # Sort the data by 'Watchtime' column in descending order
    sorted_data = readData.sort_values(by='Watchtime in Million', ascending=False)

    # Plot the bar chart for top TV shows and movies
    plt.figure(figsize=(12, 8))

    # Plot top TV shows
    top_tv_shows = sorted_data[sorted_data['Type'] == 'TV Show'].head(10)
    plt.bar(top_tv_shows['Title'] + ' (' + top_tv_shows['Genre'] + ')', top_tv_shows['Watchtime in Million'], color='skyblue', label='TV Shows')

    # Plot top movies
    top_movies = sorted_data[sorted_data['Type'] == 'Movie'].head(10)
    plt.bar(top_movies['Title'] + ' (' + top_movies['Genre'] + ')', top_movies['Watchtime in Million'], color='orange', label='Movies')

    # Labels and legend
    plt.title('Top TV Shows and Movies Based on Viewing Time')
    plt.xlabel('Title (Genre)')
    plt.ylabel('Watchtime in Million')
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.show()

plotTopTVShowsAndMovies()
