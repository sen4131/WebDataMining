# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 09:20:06 2018

@author: Sen
"""
import nltk
import re, string
from nltk import FreqDist
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import os
from matplotlib import pyplot as plt

path1 = "C:/Users/Sen/Downloads/CUS 635 (Web data mining)/Project/Data/Week1/"
path2 = "C:/Users/Sen/Downloads/CUS 635 (Web data mining)/Project/Data/Week2/"

def test(path):
    prefix = os.listdir(path)
    print(prefix)
    
    dataset={}
    dataset_raw = {}
    allFeatures=set()
    tot_articles = 0
    articles_count={}
    globaltoken=[]
    
    N={} # Number of articles in each corpus
    
    for question in prefix:
        fileName=path+question
        #print(fileName)
        f=open(fileName,'r',encoding="utf8")
        text = ''
        text_raw = ''    
        lines=f.readlines()
        tot_articles+=len(lines)
        articles_count[str(question)] = len(lines)
        dataset_raw[str(question)] = list(map(lambda line: line.lower(), lines))
        
        for line in lines:
            text+=line.replace('\n',' ').lower()
            text_raw = line.lower()
        f.close
        N[str(question)]=len(lines)
        
        
        tokens = nltk.word_tokenize(text)
        globaltoken+=tokens
        dataset[str(question)] = nltk.Text(tokens)
        
    return globaltoken

def remove_punctuation(corpus):
    punctuations = ".,\"-\\/#!?$%\^&\*;:{}=\-_'~()"    
    filtered_corpus = [token for token in corpus if (not token in punctuations)]
    return filtered_corpus

def apply_stopwording(corpus, min_len):
    filtered_corpus = [token for token in corpus if (not token in stopwords.words('english') and len(token)>min_len)]
    return filtered_corpus

def removeAbb(x):
    lst = {'Dx':'diagnosed' ,
           'Rx':'prescription',
           'OTC':'Over The Counter',
           'DFL':'Drug Fact Label',
           'AUT':'Application Under Test'}
    for i in x:
        if i in lst:
            i = lst[i]
    return x

def apply_lemmatization(corpus):
    lemmatizer = nltk.WordNetLemmatizer()
    normalized_corpus = [lemmatizer.lemmatize(token) for token in corpus]
    return normalized_corpus
    
def main(path):
    x = []
    
    result=test(path)
    x.append(len(set(result)))
    
    result=remove_punctuation(result)
    x.append(len(set(result))) 
    
    result=apply_stopwording(result, 3)
    x.append(len(set(result)))
    
    result = removeAbb(result)
    x.append(len(set(result)))
    
    result = apply_lemmatization(result)
    x.append(len(set(result)))
    
    result = nltk.Text(result)
    
    
    plt.plot(x)
    plt.xlabel('steps in normalization')
    plt.ylabel('tokens')
    plt.show()
    
    return result

w1token=main(path1)
#w2token=main(path2)
