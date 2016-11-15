
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import os

def createFolders(dirs):

    for f in dirs:
        if not os.path.isdir(f): 
            os.mkdir (f) 

def readBVTV(filename):

    res = np.zeros(27)

    i = 0
    with open(filename, "r") as ins:
        for line in ins:
            if(i != 0 and i != 1):
                arr = line.split()
                #print res.shape, len(arr), i
                res[i-2] = arr[4]

            i = i+1
            if(i>=29): break

    print res
    return res


def do_test():

    path = "/home/rodrigo/rodrigo/rodrigo/boneMeasures/SiCopyRodrigo/Win32Release/BVTV/"

    patients = ["5c", "6b", "8b", "8c", "V12"]
    scans = ["01", "02", "03", "M1", "M2", "XCT"]
    # amount of volumes of interest
    vois = 27

    # bone's multifractal spectra database
    bvtvs = np.zeros([len(patients),len(scans),vois])

    ii = 0
    for i in patients:
        jj = 0
        for j in scans:

            filename = path+i+j+".txt"

            print i,j
            print filename

            bvtvs[ii,jj] = readBVTV(filename)

            jj = jj+1

        ii = ii+1


    np.save("bvtvs",bvtvs)

    
