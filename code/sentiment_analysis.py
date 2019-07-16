__author__ = 'SushmaRadhikaSaisri'

import csv

import enchant
import pytypo
import jellyfish
import math
import dictionary
#from dictionary import stop_words
from dictionary import dic
import textblob
from textblob import TextBlob
d=enchant.Dict("en_US")
import re
import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize


from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import BernoulliNB
#from sklearn import cross_validation
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import numpy as np
from sklearn.metrics import accuracy_score
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
d = enchant.Dict("en_US")
c=0
cnt=0

# review.csv contains two columns
# first column is the review content (quoted)
# second column is the assigned sentiment (positive or negative)
def shortword(sen):

        if "'re" in sen:
              sen=sen.replace("'re"," are")
        #sent=pytypo.correct_sentence(sen)
        spl=sen.split()
        s=''

        number=['0','1','2','3','4','5','6','7','8','9']
        for string in spl:
              count=0
              nd=0
              z=0
              h=0
              val=0
              al=len(string)
          #    if not d.check(string) and string[-1]!='z':
           #        string=pytypo.correct_sentence(string)
            #  if al>1:
             #   if string[-1]==string[-2] and not d.check(string):
              #       string=pytypo.cut_repeat(string,1)
              for name,v in dictionary.dic.iteritems():
                     for a in v:
                            if string==a:
                                   count+=1
                                   s+=name+' '
                                   z=1
                                   break
              if z:
                     continue
 
              for num in number:
                     if num in string:
                            s+=string+' '
                            val+=1
                            break
              if val==1:
                     continue
              if d.check(string):
                  s+=string+' '
                  continue
              else:
                 try:
                   a=jellyfish.soundex(unicode(string))
                   x=int(a[1:])
                   z=d.suggest(string)
                   for line in z:
                       if d.check(line):
                                  b=jellyfish.soundex(unicode(line))
                                  y=int(b[1:])
                                  if (a[0]==b[0])and(abs(x-y))<=5 and len(line)>len(string):
                                      s+=line+' '
                                      count+=1
                                      break
                 except UnicodeDecodeError:
                     ex=0   
        f = open("../data_sets/shortword.txt",'a')
        f.write(str(s)+"\n");  
        return s    