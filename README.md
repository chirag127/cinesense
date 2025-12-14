# CineSense-AI-Movie-Recommender-Web-App

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python Version](https://img.shields.io/badge/python-3.9-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-390/)
[![Flask](https://img.shields.io/badge/flask-2.0-blue.svg?style=flat-square)](https://flask.palletsprojects.com/en/2.0.x/)

A Flask-based web app that delivers AI-powered content-based movie recommendations and sentiment analysis of user reviews using TMDB data.

## ✨ Features

-   **AI-Powered Recommendations:** Get personalized movie recommendations based on your favorite movies.
-   **Sentiment Analysis:** Understand the sentiment of user reviews with our NLP model.
-   **TMDB Data:** Utilizes the comprehensive TMDB dataset for accurate and up-to-date movie information.
-   **Interactive UI:** A user-friendly interface for a seamless experience.

## 🚀 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/chirag127/CineSense-AI-Movie-Recommender-Web-App.git
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the application:**
    ```bash
    python src/cinesense/web/app.py
    ```

## 🌳 Architecture

```
.
├── .github
│   ├── ISSUE_TEMPLATE
│   │   └── bug_report.md
│   ├── workflows
│   │   └── ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── AGENTS.md
├── CONTRIBUTING.md
├── LICENSE
├── PROPOSED_README.md
├── README.md
├── SECURITY.md
├── datasets
├── notebooks
├── requirements.txt
├── src
│   ├── cinesense
│   │   ├── __init__.py
│   │   └── web
│   │       ├── __init__.py
│   │       └── app.py
│   └── __init__.py
├── static
│   ├── autocomplete.js
│   └── recommend.js
└── templates
    ├── home.html
    └── recommend.html
```

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📝 License

This project is licensed under the **CC BY-NC 4.0** License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <b>Star ⭐ this repo if you found it helpful!</b>
</p>
