#!/usr/bin/python
# -*- coding:utf8 -*-
import pandas as pd
import gensim
import nltk
from nltk.tokenize import word_tokenize
import numpy as np

#1.word vector 一个一个的feed into LSTM，使用padding固定序列数据长度
#2.LDA 为每一个文章 生成固定长度的描述topic的关键词 每个关键词当然对应着一个word vector
#3.为每个document生成一个固定长度doc vector Doc2vec是不是和Word2Vec一样语料库越多越精确？

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
print int(np.mean(lengthList)) #424 without 标点符号

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