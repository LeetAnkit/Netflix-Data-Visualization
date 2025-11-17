
# step 1 -> import the required libraries
import pandas as pd
import matplotlib.pyplot as plt 

#2 Step 2 -> Load the dataset
df = pd.read_csv("Netflix_data_visualization/netflix_titles.csv")
#3 Step 3 -> cleaning the data

df = df.dropna(subset = ['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'release_year', 'rating', 'duration', 'listed_in','description' ])

type_counts = df['type'].value_counts()
plt.figure(figsize=(6, 4))
plt.bar(type_counts.index, type_counts.values, color =['skyblue', 'red'])
plt.title("Number of Movies and TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("netflix_type_distribution.png")
plt.show()


rating_counts = df['rating'].value_counts()
plt.figure(figsize=(10, 6))
plt.pie(rating_counts, labels= rating_counts, autopct='%1.1f%%', startangle=140)
plt.title("Percentage of Content Ratings on Netflix using pie chart")
plt.tight_layout()
plt.savefig("netflix_rating_distribution_pie_chart.png")
plt.show()



movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration'] = movie_df['duration'].str.replace(' min', '').astype(int)
plt.figure(figsize=(10, 6))
plt.hist(movie_df['duration'], bins=30, color='green', edgecolor='black')
plt.title("Distribution of Movie Durations on Netflix")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")  
plt.tight_layout()
plt.savefig("netflix_movie_duration_distribution.png")
plt.show()



release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6)) 
plt.scatter(release_year_counts.index, release_year_counts.values, marker='o', linestyle='-', color='purple')
plt.title("Number of Titles Released Each Year on Netflix")     
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("netflix_titles_per_year(Scattered).png")
plt.show()

release_year_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(12, 6)) 
plt.plot(release_year_counts.index, release_year_counts.values, marker='o', linestyle='-', color='purple')
plt.title("Number of Titles Released Each Year on Netflix")     
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.savefig("netflix_titles_per_year(Plot).png")
plt.show()



country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title("Top 10 Countries Producing Netflix Content") 
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("netflix_top_countries.png")
plt.show()


# compute number of titles per year split by type (Movie / TV Show)
content_by_year = df.groupby(['release_year', 'type']).size().unstack(fill_value=0)

# ensure the expected columns exist (dataset uses 'Movie' and 'TV Show')
movies = content_by_year['Movie'] if 'Movie' in content_by_year.columns else pd.Series(0, index=content_by_year.index)
tvshows = content_by_year['TV Show'] if 'TV Show' in content_by_year.columns else pd.Series(0, index=content_by_year.index)

# create two stacked subplots
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

# first subplot is movies
ax[0].plot(content_by_year.index, movies, color='blue')
ax[0].set_title("Number of Movies Released Each Year on Netflix")
ax[0].set_ylabel("Number of Movies")
ax[0].grid(color='gray', linestyle='--', linewidth=0.5)

# second subplot is TV shows
ax[1].plot(content_by_year.index, tvshows, color='orange')
ax[1].set_title("Number of TV Shows Released Each Year on Netflix")
ax[1].set_xlabel("Release Year")
ax[1].set_ylabel("Number of TV Shows")
ax[1].grid(color='gray', linestyle='--', linewidth=0.5)

fig.suptitle("Comparison of Movies vs TV Shows Released Each Year on Netflix", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("netflix_movies_tvshows_per_year.png")

plt.show()