import gensim, logging#载入gensim包#
import os
import csv
#read csv file
csvFile=open(r"test_bodies_vectors.csv","w+",newline="",encoding='utf-8')

writer=csv.writer(csvFile)
sentences = gensim.models.doc2vec.TaggedLineDocument('test_bodies.txt')
#print(type(sentences))
#print(sentences)
#for each in sentences:
    #print(each)
#input in the format ofTaggedLineDocument
model = gensim.models.Doc2Vec(sentences, size = 50, window = 5)
#Note: size is the length of the doc vector generated


model.save('review_pure_text_model.txt')
print(len(model.docvecs))
out = open('review_pure_text_vector.txt', 'w')
for idx, docvec in enumerate(model.docvecs):
    for value in docvec:
      out.write(str(value) + ' ')
    out.write('\n')
    writer.writerow(docvec.tolist())
out.close
csvFile.close()
