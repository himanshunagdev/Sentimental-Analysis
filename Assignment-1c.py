# -*- coding: utf-8 -*-
"""
Created on Tue Jun 09 06:22:12 2015

@author: NAGDEV
"""
REV_FILE = 'review.txt'

LOAD_Words=loadWords(REV_FILE)
def scan_lines:
    if sc in score:
        z=y[2].split(' ')
        for t in z:
            if t not in a:
                a[t]=1
            else:
                a[t] += 1
def get_scores(scores):
    Counter([y[2].split(' ')
             for x in REV_FILE
             if int(y[3]) in get_sentences
             ])

def get_sentences(REV_FILE, scores):
    for line in REV_FILE:
        y= line.split(' | ')
        if int(y[3]) in scores:
            yield y[2]
def get_words(REV_FILE, scores):
    import re
    from collections import Counter
    return Counter(word for sentence in get_sentences(REV_FILE, scores)
                    for word in sentence.split(' '))
           Counter(word for line in REV_FILE
                   for word in line.split(' | ')[2].split(' ')
                    if int(x.split(' | ')[3]) in scores)
def main(review_file='review.txt', outfile='output.txt'):
    process_reviews(review_file, outfile)

def print_Nwords():
    N= get_words
    print("top n(N=%s), score=[%s]  ",N, scores))
  
    
    