# Fake News Challenge - 2

Greetings from Team "Brogrammers". This is the repository developed as a solution to Fake News Challenge (http://www.fakenewschallenge.org) by the team comprising of John Fantell, Yibo Chai, and Rishap Sharma. 

# Summary

While this project was not submitted as part of the competition, all of the results are evaluated using the same scoring methodology used in the competition. 
Ten different features were used in total: TF-IDF, Cosine Similarity, Word2Vec, Doc2Vec, Word Overlap, Word Polarity, Refuting Words, Binary Cooccurrences, Binary Cooccurrence Stops, and Count grams (Figure 1). The latter five features were baseline features provided by the competition website. For predicting class labels various classifiers were used namely random forest, multinomial naive bayes, gradient boosting, k nearest neighbours, linear svm, decision tree, logistic regression, and LSTM.


# Result

Using feature engineering, various ML classifier and also ensemble learning models, applying multi-stage classification strategy, and finally with a deep LSTM model, we got a optimal solution of score of 81.999% for this stance detection competition.


# Requirements
python>=3.4.0


# Installation
python3.4 -m pip install -r requirements.txt --upgrade


# Dependencies/Libraries

In order to run this project, please download the dataset (features and model) from this GitHub repositoryand place in the root folder.
