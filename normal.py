#!/opt/anaconda3/bin/python
import numpy as np

row = int(input())
column = int(input())
listt = []
for i in range(row):
    z = list(map(int, input().split()[:column]))
    listt.append(z)
    
print(np.transpose(listt))