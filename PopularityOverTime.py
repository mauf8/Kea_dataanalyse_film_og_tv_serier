import pandas as pd
import matplotlib.pyplot as plt

readData = pd.read_csv("ExcelMovieFile/flixpatrol.csv")

def popularityEvolutionOverTime():
    readData['Watchtime in Million'] = pd.to_numeric(readData['Watchtime in Million'].str.replace('M', ''))

    filtered_data = readData[readData['Premiere'] >= 2000]

    pivot_data = filtered_data.pivot_table(index='Premiere', columns='Genre',values='Watchtime in Million', aggfunc='sum', fill_value=0)

    fig, ax = plt.subplots(figsize=(15, 10))
    pivot_data.plot.area(stacked=True, colormap='tab20', alpha=0.5, ax=ax)

    plt.title('Popularity Evolution of Genres Over Time (From Year 2000 Onwards)')
    plt.xlabel('Premiere Year')
    #plt.ylabel('Total Watchtime in Million')
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.tight_layout()
    plt.show()

# Call the function
popularityEvolutionOverTime()