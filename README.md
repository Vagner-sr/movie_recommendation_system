# Movie Recommendation System

This is a simple movie recommendation system built using Python and Streamlit. It recommends similar movies based on the selected movie.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Technologies Used](#technologies-used)

## Introduction

The Movie Recommendation System uses cosine similarity to recommend movies similar to the one selected by the user. It utilizes a dataset containing movie information such as title, overview, genres, keywords, cast, and crew. The system vectorizes the textual data and computes cosine similarity scores between movies to generate recommendations.

## Setup

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using the command `streamlit run app.py`.

## Usage

1. Upon running the Streamlit app, you will see a dropdown menu to select a movie.
2. Choose a movie from the dropdown menu and click the "Select" button.
3. The system will display a list of recommended movies similar to the selected movie.

## File Descriptions

- `app.py`: Contains the Streamlit app code for the movie recommendation system.
- `movies.csv`: Dataset containing movie information such as title, overview, genres, keywords, cast, and crew.
- `credits.csv`: Dataset containing credits information for movies.

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- NLTK

