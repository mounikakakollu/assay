import re
import math
from random import randint
import numpy as np
import sys
from time import time
import pylab as pl
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.svm import LinearSVC
from sklearn.neighbors import NearestCentroid
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import matplotlib.pyplot as plt
import main
from main import start
from crossCheck import CrossCheck
Evalution={"True_Negative":0,"True_Positive":0,"False_Negative":0,"False_Positive":0}
Domains=['baby','garden','health','music','video']
tweets=[]
stopwords={}
y_train=[]
featurecount={}
validation=[]
id_num=[]
babyc=[0]
gardenc=[0]
healthc=[0]
musicc=[0]
videoc=[0]
class miner():
	def __init__(self):
		self.feature_extraction=self.word_splitter
	def word_splitter(self,sentence):
		splitter=re.compile('\\W*')
		words=[s.lower() for s in splitter.split(sentence) if len(s)>0 and len(s)<20]
		return dict([(w,1) for w in words])

	def addstopwords(self):
		f=open("../data_sets/stopwords.txt","r").read()
		f=f.split(",")
		for i in f:
			stopwords[i]=1

	def train(self,fisher):
		f=open("../data_sets/baby/baby.txt","r").read()
		f=f.split("\n")
		if(len(f)>1000):
			f=f[:1000]
		for i in f:
			fisher.train(i,"baby")
			tweets.append(i)
			y_train.append(0)
		f1=open("../data_sets/garden/garden.txt","r").read()
		f1=f1.split("\n")
		if(len(f1)>1000):
			f1=f1[:1000]
		for i in f1:
			fisher.train(i,"garden")
			tweets.append(i)
			y_train.append(1)
		f3=open("../data_sets/health/health.txt","r").read()
		f3=f3.split("\n")
		if(len(f3)>1000):
			f3=f3[:1000]
		for i in f3:
			fisher.train(i,"baby")
			tweets.append(i)
			y_train.append(2)
		f4=open("../data_sets/music/music.txt","r").read()
		f4=f4.split("\n")
		if(len(f4)>1000):
			f4=f4[:1000]
		for i in f4:
			fisher.train(i,"baby")
			tweets.append(i)
			y_train.append(3)
		f5=open("../data_sets/video/video.txt","r").read()
		f5=f5.split("\n")
		if(len(f5)>1000):
			f5=f5[:1000]
		for i in f5:
			fisher.train(i,"baby")
			tweets.append(i)
			y_train.append(4)
		f=open("../data_sets/baby/baby_validation.txt","r").read()
		f=f.split("\n")
		if(len(f)>1000):
			f=f[:1000]
		for i in f:
			fisher.train(i,"baby")
			tweets.append(i)
			y_train.append(0)
		f2=open("../data_sets/garden/garden_validation.txt","r").read()
		f2=f2.split("\n")
		if(len(f2)>1000):
			f2=f2[:1000]
		for i in f2:
			fisher.train(i,"garden")
			tweets.append(i)
			y_train.append(1)
		f3=open("../data_sets/health/health_validation.txt","r").read()
		f3=f3.split("\n")
		if(len(f3)>1000):
			f3=f3[:1000]
		for i in f3:
			fisher.train(i,"garden")
			tweets.append(i)
			y_train.append(1)
		f4=open("../data_sets/music/music_validation.txt","r").read()
		f4=f4.split("\n")
		if(len(f4)>1000):
			f4=f4[:1000]
		for i in f4:
			fisher.train(i,"garden")
			tweets.append(i)
			y_train.append(1)
		f5=open("../data_sets/video/video_validation.txt","r").read()
		f5=f5.split("\n")
		if(len(f5)>1000):
			f5=f5[:1000]
		for i in f5:
			fisher.train(i,"garden")
			tweets.append(i)
			y_train.append(1)

	def start(self):
		nb=0
		svm=0
		fisher=FisherNB(self.feature_extraction)
		self.addstopwords()
		self.train(fisher)
		self.train(fisher)
		print ("Training is finished")
		nb1=self.findresult(fisher,nb)
		print ("Naive bayes is completed")
		SVM=Svm(svm)
		svm=SVM.classify()
		print ("SUCCESSFULLY COMPLETED")
		print ("Now we calculate polarity for each sentence")
		#start("video");
		for i in Domains:
			start(i)
			print (i+" is completed")
		print ("Result will be stored in Result.txt")
		#print gardenc[0],babyc[0],videoc[0],musicc[0],healthc[0]
		Graph=graph_plot()
		Graph.graph()
		f=open("featurecount.txt","w");
		for i in featurecount:
			f.write(str(i)+"\t"+str(featurecount[i])+'\n')
	def findresult(self,fisher,nb):
		f = open("../data_sets/test.txt","r").read()
		f = f.split("\n")
		f1 = open("../data_sets/baby/baby_result.txt","w")
		f2 = open("../data_sets/garden/garden_result.txt","w")
		f3 = open("../data_sets/health/health_result.txt","w")
		f5 = open("../data_sets/video/video_result.txt","w")
		f6 = open("../data_sets/remaining.txt","w")
		f4 = open("../data_sets/music/music_result.txt","w")
		for i in range(len(f)):
			idno=f[i][:str(f[i]).find(" ")]
			resu = fisher.classify(f[i])
			if(resu!=""):
				if(resu=="baby"):
					f1.write(f[i]+"\n")
					CrossCheck(resu,f[i],Evalution)
					babyc[0]+=1;
				elif(resu=="garden"):
					f2.write(f[i]+"\n")
					CrossCheck(resu,f[i],Evalution)
					gardenc[0]+=1
				elif(resu=="music"):
					f4.write(f[i]+"\n")
					CrossCheck(resu,f[i],Evalution)
					musicc[0]+=1
				elif(resu=="video"):
					f5.write(f[i]+"\n")
					CrossCheck(resu,f[i],Evalution)
					videoc[0]+=1
				elif(resu=="health"):
					f3.write(f[i]+"\n")
					CrossCheck(resu,f[i],Evalution)
					healthc[0]+=1
				else:
					f3.write(f[i]+"\n")
				nb+=1
			else:
				f6.write(f[i]+"\n")
		f3.close()
		f4.close()
		return nb
class graph_plot():
	def __init__(self):
		self.reviews={}
		self.count={}
		self.lables='positive','Negative','Neutral'
		self.all_Negative = 0
		self.all_Neutral = 0
		self.all_Positive = 0
	def GRAPH(self):
		sizes=[self.count['Positive'],self.count['Negative'],self.count['Neutral']]
		colors=['green','red','grey']
		explode=(0.1,0,0)
		plt.pie(sizes,labels=self.lables,colors=colors,autopct='%1.2f%%',shadow=False,startangle=160)
		plt.show()
		self.all_Positive = self.count['Positive']
		self.all_Neutral = self.count['Neutral']
		self.all_Negative = self.count['Negative']
		self.count.clear()
	def graph(self):
		for i in Domains:
			fileName = "../data_sets/"+i+"/"+i+"_polarity.txt"
			f=open(fileName,"r").read()
			f=f.split("\n")
			self.count.setdefault('Negative',0)
			self.count.setdefault('Positive',0)
			self.count.setdefault('Neutral',0)
			for i in f:
				if(i==''):
					continue
				index=str(i).find(" ")
				if(i[index+1:]=='Positive'):
					self.count['Positive']+=1
				elif(i[index+1:]=="Neutral"):
					self.count['Neutral']+=1
				else:
					self.count['Negative']+=1
			self.GRAPH()
		self.count.setdefault('Negative',0)
		self.count.setdefault('Positive',0)
		self.count.setdefault('Neutral',0)
		self.count['Positive'] = self.all_Positive
		self.count['Neutral'] = self.all_Neutral
		self.count['Negative'] = self.all_Negative
		self.GRAPH()

class Svm():
	def __init__(self,svm):
		self.svmcount=0
		self.train()
	def train(self):
		#tweet=tweets[:10000]
		self.x_train=np.array(tweets)
	def classify(self):
		f=open("../data_sets/remaining.txt","r").read()
		f=f.split("\n")
		for i in f:
			idno=i.find(" ")
			idno=i[:idno]
			validation.append(i)
			id_num.append(idno)
		x_test = np.array(validation)
		classifier = Pipeline([
			('vectorizer', TfidfVectorizer(sublinear_tf=True, max_df=0.5,stop_words='english')),
			('tfidf', TfidfTransformer()),
			('clf',  LinearSVC())])
		classifier.fit(self.x_train, y_train)
		predicted = classifier.predict(x_test)
		t2count=0
		f1 = open("../data_sets/baby/baby_result.txt","a")
		f2 = open("../data_sets/garden/garden_result.txt","a")
		f3 = open("../data_sets/health/health_result.txt","a")
		f4 = open("../data_sets/music/music_result.txt","a")
		f5 = open("../data_sets/video/video_result.txt","a")
		for ids,labels,tweet in zip(validation,predicted,validation):
			resu = Domains[labels]
			CrossCheck(resu,ids,Evalution)
			if(Domains[labels]=="baby"):
				f1.write(ids+"\n")
				babyc[0]+=1;
			elif(Domains[labels]=="garden"):
				f2.write(ids+"\n")
				gardenc[0]+=1
			elif(Domains[labels]=="health"):
				f3.write(ids+"\n")
				healthc[0]+=1
			elif(Domains[labels]=="music"):
				f4.write(ids+"\n")
				musicc[0]+=1
			else:
				f5.write(ids+"\n")
				videoc[0]+=1;
			self.svmcount+=1
		f3.close()
		return self.svmcount
class FisherNB():
	def __init__(self,getfeatures,filename=None):
		self.categorycount={}
		self.getfeatures=getfeatures
		self.minimums={}
	def train(self,sentence,category):
		words=self.getfeatures(sentence)
		for i in words:
			if i not in stopwords:
				featurecount.setdefault(i,{})
				featurecount[i].setdefault(category,0 )
				featurecount[i][category]+=1
				self.categorycount.setdefault(category,0)
				self.categorycount[category]+=1
	def feature_count(self,word,category):
		if word in featurecount and category in featurecount[word]:
			return float(featurecount[word][category])
		return 0.0

	def catcount(self,category):
		if category in self.categorycount:
			return float(self.categorycount[category])
		return 0.0

	def fprob(self,word,category):
		if self.catcount(category)==0: return 0
		return self.feature_count(word,category)/self.catcount(category)

	def cprob(self,word,category):
		clf=self.fprob(word,category)
		if clf==0: return 0
		freqsum=sum([self.fprob(word,c) for c in self.categorycount.keys()])	# total frequency of feature
		p=clf/(freqsum)
		return p

	def fisherprob(self,sentence,category):
		p=1.
		words=self.getfeatures(sentence)
		for i in words:
			basicprob=self.cprob(i,category)
			totals=sum([self.feature_count(i,c) for c in self.categorycount.keys()])
			p *= ((1.0*0.5)+(totals*basicprob))/(1.0+totals)
		if(p>0):
			fscore=-2*(math.log(abs(p)))
		else:
			fscore=0
		return self.invchi2(fscore,len(words)*2)

	def invchi2(self,chi,df):
		m = chi / 2.0
		sum = term = math.exp(-m)
		for i in range(1, df//2):
			term *= m / i
			sum += term
		return min(sum, 1.0)

	def classify(self,sentence,default=None):
		best=default
		max=0.0
		for c in self.categorycount.keys():
			p=self.fisherprob(sentence,c)
			if c not in self.minimums:
				minimum = 0
			else:
				minimum = self.minimums[c]
			if (p>minimum and p>max):
				best=c
				max=p
		p1 = self.fisherprob(sentence,"baby")
		p2 = self.fisherprob(sentence,"garden")
		p3 = abs(p1-p2)*10
		p3 = int(p3)
		maxcount=0.0
		if(p3<5.0):
			best=''
		else:
			for za in range(p3/2):
				self.train(sentence,best)	# On-line learning of model
			tweets.append(sentence)
			if(best=="baby"):
				y_train.append(0)
			else:
				y_train.append(1)
		return best

def startclassification():
	for i in Domains:
		f = "../data_sets/"+i+"/"+i+"_polarity.txt"
		f1 = open(f,"w");
		f1.close()
	classification=miner()
	classification.start()
if __name__=='__main__':startclassification()
