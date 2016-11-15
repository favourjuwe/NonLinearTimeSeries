


from imfractal import *
import Image
import time
import csv
import sys
import os
from subprocess import *
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

def do_test():
    cant = 10
    dDFs  = 20
    cantClasses = 2
    breadtrain = np.zeros((cant, dDFs)).astype(np.float32)
    breadtest = np.zeros((cant, dDFs)).astype(np.float32)

    nonbreadtrain = np.zeros((cant, dDFs)).astype(np.float32)
    nonbreadtest = np.zeros((cant, dDFs)).astype(np.float32)

    pathbtr = 'images/train/bread/'
    dirListbtr=os.listdir(pathbtr)
    pathnbtr = 'images/train/nonbread/'
    dirListnbtr=os.listdir(pathnbtr)
    pathbte = 'images/test/bread/'
    dirListbte=os.listdir(pathbte)
    pathnbte = 'images/test/nonbread/'
    dirListnbte=os.listdir(pathnbte)
    #print len(dirListbtr), dirListbtr
    
    ins = MFS()

    print 'Training: calculating MFS for the bread database...'
    for i in range(cant):
        ins.setDef(1,20,3,True)
        filename = pathbtr+dirListbtr[i]
        breadtrain[i] = ins.getFDs(filename)
        filename = pathbte+dirListbte[i]
        breadtest[i] = ins.getFDs(filename)

        filename = pathnbtr+dirListnbtr[i]
        nonbreadtrain[i] = ins.getFDs(filename)
        filename = pathnbte+dirListnbte[i]
        nonbreadtest[i] = ins.getFDs(filename)

    cfr = RandomForestClassifier(n_estimators=100)
    data = np.vstack((breadtrain,breadtest,nonbreadtrain,nonbreadtest))
    labels = np.zeros((len(data),1)) # FIX ME
    for i in range(len(data)):
        labels[i] = i
    labels = map(lambda i: np.floor(i/(2*(cant)))+1, labels)
    labels = np.array(labels)
    labels = np.transpose(labels)[0]   # FIX ME
    print "Testing..."
    scores = cross_validation.cross_val_score(cfr, data, labels, cv=4)
    print "Classification performance (Random Forest classifier): " + str( np.array(scores).mean() )



