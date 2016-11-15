
from imfractal import MFS

import time

def do_test():
    
    filename = 'images/baguette2.tif'
    i = MFS()
    i.setDef(1,20,3)
    print "Calculating Lipschitz-Holder Multifractal Spectrum..."
    t =  time.clock()
    fds = i.getFDs(filename)
    t =  time.clock()-t
    print "Time MFS: ", t
    print fds
