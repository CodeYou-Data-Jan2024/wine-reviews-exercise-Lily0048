import pandas as pd
reviews = pd.read_csv('data\winemag-data-130k-v2.csv.zip')
mean_points = reviews.groupby('country')['points'].mean().apply(lambda point: round(point, 1))
countries = reviews.value_counts('country')
dataframe = [countries, mean_points]
results = pd.concat(dataframe, axis = 1)
results.to_csv('data/reviews-per-country.csv')
print(results)







