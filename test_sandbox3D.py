
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

import sys
sys.path.append('/home/rodrigo/imfractal/imfractal/Algorithm/')

import qs3D



def do_test():
    filename = 'images/train2/bread/b1.png'
    #filename = 'images/warpbin.png'

    dims = 10
    
    params = np.array([1,0.75,3.7,1,15]).astype(np.float32)
    #arr = qs3D.volume(params,256,256)

    i = CSandbox3D(dims)
    i.setDef(40,1.02,True,params)
    fds2 = i.getFDs(filename)
    arr2 = i.readDicom("/home/rodrigo/dicom")

    for h in range(2):
        print "Computing 3D Cython Sandbox Multifractal Spectrum..."
        t =  time.clock()
        fds2 = np.vstack((fds2,i.getFDs(filename)))
        t =  time.clock()-t
    plt.figure(1)
    plt.subplot(121)
    plt.ylim(ymax = 3.8, ymin = 2.4)
    plt.title(str(params))
    plt.boxplot(fds2, sym='')#, 'b*', label='synthetic',linewidth=2.0)
    plt.subplot(122)

    plt.imshow(arr2[:,:,220],plt.get_cmap('gray'))
    plt.show()

    
