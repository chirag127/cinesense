<centre><h1>MOVIE RECOMMENDATIONS SYSTEM<h1><h2>Chirag Singhal, RKGIT

</h2>
<h2>Ashutosh Maurya, RKGIT
</h2>

</centre>

- [1.1. Abstract](#11-abstract)
- [1.2. Introduction](#12-introduction)
  - [Companies benefit through recommendation system](#companies-benefit-through-recommendation-system)
- [Methods](#methods)
  - [Collaborative](#collaborative)
  - [Content-Based](#content-based)
  - [Hybrid Recommendations](#hybrid-recommendations)
- [1.3. Data Acquisition](#13-data-acquisition)
- [1.4. Data Preprocessing](#14-data-preprocessing)
- [1.5. Modeling](#15-modeling)
- [1.6. Results](#16-results)
- [1.7. Conclusion](#17-conclusion)
  - [All avalible movie recomendation methods and approaches](#all-avalible-movie-recomendation-methods-and-approaches)
- [1.8 References](#18-references)

## 1.1. Abstract

The current generation of recommender systems is mostly classified into three main categories: content-based, collaborative, and hybrid recommendation approaches. This paper presents an overview of the field of recommender systems and describes the current generation of recommender methods, their limitations, and possible extensions.

Content-based recommender systems create recommendations based on the similarity between the content of the items being recommended and the user's preferences. These systems are generally limited to a specific domain and do not work well when the user's preferences are not well-defined.

Collaborative recommender systems, on the other hand, create recommendations based on the similarity between the users' ratings of the items being recommended. These systems are more flexible and can work with less well-defined user preferences. However, they are often subject to the "cold start" problem, wherein the system has difficulty making recommendations for new users or items.

Hybrid recommender systems combine the content-based and collaborative approaches in order to overcome the limitations of each. However, these systems are generally more complex and require more data in order to work effectively.

Current recommender systems have limitations in terms of understanding of users and items, incorporation of contextual information, support for multcriteria ratings, and provision of more flexible and less intrusive recommendations. However, these limitations can be overcome by extensions to current recommender methods, such as incorporation of user feedback, use of content-based methods to supplement collaborative methods, use of hybrid methods that combine content-based and collaborative approaches, and use of context-aware methods that take into account the user's current situation.

## 1.2. Introduction

The main objective of this paper is to recommend movies to the user based on the content of the movie. The content-based filtering system is used to recommend movies. The main parameters that are considered for the recommendations are the genre, director, and top 3 casts. The details of the movies, such as title, genre, runtime, rating, poster, casts, etc., are fetched from TMDB. The reviews of each individual movie given by the users are "web-scraped" from the IMDB website with the help of beautifulsoup4, and the reviews are subjected to sentiment analysis, where the model predicts whether the review is positive or negative.

A recommendation system is a system that is used to predict the rating or preference a user would give to an item.The main objective of a recommendation system is to get to know the user intentions and wants. A recommendation system helps in predicting what a user wants on the basis of the activity of the user and the activity of other users. There are different types of recommendation systems; we will be focusing on content-based filtering.

Netflix 2/3rd of the movies watched are
recommended
Google News recommendations generate 38% more
click-troughs
Amazon 35% sales from recommendations
Choicestream 28% of the people would buy more
music if they found what they liked
Table1. Companies benefit through recommendation
system

### Companies benefit through recommendation system

| Companies    | Benefit                                                              |
| ------------ | -------------------------------------------------------------------- |
| Netflix      | 2/3rd of the movies watched are recommended                          |
| Google News  | recommendations generate 38% more click-troughs                      |
| Amazon       | 35% sales from recommendations                                       |
| Choicestream | 28% of the people would buy more music if they found what they liked |

## Methods

### Collaborative

In collaborative recommendation methods, the system recommends items based on the similarity between the users' ratings of the items being recommended. These systems are more flexible and can work with less well-defined user preferences. However, they are often subject to the "cold start" problem, wherein the system has difficulty making recommendations for new users or items.

Collaborative systems examples are:

- **Nearest Neighbor:** In a nearest neighbor approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

- **Clustering:** In a clustering approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

- **Graph-Theory:** In a graph-theory approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

### Content-Based

In content-based recommendation methods, the system recommends items based on the similarity between the items being recommended and the items the user has already rated. These systems are generally limited to a specific domain and do not work well when the user's preferences are not well-defined.

Content-based systems examples are:

- **Tf-idf:** In a tf-idf approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

- **Bayesian Classifier:** In a Bayesian classifier approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

- **Decision Tree:** In a decision tree approach, the system recommends items that are similar to the items that the user has already rated. The similarity between items is typically measured using the cosine similarity between the item vectors. The item vectors are created by combining the user ratings for each item into a single vector. The system then recommends items that are similar to the items that the user has already rated.

### Hybrid Recommendations

Hybrid systems are effective in overcoming the limitations of both content-based and collaborative systems by using the strengths of each approach. Hybrid systems are typically more complex than content-based or collaborative systems, and require more data in order to work effectively. However, they can provide more accurate and personalized recommendations than either content-based or collaborative systems.

Hybrid systems can be classified into three types:

- **Mixed Approach:** In a mixed approach, the recommender system uses both content-based and collaborative methods, but the methods are used independently. That is, the content-based and collaborative methods are not combined into a single approach.

- **Ensemble Method:** In an ensemble method, the recommender system combines the results of multiple content-based and collaborative methods. Ensemble methods can be used to improve the accuracy of the recommendations by combining the strengths of multiple methods.

- **Hybrid Approach:** In a hybrid approach, the recommender system combines content-based and collaborative methods into a single approach. Hybrid methods typically use content-based methods to provide initial recommendations, which are then refined using collaborative methods.

## 1.3. Data Acquisition

There are 2 datasets that we have used for this analysis:

1. **Movies_metadata.csv**
   Data on 45,000 movies features including budget, revenue, title, cast, director and overview from the 1950's to 2015. Collected from The Movie Database (TMDb).

2. **IMDB 5000 Movie Dataset**

   This data set contains all the metadata for the movies in IMDB past 50 years and put them into a CSV file, sorted according to social popularity.

## 1.4. Data Preprocessing

The first step in the preprocessing of the data is to understand each column of the data and what information it contains. Each column and dataset is reviewed in detail and the required feature engineerig and cleaning is carried out on some of the attributes in the data.

**Irrelevant Attribute:**

There are some columns in the data which don't contribute torecommendation and are discarded.

**Univariate Analysis:**

We carried out some analysis on individual features to see their importance for generating recommendation. Some features were dropped based on the univariate analysis.

**Multivariate Analysis:**

We carried out some analysis of relationship between multiple independent variables and the dependent variable in order to see the utility of the independent variable to generate recommendation. Some features were dropped based on the multivariate analysis.

**Sentiment Analysis:**

During the univariate and multivariate analysis we realized that the reviews given by the users was major data source for us as it would give us greater insights as to how the movie was liked. Due to it's importance , a textanalyzer model was created which can predict how positive, negative or neutral the review is.

**Transformation:**

All the features were transformed such that all features lie in the same scale between 0 and 1. This helps in the performance of the machine learning model.

## 1.5. Modeling

We have built different models with different parameters and dataset sizes to test which one works best.
The information given in the dataset had text and numeric features. Since no recommendation was possible using numerical features alone, we removed them to build the recommendations model.

Some of the text features had "N/A" or blanks. We removed them once the feature selection was complete.

Once we had made the data ready, we pushed it into a `SVM` model and tested it. All the models we used are specified in the repo's readme. The best model was then used to generate the recommendations.

In order to test out which model suits our dataset the best, we have used two models of SKlearn:

- **TextAnalysis('en')**

- **LinearRegression()**

We used linear regression to normalize the predictions given by the text analysis. The text analysis gave random results which were not at all close to the actual sentiments.It's predictions were higher than the actual values by a range of 0.2 to 0.5.
Once, we normalized the predictions, we were able to get a model which had a good prediction score.
This model was then fitted and predictions on other dataset were made.

**Graphical Representation:**

## 1.6. Results

The model gives recommendations based on the genre, director, and top 3 casts of each movie. It is observed that if the genre of the movie and the genre that the user likes match, then the movie is recommended to the user. The model gives better recommendations as compared to other models.

## 1.7. Conclusion

We observed that collaborative and content-basedrecommendation systems are non robust, hard to handle and computationally complex since it studies a large number of user preferences. Combining both content and collaborative recommendation methods improve recommendation quality and provide more customized recommendations. Content-based approach directly correlates with a user preference whereas, items with similar characteristics to the content of the items being recommended are recommended. Collaborativerecommendation systems learn from past user behaviors, on the otherhand.The extension of the current recommendationsystem further takes contextual information into consideration, understands user and item knowledge and at the same time, provides more flexible and less intrusive recommendations. Such a system can provide facility to users for indirect interaction that is not possible for many standard recommender systems and at the same time, promotes online discussion and learning among the users. This further enables individual recommendation providers to build an online community of niche interests.

### All avalible movie recomendation methods and approaches

| Recommendation Approach | heuristics-based                                                                                                                                                | model-based                                                                                                                                                                        |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| content-based           | Commonly used techniques: TF-IDF (information retrieval)                                                                                                        | Commonly used techniques: Bayesian classifiers, clustering, decision trees, artificial neural networks                                                                             |
|                         | Representative research examples: Lang 1995, Balabanovic & Shoham 1997, Pazzani & Billsus 1997                                                                  | Representative research examples: Pazzani & Billsus 1997, Mooney et al. 1998, Mooney & Roy 1999, Billsus & Pazzani 1999, 2000, Zhang et al. 2002                                   |
| collaborative           | Commonly used techniques: Nearest neighbor (cosine, correlation), clustering                                                                                    | Commonly used techniques: Bayesian network, clustering, artificial neural networks, linear regression, probabilistic models                                                        |
|                         | Representative research examples: Resnick et al. 1994, Hill et al. 1995, Shardanand & Maes 1995, Breese et al. 1998                                             | Representative research examples: Nakamura & Abe 1998, Aggarwal et al. 1999, Delgado & Ishii 1999, Pennock & Horwitz 1999, Sarwar et al. 2001                                      |
|                         | Representative research examples: Pavlov & Pennock 2002, Shani et al. 2002, Yu et al. 2002, 2004, Hofmann 2003, 2004, Marlin 2003, Si & Jin 2003                |                                                                                                                                                                                    |
| hybrid                  | Commonly used techniques: Linear combination of predicted ratings, various voting schemes, incorporating one component as a part of the heuristic for the other | Commonly used techniques: Incorporating one component as a part of the model for the other, building one unifying model                                                            |
|                         | Representative research examples: Basu et al. 1998, Condliff et al. 1999, Soboroff & Nicholas 1999, Ansari et al. 2000, Popescul et al. 200, Schein et al. 2002 | Representative research examples: Balabanovic & Shoham 1997, Claypool et al. 1999, Good et al. 1999, Pazzani 1999, Billsus & Pazzani 2000, Tran & Cohen 2000, Melville et al. 2002 |

## 1.8 References

[1] G. Adomavicius, A. Tuzhilin, Toward the next generation of recommender system: a survey of the state-of-the-art and possible extensions, IEEE Trans. Knowl. Data Eng. 17 (6) (2005) 734–749.

[2] G. Linden, B. Smith, J. York, Amazon.com recommendations: item to item collaborative filtering, IEEE Internet Comput. 7 (1) (2003)
76–80.

[3] B.M. Sarwar, G. Karypis, J. Konstan, J. Riedl, Recommender systems
for large-scale e-commerce: scalable neighborhood formation using
clustering, in: Proceedings of International Conference on Computer
and Information Technology, Dhaka, Bangladesh, 2002.

[4] B.M. Sarwar, G. Karypis, J. Konstan, J. Riedl, Item-based collaborative
filtering recommendation algorithm, in: Proceedings of the 10th
International WWW Conference, Hong Kong, 2001, pp. 285–295.

[5] B.M. Sarwar, G. Karypis, J. Konstan, J. Riedl, Application of dimensionality reduction in recommender system—a case study, in:
Proceedings of ACM WebKDD Workshop, Boston, MA, 2000.

[6] J.S. Breese, D. Heckerman, C. Kadie, Empirical analysis of predictive
algorithms for collaborative filtering, in: Proceedings of the 14th
Conference on Uncertainty in Artificial Intelligence, Madison,
Wisconsin, USA, 1998, pp. 43–52.

[7] G. Xue, C. Lin, Q. Yang, et al., Scalable collaborative filtering using
cluster-based smoothing, in: Proceedings of the 28th International
Conference on ACM SIGIR, Brazil: ACM Press, 2005, pp. 114–121.

[8] F. Gao, C. Xing, Y. Zhao, An Effective Algorithm for Dimensional
Reduction in Collaborative Filtering, in LNCS 4822, Springer, Berlin,
2007, 75–84.

[9] Q. Li, B.M. Kim, Clustering approach for hybrid recommendation
system, in: Proceedings of the International Conference on Web
Intelligence, Halifax, Canada, 2003, pp. 33–38.

[10] K. Kim, H. Ahn, A recommender system using GA K-means clustering
in an online shopping market, Expert Syst. Appl. 34 (2) (2008)
1200–1209.

[11] A. Kohrs, B. Merialdo, Clustering for collaborative filtering applications, in: Proceedings of Computational Intelligence for Modeling,
Control and Automation (CIMCA), Vienna: IOS Press, 1999, pp. 199– 204.

[12] D. Goldberg, D. Nichols, B.M. Oki, D. Terry, Using collaborative
filtering to weave an information tapestry, Commun. ACM 35 (12)
(1992) 61–70.

[13] D. Billsus, M.J. Pazzani, Learning collaborative information filters, in:
Proceedings of the 15th International Conference on Machine
Learning, Madison, 1998, pp. 46–53.

[14] K. Goldberg, T. Roeder, D. Gupta, C. Perkins, Eigentaste: a constant
time collaborative filtering algorithm, Inf. Retrieval. 4 (2) (2001)
133–151.

[15] 1. Wikipedia Contributors. Machine learning. Wikipedia. Published November 28, 2022. Accessed November 28, 2022. <https://en.wikipedia.org/wiki/Machine_learning>
‌
