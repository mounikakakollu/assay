-----------------------------------------------------------------
ASSAY: An Hybrid Approach For Sentiment Analysis
             -- K. Mounika, kmc.iiitn@gmail.com
Goole link for this project:
	https://drive.google.com/open?id=1kfhz4TqDfpwQIZ9GAPGAQKc3cbgnmoRM
-----------------------------------------------------------------

This is the working code for hierarchical review classifier and polarity extraction by combining Machine learning approach and Lexicon-based apporach to develop a hybrid approach known as ASSAY.
To run this code after installing sklearn,matplotlib,numpy please type this command in your terminal
>	python domain.py

------Requirements:----------------------

1. Python sklearn package version 0.13.1

You can install scikit-learn-0.13.1 scikit-learn.org

sudo apt-get install build-essential python-dev python-numpy python-setuptools python-scipy libatlas-dev


-----Files contained in this code:--------

This code contains following files

1."domain.py" 
	This file containing the code which is used to classify the reviews. 
	It uses two classification algorithms 
	i) Fisher score based Naive bayesian Classification
	ii) Linear SVM text classifier
	iii) Plot graph of every domain after calculate polarity
	Initially, Bayesian probability is calculated, if this probability is >0.5 then classify that review otherwise that review will send to SVM.
2. "main.py"
	This file is used to preprocess the data.
	Removal of stopwords are done in this file.
3. "Polarity.py"
	The code in this file is used to calculate the polarity of each review at sentence level.
	Here we use two types of dictionarys called Noun-Verb dictionary and Ordinary dictionary.
	a) "reviews.py"
		This ia python file which is used to store dictionary.
		This dictionary is known as Noun-Verb Dictionary.
		Here Noun will be the name of the dictionary. verb,adverb,adjectives are the keys in this dictionary and polaritys of corresponding aspect is the value in the Noun-Verb Dictionary.
	b) "Dictionary.py"
		this file contains three arrays.
		i. Positive array:- contains all positive aspects.
		ii. Negative array:- contains all negative aspects.
		iii. Neutral array:- contains all neutral aspects.
	While calculating the polarity at sentence level, inintially by using these two dictionaries extract the polarity of every aspects in the review.
	The Noun-Verb dictionary is helpful to avoid domain-specific adoptation.
	 ex: Training is moving fast. --> Positivie
	 	 Battery is draining fast. --> Negative
4. "result.py"
	This file is used to make a decision whether the review is positive or negative or neutral.
5. "crosscheck.py"
	this is used to calculate the TruePositive,TrueNegative,FalsePositive,FalseNegative.

 ----------------data_sets directory-----------------
 In this directory, training and testing data_sets of every domains are grouped.
  1. "result.txt"
	Output predictions of my model will be stored in this file.
 2. "stopwords.txt"
	This is collection of some stop words which were gathered from external sources. 
Note: I have not used any other garden or baby or video or music or health external keywords.
  3. "validation.txt" and "test.txt"

Note: This code does not contain any other external datasets or keywords except some few stopwords. 
	All above reviews used as training set are extracted only from Amazon dataset
-------------Explanation------------------------

Only Naive Bayes can give accurracy of 85%. To improve the performance of our model we combine SVM with Naive Bayes.By combining Naive Bayes and SVM we achieve to get accuracy for classification of individual domain is increated by 12%.
 After classify the reviews into individual domains, we calculate the polarity of each domain at document level. For this we propose a new method called Harn's Algorithm. The heart of this algorithm is Noun-Verb Dictionary which is used to solve domain-specific adoptation. 
  Overall accurracy of our work achieves about 90%. This word is also publishing in Springer. Conference of Springer is held at Ahmedabad, April 5,6 2018.