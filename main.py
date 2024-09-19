from src.proccess_csv import process_data
from sklearn.metrics.pairwise import cosine_similarity

if __name__ == "__main__":
    df_movies, columndictionary = process_data()
    genre_columns = df_movies.columns[21:]

    user_preference = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0]
    df_movies['similarity'] = cosine_similarity([user_preference], df_movies[genre_columns])[0]

    top_n_recommendation = df_movies[['title', 'similarity']].sort_values(by='similarity', ascending=False).head(10)
    print(top_n_recommendation)