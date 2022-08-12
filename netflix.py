#Netflix! 
# What started in 1997 as a DVD rental service has since exploded into the largest entertainment/media company by market capitalization, boasting over 200 million subscribers as of January 2021.
# Given the large number of movies and series available on the platform, it is a perfect opportunity to flex our data manipulation skills and dive into the entertainment industry. Our friend has also been brushing up on their Python skills and has taken a first crack at a CSV file containing Netflix data. For their first order of business, they have been performing some analyses, and they believe that the average duration of movies has been declining.

# Import pandas under its usual alias
import pandas as pd
# Import matplotlib.pyplot under its usual alias and create a figure
import matplotlib.pyplot as plt
fig = plt.figure()

# Create the years and durations lists
years = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
durations = [103, 101, 99, 100, 100, 95, 95, 96, 93, 90]

# Create a dictionary with the two lists
movie_dict = {"years": years, "durations": durations}

# Print the dictionary
print(movie_dict)

# Create a DataFrame from the dictionary
durations_df = pd.DataFrame(movie_dict)

# Print the DataFrame
print(durations_df)

# Draw a line plot of release_years and durations
plt.plot(years, durations)

# Create a title
plt.title("Netflix Movie Durations 2011-2020")

# Show the plot
plt.show()

# Read in the CSV as a DataFrame
netflix_df = pd.read_csv(r"Datasets/netflix_data.csv", index_col = 0)

# Print the first five rows of the DataFrame
print(netflix_df[:5])

# Subset the DataFrame for type "Movie"
netflix_df_movies_only = netflix_df[netflix_df["type"].isin(["Movie"])] 

# Select only the columns of interest
netflix_movies_col_subset = netflix_df_movies_only[['title', 'country', 'genre', 'release_year', 'duration']]

# Print the first five rows of the new DataFrame
print(netflix_movies_col_subset[:5])

# Create a figure and increase the figure size
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus year
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]])

# Create a title
plt.title("Movie Duration by Year of Release")

# Show the plot
plt.show()

# Filter for durations shorter than 60 minutes
short_movies = netflix_movies_col_subset[netflix_movies_col_subset["duration"] < 60]

# Print the first 20 rows of short_movies
print(short_movies[:20])

# Define an empty list
colors = []

# Iterate over rows of netflix_movies_col_subset
for row, ser in netflix_movies_col_subset.iterrows() :
    if ser['genre'] == "Children" :
        colors.append("red")
    elif ser['genre'] == "Documentaries" :
        colors.append("blue")
    elif ser['genre'] == "Stand-Up" :
        colors.append("green")
    else:
        colors.append("black")
        
# Inspect the first 10 values in your list        
print(colors[:10])

# Set the figure style and initalize a new figure
plt.style.use('fivethirtyeight')
fig = plt.figure(figsize=(12,8))

# Create a scatter plot of duration versus release_year
plt.scatter(netflix_movies_col_subset[["release_year"]], netflix_movies_col_subset[["duration"]], c = colors)

# Create a title and axis labels
plt.title("Movie duration by year of release")
plt.xlabel("Release year")
plt.ylabel("Duration (min)")

# Show the plot
plt.show()

# Are we certain that movies are getting shorter?
are_movies_getting_shorter = "yes"