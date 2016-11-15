
from imfractal import *

import Image
import time
import matplotlib.pyplot as plt
from pylab import *

def do_test():
    filename = 'images/train2/bread/b1.png'
    #filename = 'images/warpbin.png'

    dims = 10

    i = Sandbox(dims)
    i.setDef(40,1.02,True)

    print "Computing Sandbox Multifractal Spectrum..."
    t =  time.clock()
    fds2 = i.getFDs(filename)
    t =  time.clock()-t
    plt.plot(range(-dims,dims+1), fds2, 'b*', label='synthetic',linewidth=2.0)
    plt.show()
    print "Time Sandbox: ", t
    print fds2

