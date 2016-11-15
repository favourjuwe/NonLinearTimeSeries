
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import os
import sys
sys.path.append('/home/rodrigo/imfractal/imfractal/Algorithm/')

import qs3D

def createFolders(dirs):

    for f in dirs:
        if not os.path.isdir(f): 
            os.mkdir (f) 


def do_test():

    # load array object file
    #res = np.load("mfss.npy")
    res = np.load("mfss.npy")


    patients = ["5c", "6b", "8b", "8c", "V12"]

    # scans except xct
    #scans = ["01", "02", "03","M1", "M2"]
    # all scans
    scans = ["01", "02", "03","M1", "M2", "xct"]


    dims = 10
    vois = 27


    print "test"
    with open("results.txt", "w") as text_file:
        for p in range(len(patients)):
            for k in range(len(scans)):
                for j in range(vois):      
                    s = str(p+1)+ " " + str(k+1)+ " " + str(j+1) + " "+  ' '.join(map(str, res[p][k][j])) + "\n"
                    text_file.write(s)
