# -*- coding: utf-8 -*-
"""
Python script to plot the FSC from text file

Usage:
    python plotFSC.py <text file with frequence in column 1 and fsc in column 2> <output plot file>

Example:
    python plotFSC.py fsc.dat fsc.png
    
    or
    
    run plotFSC.py fsc.dat fsc.png
"""

#--------------------------------------------------------------------------------------
#import module
#--------------------------------------------------------------------------------------
import sys
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("numpy or matplotlib was not found")
    
    
#--------------------------------------------------------------------------------------
#check arguments
#--------------------------------------------------------------------------------------
if len(sys.argv)<3:
    print("Usage:\n\tpython"+sys.argv[0]+"<FSC file> <Output plot file>\n\n")
    sys.exit(1)

fsc_file=sys.argv[1]
output_file=sys.argv[2]

#-------------------------------------------------------------------------------------
#load fsc text file and transpose
#-------------------------------------------------------------------------------------
data=np.loadtxt(fsc_file,skiprows=3)
data=np.transpose(data)

#------------------------------------------------------------------------------------
#plot and custom
#------------------------------------------------------------------------------------
plt.plot(data[0],data[1],'b-') #color=blue, linestyle=dashline
plt.xlim(0,max(data[0]))
plt.ylim(0,1.0)
plt.title("FSC of merged data")
plt.xlabel("resolution ("+r"$\AA$"+")")
plt.ylabel("Fourier shell correlation")
ticks=np.linspace(min(data[0])+0.001,max(data[0])+0.001,10)
labels=np.round(np.reciprocal(ticks),1)
plt.xticks(ticks.tolist(),labels.tolist())
plt.axhline(y=0.143,xmin=0,xmax=1,color="r",label="FSC of 0.143")
plt.axhline(y=0.5,xmin=0,xmax=1,color="g",label="FSC of 0.5")
plt.legend()

#save plot to file
plt.savefig(output_file,dpi=300) #setup dpi according to need