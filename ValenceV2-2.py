#-------------------------------------------------------------------------------
# Name:        Valence 2.2
# Purpose:
#
# Author:      Mohammad Darwich - modarwish@hotmail.com
#
# Created:     06/01/2015
# Copyright:   (c) datasentimentanalysis.com
#-------------------------------------------------------------------------------

from pos_lexicon import *
from neg_lexicon import *
import re

posSentCounter = 0
negSentCounter = 0
neutSentCounter = 0

pos_lex = pos_lexicon_string.split() #get pos lexicon
#print(pos_lex)

neg_lex = neg_lexicon_string.split() #get neg lexicon
#print(neg_lex)

#get input doc (located in same directory as ValenceV2-2.py)
f = open("input_doc.txt", "r")
if (f.mode == "r"):
    input_doc = f.read()

#split input_doc into sentences, each by a separator "[S]"
input_doc = re.sub(r"([!?.])(?=\s*[A-Z])", r"\1 [S] ", input_doc)
print (input_doc)

sents = re.split(" \[S\] ", input_doc)
#print(sents)

sentsList = []

#separate punctuation from words
for sent in sents:
    sent = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", sent)
    sentsList.append(sent)
#print (sentsList)

sentCounter = 0

print ("---------------------------------------------\n")
print ("Analyzing document's sentiment..\n")
print ("---------------------------------------------\n")

for sent in sentsList:
    matchedPosWords = []
    matchedNegWords = []
    posMatchCount = 0
    negMatchCount = 0
    sentCounter += 1

    words = sent.split()

    for word in words:
        if word in pos_lex:
            matchedPosWords.append(word)
            posMatchCount += 1
        if word in neg_lex:
            matchedNegWords.append(word)
            negMatchCount -= 1

    polarityValue = ""
    weight = posMatchCount + negMatchCount

    if weight > 0:
        polarityValue = "POS"
        posSentCounter += 1
    elif weight < 0:
        polarityValue = "NEG"
        negSentCounter += 1
    else:
        polarityValue = "NEUT"
        neutSentCounter += 1


    print ("_____________________________________________\n")
    print ("[SENT %d] %s [SENT %d]" % (sentCounter, sent, sentCounter))
    print ("Matched POS words: %s" % (matchedPosWords))
    print ("Matched NEG words: %s" % (matchedNegWords))
    print ("POS weight is: %d" % (posMatchCount))
    print ("NEG weight is: %d" % (negMatchCount))
    print ("Polarity of sentence is: %s" % (polarityValue))


print ("\n---------------------------------------------\n")
print ("Total sentences in doc: %d" % sentCounter)
print ("Total POS sentences: %d" % posSentCounter)
print ("Total NEG sentences: %d" % negSentCounter)
print ("Total NEUT sentences: %d" % (neutSentCounter))

if posSentCounter > negSentCounter:
    print ("Final polarity of doc is POSITIVE")
elif posSentCounter < negSentCounter:
    print ("Final polarity of doc is NEGATIVE")
else:
    print ("Final polarity of doc is NEUTRAL")

print ("\n---------------------------------------------\n")
