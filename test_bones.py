
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import sys
sys.path.append('/home/rodrigo/imfractal/imfractal/Algorithm/')

import qs3D



def do_test():

    path = "/home/rodrigo/rodrigo/rodrigo/members.imaglabs.org/felix.thomsen/Rodrigo/VertebraPhantom/mats/"

    patients = ["5c", "6b", "8b", "8c", "V12"]
    scans = ["01", "02", "03", "M1", "M2", "XCT"]
    # amount of volumes of interest
    vois = 27
    dims = 10

    # bone's multifractal spectra database
    mfss = np.zeros([len(patients),len(scans),vois,2*dims+1])

    aux = CSandbox3D(dims)

    slices = "slices"
    masks = "masks"

    ii = 0
    for i in patients:
        jj = 0
        for j in scans:
            for k in range(1,vois+1):
                fmask = path+masks+i+j+".mat"
                # set voi number and mask filename
                params = [1,0.75,3.7,1,15,k,fmask,slices,masks]
                aux.setDef(40,1.02,True,params)

                filename = path+slices+i+j+".mat"

                print i,j,"voi: ",k
                print fmask
                print filename

                mfss[ii,jj,k-1] = aux.getFDs(filename)

            jj = jj+1

        ii = ii+1


    np.save("mfss",mfss)



    exit()

    plt.figure(1)
    plt.subplot(121)
    plt.ylim(ymax = 3.8, ymin = 2.4)
    #plt.title("XCT 5c_XtremeCTSlices")
    plt.title("HRCT 5c_O1_120Slices")
    plt.plot(fds2)
    plt.subplot(122)
    plt.imshow(arr2[:,:,40],plt.get_cmap('gray'))
    plt.show()

    exit()

    
