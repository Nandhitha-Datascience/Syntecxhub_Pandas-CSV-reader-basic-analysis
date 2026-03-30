import pandas as pd

##Loading data
data=pd.read_csv("moviesDB.csv")
print(data.head())

##Top 5 movies
print("Top 5 movies:")
print(data.sort_values(by="Rating", ascending=False)[["title","Rating"]].head())


##inspecting head/tail/types
print(data.head())
print(data.tail())
print(data.info())


##Compute summary stats
print("Mean:\n " ,data.mean(numeric_only=True))
print("Median:\n " ,data.median(numeric_only=True))
print("Minimum:\n " ,data.min(numeric_only=True))
print("Maximum:\n " ,data.max(numeric_only=True))
print("Count:\n", data.count())


##Filter rows, select columns and slice subsets
highly_rated=data[data["Rating"]>9]
print(highly_rated)
movies=data[data["year"]>2015]
print(movies)
selected=data[["year","title","genres"]]
print("selected columns:\n " ,selected)
subset=data.iloc[:10]
print(subset)


##Saving filtered and selected results to CSV/excel
highly_rated.to_csv("highly_rated_movies.csv", index=False)
movies.to_csv("movies_after_2015.csv", index=False)
selected.to_excel("selected_movies.xlsx", index=False)
