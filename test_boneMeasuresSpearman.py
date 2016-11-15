
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import os
import scipy

def createFolders(dirs):

    for f in dirs:
        if not os.path.isdir(f): 
            os.mkdir (f) 

def do_test():

    #path = "/home/rodrigo/rodrigo/rodrigo/boneMeasures/SiCopyRodrigo/Win32Release/BVTV/"

    measures = np.load('measures.npy')
    mfss = np.load('mfss.npy')

    dims = 10  

    patients = ["5c", "6b", "8b", "8c", "V12"]
    scans = ["01", "02", "03", "M1", "M2", "XCT"]
    
    # amount of volumes of interest (voi)
    vois = 27
    fsize = 18
    e = 0.1
    s = 10.0
    x1 = 1
    x2 = 20
    x = np.arange(2*dims+1)+1



    for m in range(measures.shape[3]):


        correls = np.zeros((len(patients),vois,2*dims+1))
        correlsAll = np.zeros((len(patients),2*dims+1))
        for p in range(len(patients)):
            for j in range(vois):      
               for i in range(2*dims+1):
                   correls[p,j,i] = scipy.stats.stats.spearmanr(mfss[p,:,j,i],measures[p,:,j,m])[0]

        # for all vois
        for p in range(len(patients)):
            for i in range(2*dims+1):
                allmeasures = measures[p,:,0,m]
                allvois = mfss[p,:,0,i]
                for j in range(1,vois):
                   allvois = np.hstack((allvois,mfss[p,:,j,i]))
                   allmeasures = np.hstack((allmeasures,measures[p,:,j,m]))

                print allvois.shape, allmeasures.shape
                correlsAll[p,i] = scipy.stats.stats.spearmanr(allvois,allmeasures)[0]

        print correlsAll

        plt.ylim((-1, 1))
        plt.xlim(x1,x2)
        plt.title('ALL - Measure ' + str(m))
        plt.ylabel(r'$\rho$',fontsize=fsize)
        plt.xlabel(r'$q$',fontsize=fsize)   
        plt.plot(x, correlsAll[0], 'kD--', label='5c', linewidth=2.0,markeredgewidth=e, markersize=s)
        plt.plot(x, correlsAll[1], 'rs--', label='6b', linewidth=2.0,markeredgewidth=e, markersize=s)
        plt.plot(x, correlsAll[2], 'b^--', label='8b', linewidth=2.0,markeredgewidth=e, markersize=s)
        plt.plot(x, correlsAll[3], 'r*--', label='8c', linewidth=2.0,markeredgewidth=e, markersize=s)
        plt.plot(x, correlsAll[4], 'gv--', label='V12', linewidth=2.0,markeredgewidth=e, markersize=s)
        plt.legend(loc = 2) # loc 4: bottom, right
        plt.show()
        
        print correls


        figure(2)

        if(False):
            xticks(x,range(-10,10)) # translate
            for j in range(vois):
                plt.ylim((-1, 1))
                plt.xlim(x1,x2)
                plt.title('VOI ' + str(j+1) + ' Measure ' + str(m))
                plt.ylabel(r'$\rho$',fontsize=fsize)
                plt.xlabel(r'$q$',fontsize=fsize)   
                #for p in range(len(patients)): 
                    #plt.plot(x, correls[p,j], 'kD--', linewidth=1.5, markeredgewidth=e, markersize=s)
                plt.plot(x, correls[0,j], 'kD--', label='5c', linewidth=2.0,markeredgewidth=e, markersize=s)
                plt.plot(x, correls[1,j], 'rs--', label='6b', linewidth=2.0,markeredgewidth=e, markersize=s)
                plt.plot(x, correls[2,j], 'b^--', label='8b', linewidth=2.0,markeredgewidth=e, markersize=s)
                plt.plot(x, correls[3,j], 'r*--', label='8c', linewidth=2.0,markeredgewidth=e, markersize=s)
                plt.plot(x, correls[4,j], 'gv--', label='V12', linewidth=2.0,markeredgewidth=e, markersize=s)
                plt.legend(loc = 3) # loc 4: bottom, right
                plt.show()




    np.save("correlsMeasures",correls)

    
