# Project Outline Keypoints

## Problem solving
The Production of a movie is very expensive and the success of a movie is not guaranteed. Thatswhy producing a movie is a big risk for all the investors. 
A lot of factors influence if a movie is going to be a success (e.g. main actors, storyline, setting of the movie...). These are too many factors, to easily tell success of a movie. To solve this problem Data Mining is neccessary. 
We want to build a solution, which will help steakholders to predict the success of a movie:
* Will be a movie good or will it be a flop?
* Predict revenue of a movie
* What influences a good movie?

## What Data we are using
To predict the revenue of a movie, a classifier has to be built on a big set of movies. Thatfor we will use the Movie Data set from Kaggle. This dataset contains the metadata with 24 different features (e.g. budget, release-date, genre and the classifier revenue) for 45.000 movies. Additional to the movie metadata, we will have a look at the cast and the crew of all the movies. 
* Movie Data from Kaggle
* https://www.kaggle.com/rounakbanik/the-movies-dataset
* IMDB movie data
* Box office data if neccessary

## How we will solve the problem
We will measure the success of a movie with the created revenue of the movie. Since the revenue is a continious attribute we will bin the revenue into 10 bins/classes. With that binning we can later on predict in which range the revenue of the new movie will be.
Since the metadata of the movies already contains 24 features and not all of them are relevant, we will discard some of the features. To find out the most important features, we will run different classifier on different sets of features. Movies with missing features will be filtered out beforehand. 
For the best prediction, we will test different classifier on the data set. Since Naive Bayes gives good results, despite the assumption of independence of the features, we will take Naive Bayes as Baseline to compare the different classifier. We will work with classifier like KNN, Naive Bayes, Decision Trees and Random forest. On all the classifier we will do some hyperparameter tuning, to get the best results. We will run the KNN with k from 1 to 10, the decision trees with with different depths and split techniques (Entropy, Gini).
To compare the results of the different classifier, we will run a 10 times cross validiation on the dataset and draw a Roc-curve.
* Predict revenue / visitors for new movies in the cinema. 
* Preprocessing and encoding
* Feature selections
* Binning revenue in different "classes"
* Train test split and cross validation
* Different classifiers
	* Knn
	* Naive Bayes (as baseline)
	* Decisions tree if possible
	* Random forest
* Support vector machines
* Parameter optimization

## How we will measure success
After we found the best classifier on the dataset with all the parameters set we will run a train and test split on the data. The train data won't contain any test data. We will compute the accuracy, recall, precision and the f1 score of the prediction of the test data and the prediction of the test data. A high F1-score will show a high success.
* Different metrics

## What do we expect our results will look like
We will create an application, which gives you the option to enter all known metadata of a new movie, to predict the range of revenue this movie will create.
* Put in a new movie with some data you have about it
* Get a prediction of the movie success
* Multilabel classifier
