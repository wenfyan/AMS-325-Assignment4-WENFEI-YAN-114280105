# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(n,N_max,threshold):
    """
    Draw the mandelbrot set on a part of coordinates
    
    By dividing the area into n*n blacks, compute all the cross point by the 
    mandelbrot iteration, after N_max iterations, if the absolute value of z is
    still in the threshold, then the point will be drawn as white
    
    Parameters
    ----------
    n: int
        n means the area will be divided into n*n parts and generate n**2 points
        the more points there are, the more accurate the figure is
    N_max: int
        N_max desides number of times the mandelbrot iteration be applied.
        the value of finial z change as the N_max change
    threshold: int
        threshold is used to compare with absolute value of z to desides which
        z and its corresponding x,y is in mandelbrot set.
        
    Returns
    ----------
    function return the figure of mandelbrot set on a limited area of coordinates
    
    """
    xvalues=np.linspace(-2,1,n) #create n points between -2 and 1 with equal distance
    yvalues=np.linspace(-1.5,1.5,n) #create n points between -1.5 and 1.5 with equal distance
    xx, yy = np.meshgrid(xvalues, yvalues,indexing='xy')
    #combine the two division into n*n points and store their coordinate



    C=np.zeros((n,n),dtype=complex) #create an array to store the complex number that each point corresponding
    for a in range(n):
        for b in range(n):
            C[a][b]=xx[a][b]+1j*yy[a][b] #write the value of complex number

    mask=np.zeros((n,n),dtype=bool) #create an array of boolean value to store each point is in the threshold or not
    for k in range(n):
        for l in range(n):
            z=0
            for m in range(N_max):
                z=z**2+C[k][l] #implement the mandelbrot iteration
    
            if abs(z)<threshold:
                mask[k][l]=True #set the value of entre in mask as true if z is in the threshold
            else:
                mask[k][l]=False #false if not


    plt.imshow(mask, extent=[-2,1,-1.5,1.5]) #use the code in the homework pdf as instructed but not use mask.T, the figure will be same as example
    plt.savefig('mandelbrot.png')
    return plt.gray() #return must be put after the plt.savefig, otherwise the sentence will not be excuted

    #end of function part


n=1000
N_max=50
threshold=50
mandelbrot(n,N_max,threshold)

