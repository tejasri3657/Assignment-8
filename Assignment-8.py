# -*- coding: utf-8 -*-
"""Assignment-8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bwld87MW6NKLyk6ZJyhrgVWv1SaXCkl6
"""

"""Assignment-9.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/16PveVTChQ2hQS9EMT8b-JokY-EBVOOkJ
"""

import numpy as np
import matplotlib.pyplot as plt

#if using termux
import subprocess
import shlex
#end if

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
  return x_AB

#Triangle vertices
A = np.array([1,-2,3]) 
B = np.array([3,4,-5]) 
m=2
n=3



# To find the point P which divides AB in the ratio 2 : 3
#Section ratio
#Section point
P = (m*B+n*A)/(m+n)
print(P)



#Generating all lines
x_AP = line_gen(A,P)
x_PB = line_gen(P,B)

 

#Plotting all lines
plt.plot(x_AP[0,:],x_AP[1,:])
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:])
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')



plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.02), B[1] * (1) , 'B')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1), P[1] * (1 + 0.02) , 'P')





plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()