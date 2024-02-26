import pandas as pd
import matplotlib.pyplot as plt

readData = pd.read_csv("../ExcelMovieFile/flixpatrol.csv")

def MostFrequentlyOccuringGenre():
    genre_counts = readData['Genre'].value_counts()

    plt.figure(figsize=(10,6))

    genre_counts.plot(kind='bar',color='skyblue')

    plt.title('Most Frequently Occuring Genre')
    plt.xlabel('Genre')
    plt.ylabel('Count')
    plt.show()



MostFrequentlyOccuringGenre()
