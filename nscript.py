# Sample exercise for text Classifcation
import os
import sys
import glob
import random
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
from collections import Counter


Propath = '/mnt/hgfs/WORK/Reza/PythonTask/testData/Pro/*.txt'
NonPropath = '/mnt/hgfs/WORK/Reza/PythonTask/testData/NonPro/*.txt'
data = []
files = glob.glob(Propath)
for name in files:
	with open(name) as f:
		text = f.read()
		text = text.replace('\n' ,' ')
		text = unicode(text, "utf-8", errors="ignore")
		data.append((text , 'pro')) 
	
	
	
	
	
files = glob.glob(NonPropath)
for name in files:
	with open(name) as f:
		text = f.read()
		text = text.replace('\n' , ' ')
		text = unicode(text, "utf-8", errors = "ignore")
		data.append((text , 'non-pro'))
	
	
	
	
	
random.shuffle(data)
number_of_elements = len(data)
split = ( number_of_elements / 3 ) * 2
train = data[:split]
test = data[split:]


cl = NaiveBayesClassifier(train)
print "Accuracy on Test data:"
print cl.accuracy(test)

#Create confusion matrix:
#[org label, pred label]
conf = []
for row in test:
	conf.append((row[1], cl.classify(row[0])))
	

Counter(conf)
print "********The Confusion matrix*********"
print "Total size of test data :	%d" %len(test)
print "Original(>) Predicted (V)" 
print "	pro			non-pro"
print "pro	 %d				%d"  %(Counter(conf)['pro' , 'pro'] , Counter(conf)['pro' , 'non-pro'])
print "non-pro	 %d				%d"  %(Counter(conf)['non-pro' , 'pro'] , Counter(conf)['non-pro' , 'non-pro'])


#print cl.classify("Your symptoms may be caused due to a musculo-skeletal strain. I would advise you to take OTC pain-killers/NSAIDS and see if it helps. Rest and ice will also help to relieve the symptoms. If the pain does not get better, you may need to visit your doctor for a physical examination. X-rays will usually be normal in most cases.")