from src.proccess_csv import process_data
from sklearn.metrics.pairwise import cosine_similarity
from src.feature_extraction import get_genres

if __name__ == "__main__":
    df_movies, columndictionary = process_data()
    genre_columns = df_movies.columns[21:]

    # Test input:
    # I think i like movies that are in the genre of action fantasy, maybe some thriller and drama
    user_input = input("What genres do you like in a movie:\n")
    user_preference = get_genres(user_input, columndictionary)
    df_movies['similarity'] = cosine_similarity([user_preference], df_movies[genre_columns])[0]

    top_n_recommendation = df_movies[['title', 'similarity']].sort_values(by='similarity', ascending=False).head(10)
    print(top_n_recommendation)