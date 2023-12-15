import pickle
import pandas as pd


def recommend(movie):
    recommendations = []
    movie_index = movies[movies['imdbID'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].to_dict())
    return recommendations


movies_list = pickle.load(open('movies.pkl', 'rb'))  # get movies list
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))
id_available = 'tt0468569' in movies['imdbID'].values

print(recommend('tt0468569'))
print(id_available)
