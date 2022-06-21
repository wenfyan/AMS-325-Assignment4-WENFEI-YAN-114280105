# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt
def markov(n,N):
    """
    Create a n*1 probability distribution vector and a n*n transition matrix
    to compute the markov transform process and analysis the relation between
    the times of iterations and the norm of difference of probability
    distribution and stationary statue.
    
    Parameters
    ----------
    n: int
        n is size of initial probability distribution vector, it also determine
        the size of transition matrix
    N: int
        N is the times of iteration by the transition matrix
    
    Returns
    ----------
    function return the plot of time of iteration by transition matrix against
    norm, norm is used to measure the difference bewteen the current statue of 
    probability distribution and stationary statue
    
    See Also
    --------
    np.linalg.eig: compute the eigenvalue and corresponding eigenvectors of a 
    square matrix
    np.argmax: return index of the largest entries of an array
    np.dot: compute dot product of matrix and array
    """
    p_origin=np.random.rand(n, 1) #generate a random number array
    s=sum(p_origin) 
    p=p_origin/s #scale their values to make their sum is 1
    P_transition=np.random.rand(n,n) #generate a random number matrix
    P=np.zeros((n,n))
    for i in range(n): #using for loop to calculate the sum of each row
        S=sum(P_transition[i])
        for j in range(n):
            P[i][j]=P_transition[i][j]/S #scale each row
    
    
    
    eigen=np.linalg.eig(P) #compute the eigenvalue value 
    eigenvalues=eigen[0] 
    eigenvectors=eigen[1]
    max_index=np.argmax(eigenvalues) #pick out the largest eigenvalue
    max_eigenvector=np.zeros((n,1))
    for l in range(n):
        max_eigenvector[l]=eigenvectors[l][max_index] #because the corresponding
        #eigenvector is listed as columns, so use for loop to pick it out
    s_eigen=sum(max_eigenvector)
    p_stationary=max_eigenvector/s_eigen #scale the eigenvector
    
    
    norms=np.zeros((1,N))
    iteration=np.zeros((1,N))
    for k in range(N): #iteration N time by transition matrix
        temp=np.dot(P,p) #create variable temp to store the value of dot product
        p=temp #assign it to p to renew the value of p
        p_difference=p-p_stationary #compute the difference of two arrays
        norm=0
        for m in range(n): #using for loop to compute the norm of difference
            norm+=(p_difference[m])**2
        norm=math.sqrt(norm)
        norms[0][k]=norm
        iteration[0][k]=k+1 #count the time of iteration 
    
    return plt.plot(iteration,norms,'bo') 
    #plot the figure of norm against times of iteration as the return of the function


n=5
N=50 #set intended value and call the function
markov(n,N)
    
        
    




    