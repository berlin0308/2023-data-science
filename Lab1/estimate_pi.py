"""C-2
The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate 
a numerical approximation of 1 / π: 

Write  a  function  called  estimate_pi()  that  uses  this  formula  to  compute  and  return  an 
estimate of π. It should use a while loop to compute terms of the summation until the last term 
is  smaller  than  1e-15  (which  is  Python  notation  for  10−15).  You  can  check  the  result  by 
comparing it to math.pi.

"""
import math
import numpy as np

def estimate_pi():

    sigma = 0.0
    for k in range(30):
        sigma += (math.factorial(4*k)*(1103+26390*k))/(math.pow(math.factorial(k), 4)*math.pow(396,4*k))

    reciprocal_pi = (2*math.sqrt(2.0))/9801*sigma
    pi = np.reciprocal(reciprocal_pi)
    return pi

if __name__ == '__main__':
    print(estimate_pi())
    print(format((estimate_pi()-math.pi), ".30f"))