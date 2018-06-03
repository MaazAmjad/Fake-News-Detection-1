#!/usr/bin/python
# -*- coding:utf8 -*-
import pandas as pd
import gensim
import nltk
from nltk.tokenize import word_tokenize
import numpy as np


trainBody = pd.read_csv('train_bodies.csv') #length is 1683

print type(trainBody['articleBody'])
print trainBody['articleBody'].shape
#if using pre-trained word vectors, no need to join two excels
#print trainBody['articleBody'][3]
#tokenize the sentences into a list
#  of word, but not a set of words
lengthList = np.array([])
for index in range(trainBody['articleBody'].shape[0]):
    line = trainBody['articleBody'][index]
    line = line.decode('utf-8')
    #trainBody['After Splitting'][index] = str(word_tokenize(line))
    lengthList = np.append(lengthList,len(word_tokenize(line)))

print "the average length of text body is: "
print int(np.mean(lengthList)) #424 

averageLength = np.mean(lengthList)
#trainBody.to_csv('train_bodies.csv')


trainStances = pd.read_csv('train_stances.csv')
lengthList1 = np.array([])
for index in range(trainStances['Headline'].shape[0]):
    line = trainStances['Headline'][index]
    line = line.decode('utf-8')
    #trainBody['After Splitting'][index] = str(word_tokenize(line))
    lengthList1 = np.append(lengthList1,len(word_tokenize(line)))

print "the average length of headline is: "
print int(np.max(lengthList1))

averageLength1 = np.max(lengthList) #45
