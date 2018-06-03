import pandas as pd
import nltk
import re
_wnl = nltk.WordNetLemmatizer()

inputfile1 = 'test_bodies.csv'
outputfile1 = 'test_bodies.txt'
data1 = pd.read_csv(inputfile1)
data1 = data1[[u'articleBody']]

for i in range(len(data1['articleBody'])):
	data1['articleBody'][i]=_wnl.lemmatize(data1['articleBody'][i]).lower()
	data1['articleBody'][i]=" ".join(re.findall(r'\w+', data1['articleBody'][i], flags=re.UNICODE)).lower()
	data1['articleBody'][i]=data1['articleBody'][i].strip('\n')

data1['articleBody'].to_csv(outputfile1, index = False, header = False)
