-----------------------------------------------------------------
ASSAY: An Hybrid Approach For Sentiment Analysis
------------------------------------------------------

Goole link: https://drive.google.com/open?id=1kfhz4TqDfpwQIZ9GAPGAQKc3cbgnmoRM


This is the working code for hierarchical review classifier and polarity extraction by combining Machine learning approach and Lexicon-based apporach to develop a hybrid approach known as ASSAY.
To run this code after installing sklearn,matplotlib,numpy please type this command in your terminal
>	python domain.py

Requirements:
-------------
* Python sklearn package version 0.13.1
* You can install scikit-learn-0.13.1 scikit-learn.org
* sudo apt-get install build-essential python-dev python-numpy python-setuptools python-scipy libatlas-dev

GETTING STARTED
----------------------------------------
* domain.py

	This file containing the code which is used to classify the reviews. 
	It uses two classification algorithms 
	* Fisher score based Naive bayesian Classification
	* Linear SVM text classifier
	* Plot graph of every domain after calculate polarity
	Initially, Bayesian probability is calculated, if this probability is >0.5 then classify that review otherwise that review will send to SVM.
*  main.py

	  This file is used to preprocess the data.
	  Removal of stopwords are done in this file.
* Polarity.py

	  The code in this file is used to calculate the polarity of each review at sentence level.
	  Here we use two types of dictionarys called Noun-Verb dictionary and Ordinary dictionary.
	*  reviews.py
  
		This ia python file which is used to store dictionary.<br />
		This dictionary is known as Noun-Verb Dictionary.<br />
		Here Noun will be the name of the dictionary. verb,adverb,adjectives are the keys in this dictionary and polaritys of corresponding aspect is the value in the Noun-Verb Dictionary.
    
	* Dictionary.py
  
		this file contains three arrays.
		*  Positive array:- contains all positive aspects.
		* Negative array:- contains all negative aspects.
		* Neutral array:- contains all neutral aspects.
    
	While calculating the polarity at sentence level, inintially by using these two dictionaries extract the polarity of every aspects in the review.
	The Noun-Verb dictionary is helpful to avoid domain-specific adoptation.
  
	 ex: Training is moving fast. --> Positivie
	 	 Battery is draining fast. --> Negative
* result.py

	This file is used to make a decision whether the review is positive or negative or neutral.
* crosscheck.py

	this is used to calculate the TruePositive,TrueNegative,FalsePositive,FalseNegative.

data_sets directory
-------------------
 In this directory, training and testing data_sets of every domains are grouped.
  * "result.txt"
		Output predictions of my model will be stored in this file.
  * "stopwords.txt"
		This is collection of some stop words which were gathered from external sources. 
Note: I have not used any other garden or baby or video or music or health external keywords.
  * "validation.txt" and "test.txt"

Note: This code does not contain any other external datasets or keywords except some few stopwords. 

	All above reviews used as training set are extracted only from Amazon dataset

Explanation
----------
Only Naive Bayes can give accurracy of 85%. To improve the performance of our model we combine SVM with Naive Bayes.By combining Naive Bayes and SVM we achieve to get accuracy for classification of individual domain is increated by 12%.
After classify the reviews into individual domains, we calculate the polarity of each domain at document level. For this we propose a new method called Harn's Algorithm. The heart of this algorithm is Noun-Verb Dictionary which is used to solve domain-specific adoptation. 
Overall accurracy of our work achieves about 90%. This word is also publishing in Springer. Conference of Springer is held at Ahmedabad, April 5,6 2018.
