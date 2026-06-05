# 🎬 Advanced Movie Recommendation System
# Interactive + Rating Based + Genre Based

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------------
# Movie Dataset
# -----------------------------------

movies = {
    "Movie": [
        "Inception",
        "Titanic",
        "Avengers",
        "Interstellar",
        "Batman",
        "Joker",
        "Iron Man",
        "The Notebook",
        "Avatar",
        "Doctor Strange"
    ],

    "Genre": [
        "Sci-Fi Action",
        "Romance Drama",
        "Action Adventure",
        "Sci-Fi Drama",
        "Action Crime",
        "Crime Thriller",
        "Action Sci-Fi",
        "Romance Drama",
        "Sci-Fi Adventure",
        "Fantasy Sci-Fi"
    ],

    "Rating": [
        8.8,
        7.9,
        8.0,
        8.7,
        8.2,
        8.5,
        7.9,
        7.8,
        7.8,
        7.5
    ]
}

df = pd.DataFrame(movies)

# -----------------------------------
# Convert Genre into Numeric Matrix
# -----------------------------------

cv = CountVectorizer()
matrix = cv.fit_transform(df["Genre"])

# -----------------------------------
# Similarity Matrix
# -----------------------------------

similarity = cosine_similarity(matrix)

# -----------------------------------
# Recommendation Function
# -----------------------------------

def recommend(movie_name):

    movie_name = movie_name.lower()

    # Check movie exists
    if movie_name not in df["Movie"].str.lower().values:
        print("\n❌ Movie Not Found!")
        return

    # Movie Index
    index = df[df["Movie"].str.lower() == movie_name].index[0]

    # Similarity Scores
    distances = list(enumerate(similarity[index]))

    # Sort by Similarity
    sorted_movies = sorted(
        distances,
        key=lambda x: x[1],
        reverse=True
    )

    print("\n🎯 Top Recommended Movies:\n")

    count = 0

    for movie in sorted_movies[1:]:

        movie_index = movie[0]

        print(
            f"🎬 {df.iloc[movie_index]['Movie']}"
        )

        print(
            f"📂 Genre : {df.iloc[movie_index]['Genre']}"
        )

        print(
            f"⭐ Rating : {df.iloc[movie_index]['Rating']}"
        )

        print("-" * 35)

        count += 1

        if count == 5:
            break


# -----------------------------------
# Display Movies
# -----------------------------------

print("=" * 60)
print("        🎥 MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)

print("\n📌 Available Movies:\n")

for movie in df["Movie"]:
    print("👉", movie)

# -----------------------------------
# User Interaction Loop
# -----------------------------------

while True:

    choice = input(
        "\n🎞️ Enter Movie Name: "
    )

    recommend(choice)

    again = input(
        "\n🔁 Want More Recommendations? (yes/no): "
    ).lower()

    if again != "yes":
        print("\n👋 Thanks for Using Movie Recommendation System!")
        break
