import numpy as np                                                        

import matplotlib.pyplot as plt                                           

from math import sqrt

import trsfile
task = trsfile.open('sample/task.trs'  ,"r")
t=[i  for i in range(10,len(task[0])-2) if task[0][i-1]==0 and task[0][i] in {19,20,22} and task[0][i+1]==0 and task[0][i+2]==0 ]
n=[-1 if 32 in task[0][x:y] else 0 for x,y in zip(t,t[1:]+[-1])]
print(n)