import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
def create_movie_dataset():
    data = {
        'title': [
            'Dilwale Dulhania Le Jayenge',
            '3 Idiots',
            'Dangal',
            'Gully Boy',
            'Kabir Singh',
            'Bahubali',
            'Chak De! India',
            'Zindagi Na Milegi Dobara',
            'Sholay',
            'Andhadhun'
        ],
        'genre': [
            'romantic drama',
            'comedy drama',
            'sports drama',
            'musical drama',
            'romantic thriller',
            'epic action',
            'sports drama',
            'coming-of-age drama',
            'action adventure',
            'thriller mystery'
        ]
    }

    return pd.DataFrame(data)
def build_model(df):

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(df['genre'])


    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim
def recommend_movies(title, df, cosine_sim):

    if title not in df['title'].values:
        return ["Movie not found in dataset."]

    idx = df[df['title'] == title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":

    movie_df = create_movie_dataset()
    similarity_matrix = build_model(movie_df)

    user_input = input("Enter a movie title (e.g., '3 Idoits','Dangal','Kabir Singh): ")
    recommendations = recommend_movies(user_input, movie_df, similarity_matrix)

    print("\nRecommended movies:")
    for movie in recommendations:
        print(f"- {movie}")
