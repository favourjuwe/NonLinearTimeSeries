
from imfractal import *

import time

def do_test():
    #path = '/almacen/members.imaglabs.org/felix.thomsen/Rodrigo/BioAsset/mats/'
    #filename = path + 'BA01_120_1Slices.mat'
    #file_mask = path + 'BA01_120_1Mask.mat'
    #i = MFS_3D()
    #i.setDef(1, 20, 3, filename, file_mask)
    #print "Calculating 3D MFS Multifractal Spectrum (Holder)..."
    #t = time.clock()
    #fds3 = i.getFDs()
    #t = time.clock() - t
    #print "Time 3D MFS: ", t
    #print fds3


    filename = 'images/baguette2.tif'#fractal20Bread.png'
    i = MFS()
    i.setDef(1,20,3)
    print "Calculating MFS Multifractal Spectrum..."
    t =  time.clock()
    fds3 = i.getFDs(filename)
    t =  time.clock()-t
    print "Time MFS: ", t
    print fds3

    i = Singularity(20)

#    print "Calculating Singularity Multifractal Spectrum..."
    #t =  time.clock()
    #fds = i.getFDs(filename)
    #t =  time.clock()-t
    #print "Time Singularity: ", t
    #print fds

    i = Sandbox(14)
    i.setDef(40,1.15, True)

    print "Calculating Sandbox Multifractal Spectrum..."
    t =  time.clock()
    fds2 = i.getFDs(filename)
    t =  time.clock()-t
    print "Time Sandbox: ", t
    print fds2

