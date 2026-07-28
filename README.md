# CineSense

[![GitHub stars](https://img.shields.io/github/stars/chirag127/cinesense?style=flat-square)](https://github.com/chirag127/cinesense)
[![License](https://img.shields.io/github/license/chirag127/cinesense?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue?style=flat-square)](https://python.org)
[![GH Pages](https://img.shields.io/badge/site-live-brightgreen?style=flat-square)](https://chirag127.github.io/cinesense/)

AI-powered movie recommendation web app. Content-based filtering + IMDb review sentiment analysis. Built with Flask, scikit-learn, TF-IDF.

## Live Site

**https://chirag127.github.io/cinesense/**

## Features

- Content-based movie recommendations using TF-IDF + cosine similarity
- Sentiment analysis of IMDb user reviews (Good/Bad classification)
- TMDB dataset with poster images and cast details
- Cached ML model loading (loaded once at startup)

## Setup

```bash
pip install -r requirements.txt

# Place model files in project root:
# - nlp_model.pkl (sentiment classifier)
# - tranform.pkl (TF-IDF vectorizer)
# - main_data.csv (movie dataset)

python src/cinesense/web/app.py
```

## Architecture

```
src/cinesense/web/app.py   Flask app + MovieRecommender class
templates/                  Jinja2 HTML templates
static/                     JS, CSS, images
notebooks/                  Jupyter preprocessing notebooks
datasets/                   Raw TMDB data
```

## License

MIT
