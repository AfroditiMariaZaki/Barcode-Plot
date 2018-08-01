"""
#Distances Barcode Plot Version 1.0 01/08/2018
#Author: Aphroditi Maria Zaki
#Institution: University of Oxford

"""


"""

#This code plots a 2D array of data in a barcode plot

"""

# Import relevant programs
import os
#import sys
import pylab

# Import plotting package
#import matplotlib.pyplot as plt
import numpy as np

# Get name of current directory
dirpath = os.getcwd()
dir=os.path.basename(dirpath)

# Get array of random values
data=np.random.rand(4,100)

# Plot the 2D array
#pylab.matshow(data, cmap='RdBu', vmin=0, vmax=1.6)
pylab.pcolormesh(data, cmap='RdBu', vmin=0, vmax=1.0)
pylab.title("Barcode Plot")
pylab.xlabel("Time / ns")
#pylab.ylabel("Residue Name")
cbar=pylab.colorbar()
cbar.set_label("Distance / nm")
cbar.ax.get_yaxis().labelpad = 15
pylab.xticks(np.arange(0,101,20))
pylab.yticks(np.arange(4), ("GLY", "LYS", "LEU", "TYR"))
#plt.tick_params(axis='x', bottom='True', top='True', which='major', labelbottom='True', labeltop='False', direction='in', labelsize=10)
#pylab.show()

# Save the image
pylab.savefig('barcode-%s.png' %dir, bbox_inches='tight', dpi=600)

