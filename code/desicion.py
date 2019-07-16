import numpy as np 
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
domain=["baby","garden"]
x_train=[]
y_train=[]
validation=[]
id_num=[]
f=open("../data_sets/baby/baby.txt","r").read()
f=f.split("\n")
for i in f:
	x_train.append(i)
	y_train.append(0)
f1=open("../data_sets/garden/garden.txt","r").read()
f1=f1.split("\n")
for i in f1:
	x_train.append(i)
	y_train.append(1)
f=open("../data_sets/baby/baby_test.txt","r").read()
f=f.split("\n")
for i in f:
	idno=i.find(" ")
	idno=i[:idno]
	validation.append(i)
	id_num.append(idno)
x_test = np.array(validation) 
#x=balance_data.values[:,1:5]
#y=balance_data.values[:,0]
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=100)
clf_gini=DecisionTreeClassifier(criterion="gini",random_state=100,max_depth=3.0,min_samples_leaf=5.0)
clf_gini.fit(y_train,x_train)
clf_gini.predict([[4,4,3,3]])
y_pred=clf_gini.predict(x_test)
print y_pred
y_pred_en=clf.entropy.predict(x_test)
#accuracy score gini index
print accuracy_score(y_test,y_pred)*100
#accuracy score information gain
print accuracy_score(y_test,y_pred_en)*100