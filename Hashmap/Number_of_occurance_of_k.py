"""
Problem Link : https://www.geeksforgeeks.org/find-frequency-number-array/

"""

from collections import defaultdict

def find_occurances(l,k):

    d=defaultdict(int)
    for i in l :
        d[i]+=1
    
    if k in d:
        return d[k]
    else :
        return -1


l=[0,5,5,5,4]
d=find_occurances(l,5)
print(d)


