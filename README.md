#Movie Recommender System
This repository contains the code for a movie recommender system that uses content-based filtering and the TMDB movies dataset.

#Getting Started
To install the dependencies, run the following command:

pip install -r requirements.txt


To run the recommender system, run the following command:

streamlit run app.py

This will open a web browser window with the recommender system.

#How it works
The recommender system first extracts features from the movie descriptions. These features include the movie's genres, cast, crew, keywords, and taglines. The features are then used to calculate the similarity between movies.

The recommender system then recommends movies that are similar to movies that the user has already liked. To do this, the user enters a movie name, and the recommender system returns 5 most similar movies along with their posters.

#License
This project is licensed under the MIT License.
