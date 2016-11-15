
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import os

cantMeasures = 15 # different ways for obtaining identical measures

def createFolders(dirs):

    for f in dirs:
        if not os.path.isdir(f): 
            os.mkdir (f) 

def readMeasures(filename):

    res = np.zeros((27,cantMeasures))

    i = 0
    with open(filename, "r") as ins:
        for line in ins:
            if(i != 0 and i != 1):
                arr = line.split()
                #print arr
                #print len(arr)
                #exit()
                #print res.shape, len(arr), i
                res[i-2,0] = arr[5]
                res[i-2,1] = arr[6]
                res[i-2,2] = arr[28]
                res[i-2,3] = arr[29]
                res[i-2,4] = arr[30]
                res[i-2,5] = arr[31]
                res[i-2,6] = arr[32]
                res[i-2,7] = arr[33]
                res[i-2,8] = arr[34]
                res[i-2,9] = arr[35]
                res[i-2,10] = arr[36]
                res[i-2,11] = arr[37]
                res[i-2,12] = arr[38]
                res[i-2,13] = arr[39]
                res[i-2,14] = arr[40]


            i = i+1
            if(i>=29): break

    print res
    return res


def do_test():

    path = "/home/rodrigo/rodrigo/rodrigo/boneMeasures/SiCopyRodrigo/Win32Release/DSM-RLM/"

    patients = ["5c", "6b", "8b", "8c", "V12"]
    scans = ["01", "02", "03", "M1", "M2", "XCT"]
    # amount of volumes of interest
    vois = 27


    # bone's multifractal spectra database
    measures = np.zeros([len(patients),len(scans),vois,cantMeasures])

    ii = 0
    for i in patients:
        jj = 0
        for j in scans:

            filename = path+i+j+".txt"

            print i,j
            print filename

            measures[ii,jj] = readMeasures(filename)

            jj = jj+1

        ii = ii+1


    np.save("measures",measures)

    
