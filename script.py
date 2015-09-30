# Sample exercise for text Claissifcation
import os
import sys
import glob
import random
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


Propath = '/mnt/hgfs/WORK/Reza/PythonTask/testData/Pro/*.txt'
NonPropath = '/mnt/hgfs/WORK/Reza/PythonTask/testData/NonPro/*.txt'
i =0
data = []
files = glob.glob(Propath)
for name in files:
	with open(name) as f:
		text = f.read()
		text = text.replace('\n' ,' ')
		text = unicode(text, "utf-8", errors="ignore")
		data.append((text , 'pro')) 
		i+=1
	
	
	
	
	
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
	
#print 'content of line 5 ' , train[4]

cl = NaiveBayesClassifier(train)
cl.accuracy(test)
cl.classify("Your symptoms may be caused due to a musculo-skeletal strain. I would advise you to take OTC pain-killers/NSAIDS and see if it helps. Rest and ice will also help to relieve the symptoms. If the pain does not get better, you may need to visit your doctor for a physical examination. X-rays will usually be normal in most cases.")
