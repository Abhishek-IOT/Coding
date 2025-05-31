"""
https://www.geeksforgeeks.org/maximum-distance-two-occurrences-element-array/

"""

"""
Using two iterations .
"""


l=[1, 1, 2, 2, 2, 5]

d={}

for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=i
max_dis=0    
for i in range(len(l)-1,-1,-1):
    if l[i] in d:
        max_dis=max(max_dis,i-d[l[i]])
print(d)
print(max_dis)


"""

Use One Iteration.

"""

d={}
max_dis=0
for i in range(len(l)):
    if l[i] not in d:
        d[l[i]]=i
    else :
        max_dis=max(max_dis,i-d[l[i]])
print(max_dis)