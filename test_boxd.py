
from imfractal import *

import Image
import time

def do_test():
    filename = 'images/baguette2.tif'

    i = Boxdimension()
    i.setDef(40,1.15)

    print "Computing Box Dimension..."
    #t =  time.clock()
    fds = i.getFDs(filename)
    #t =  time.clock()-t
    #print "Time Boxdimension: ", t
    print fds

