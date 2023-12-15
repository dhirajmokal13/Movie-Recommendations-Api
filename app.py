from flask import Flask, jsonify, request
import pickle
import pandas as pd
app = Flask(__name__)

movies_list = pickle.load(open('movies.pkl', 'rb'))  #get movies list
movies = pd.DataFrame(movies_list) #convert it to panda dataframe
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    recommendations = []
    movie_index = movies[movies['imdbID'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),
                         reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        recommendations.append(movies.iloc[i[0]].to_dict())
    return recommendations

@app.route("/recommendation", methods=['GET'])
def recommendation():
    imdbID = request.args.get('imdbID')
    print(imdbID)
    if (imdbID in movies['imdbID'].values):
        data = recommend(imdbID)
        return jsonify({'Found': True, 'data': data})
    else:
        return jsonify({'Found': False})

@app.route("/randoms", methods=['GET'])
def randomMovies():
    return jsonify({'Found': True, 'data': movies.sample(n=20).to_dict(orient='records')}) #It will get Random 20 movies from dataframe and returns

if __name__ == '__main__':
    app.run(debug=True)