# import libraries
import pickle
import urllib.request
from typing import Any, Dict, List, Tuple

import bs4 as bs
import numpy as np
import pandas as pd

# import flask
from flask import Flask, render_template, request

# import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class MovieRecommender:
    """
    A class to handle movie recommendations and sentiment analysis.
    """

    def __init__(self, nlp_model_path: str, vectorizer_path: str, data_path: str):
        """
        Initializes the MovieRecommender with the necessary models and data.

        Args:
            nlp_model_path: Path to the NLP model file.
            vectorizer_path: Path to the Tfidf vectorizer file.
            data_path: Path to the movie data CSV file.
        """
        self.clf = self._load_model(nlp_model_path)
        self.vectorizer = self._load_model(vectorizer_path)
        self.data, self.similarity = self._create_similarity_matrix(data_path)

    def _load_model(self, model_path: str) -> Any:
        """
        Loads a pickled model from the given path.

        Args:
            model_path: The path to the model file.

        Returns:
            The loaded model.
        """
        try:
            with open(model_path, "rb") as f:
                return pickle.load(f)
        except IOError:
            print(f"Model file not found at {model_path}")
            exit()

    def _create_similarity_matrix(
        self, data_path: str
    ) -> Tuple[pd.DataFrame, np.ndarray]:
        """
        Creates a cosine similarity matrix from the movie data.

        Args:
            data_path: The path to the movie data CSV file.

        Returns:
            A tuple containing the movie data and the similarity matrix.
        """
        data = pd.read_csv(data_path)
        cv = TfidfVectorizer()
        count_matrix = cv.fit_transform(data["comb"])
        similarity = cosine_similarity(count_matrix)
        return data, similarity

    def recommend(self, movie_title: str) -> List[str]:
        """
        Recommends movies similar to the given movie title.

        Args:
            movie_title: The title of the movie to get recommendations for.

        Returns:
            A list of recommended movie titles.
        """
        movie_title = movie_title.lower()
        if movie_title not in self.data["movie_title"].unique():
            return []
        else:
            i = self.data.loc[self.data["movie_title"] == movie_title].index[0]
            lst = list(enumerate(self.similarity[i]))
            lst = sorted(lst, key=lambda x: x[1], reverse=True)
            lst = lst[1:11]
            return [self.data["movie_title"][i[0]] for i in lst]

    def get_suggestions(self) -> List[str]:
        """
        Gets a list of movie titles for autocomplete suggestions.

        Returns:
            A list of movie titles.
        """
        return list(self.data["movie_title"].str.capitalize())

    def get_movie_reviews(self, imdb_id: str) -> Dict[str, str]:
        """
        Scrapes and analyzes movie reviews from IMDb.

        Args:
            imdb_id: The IMDb ID of the movie.

        Returns:
            A dictionary of reviews and their sentiment.
        """
        sauce = urllib.request.urlopen(
            f"https://www.imdb.com/title/{imdb_id}/reviews?ref_=tt_ov_rt"
        ).read()
        soup = bs.BeautifulSoup(sauce, "lxml")
        soup_result = soup.find_all("div", {"class": "text show-more__control"})

        reviews_list = []
        reviews_status = []
        for review in soup_result:
            if review.string:
                reviews_list.append(review.string)
                movie_review_list = np.array([review.string])
                movie_vector = self.vectorizer.transform(movie_review_list)
                pred = self.clf.predict(movie_vector)
                reviews_status.append("Good" if pred else "Bad")

        return {reviews_list[i]: reviews_status[i] for i in range(len(reviews_list))}


app = Flask(
    __name__, template_folder="../../../templates", static_folder="../../../static"
)


def get_recommender():
    """
    Gets the recommender instance.
    """
    return MovieRecommender("nlp_model.pkl", "tranform.pkl", "main_data.csv")


def _convert_to_list(my_list: str) -> List[str]:
    """
    Converts a string representation of a list to a Python list.

    Args:
        my_list: The string to convert.

    Returns:
        A list of strings.
    """
    my_list = my_list.split('","')
    my_list[0] = my_list[0].replace('["', "")
    my_list[-1] = my_list[-1].replace('"]', "")
    return my_list


@app.route("/")
@app.route("/home")
def home():
    """
    Renders the home page.
    """
    suggestions = get_recommender().get_suggestions()
    return render_template("home.html", suggestions=suggestions)


@app.route("/similarity", methods=["POST"])
def similarity():
    """
    Gets movie recommendations.
    """
    movie = request.form["name"]
    rc = get_recommender().recommend(movie)
    if not rc:
        return "Sorry! The movie you requested is not in our database. Please check the spelling or try with some other movies"
    else:
        return "---".join(rc)


@app.route("/recommend", methods=["POST"])
def recommend():
    """
    Renders the recommend page with movie details and reviews.
    """
    title = request.form["title"]
    imdb_id = request.form["imdb_id"]
    rec_movies = _convert_to_list(request.form["rec_movies"])
    rec_posters = _convert_to_list(request.form["rec_posters"])
    cast_names = _convert_to_list(request.form["cast_names"])
    cast_chars = _convert_to_list(request.form["cast_chars"])
    cast_profiles = _convert_to_list(request.form["cast_profiles"])
    cast_bdays = _convert_to_list(request.form["cast_bdays"])
    cast_bios = _convert_to_list(request.form["cast_bios"])
    cast_places = _convert_to_list(request.form["cast_places"])
    cast_ids = request.form["cast_ids"].split(",")
    cast_ids[0] = cast_ids[0].replace("[", "")
    cast_ids[-1] = cast_ids[-1].replace("]", "")

    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r"\n", "\n").replace(r"\"", '"')

    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}
    casts = {
        cast_names[i]: [cast_ids[i], cast_chars[i], cast_profiles[i]]
        for i in range(len(cast_profiles))
    }
    cast_details = {
        cast_names[i]: [
            cast_ids[i],
            cast_profiles[i],
            cast_bdays[i],
            cast_places[i],
            cast_bios[i],
        ]
        for i in range(len(cast_places))
    }
    movie_reviews = get_recommender().get_movie_reviews(imdb_id)

    return render_template(
        "recommend.html",
        title=title,
        poster=request.form["poster"],
        overview=request.form["overview"],
        vote_average=request.form["rating"],
        vote_count=request.form["vote_count"],
        release_date=request.form["release_date"],
        runtime=request.form["runtime"],
        status=request.form["status"],
        genres=request.form["genres"],
        movie_cards=movie_cards,
        reviews=movie_reviews,
        casts=casts,
        cast_details=cast_details,
    )


if __name__ == "__main__":
    app.run(debug=True)
