# 1. MOVIE RECOMMENDATIONS SYSTEM

Chirag Singhal, Undergraduate Student, Department of Computer Science and Engineering, RKGIT
Ashutosh Maurya, Undergraduate Student, Department of Computer Science and Engineering, RKGIT

- [1. MOVIE RECOMMENDATIONS SYSTEM](#1-movie-recommendations-system)
  - [1.1. Abstract](#11-abstract)
  - [1.2. Introduction](#12-introduction)
  - [1.3. Data Acquisition](#13-data-acquisition)
  - [1.4. Data Preprocessing](#14-data-preprocessing)
  - [1.5. Modeling](#15-modeling)
  - [1.6. Results](#16-results)
  - [1.7. Conclusion](#17-conclusion)

## 1.1. Abstract

The main objective of this paper is to recommend movies to the user based on the content of the movie. The content-based filtering system is used to recommend movies. The main parameters that are considered for the recommendations are the genre, director, and top 3 casts. The details of the movies, such as title, genre, runtime, rating, poster, casts, etc., are fetched from TMDB. The reviews of each individual movie given by the users are "web-scraped" from the IMDB website with the help of beautifulsoup4, and the reviews are subjected to sentiment analysis, where the model predicts whether the review is positive or negative.

## 1.2. Introduction

A recommendation system is a system that is used to predict the rating or preference a user would give to an item.The main objective of a recommendation system is to get to know the user intentions and wants. A recommendation system helps in predicting what a user wants on the basis of the activity of the user and the activity of other users. There are different types of recommendation systems; we will be focusing on content-based filtering.

## 1.3. Data Acquisition

The details of the movie, such as title, genre, runtime, rating, poster, casts, etc., are fetched from TMDB. The reviews of each individual movie given by the users are "web-scraped" from the IMDB website.

## 1.4. Data Preprocessing

The data that is fetched from the TMDB is in JSON format. The JSON file is converted into a CSV file for further processing. The data that is fetched from the IMDB website is in the form of HTML. BeautifulSoup4 is used to "web-scrape" the reviews and extract the data. The reviews are subjected to sentiment analysis, where the model predicts whether the review is positive or negative.

## 1.5. Modeling

The model used in this project is a content-based filtering system. The main parameters that are considered for the recommendations are the genre, director, and top 3 casts.

## 1.6. Results

The model gives recommendations based on the genre, director, and top 3 casts of each movie. It is observed that if the genre of the movie and the genre that the user likes match, then the movie is recommended to the user. The model gives better recommendations as compared to other models.

## 1.7. Conclusion

The model that we have used is a content-based filtering system. The model gives recommendations based on the genre, director, and top 3 casts of each movie. It is observed that if the genre of the movie and the genre that the user likes match, then the movie is recommended to the user. The model gives better recommendations as compared to other models.
