"""
We will be given an array and we need to provide the count of the shortest subarray and longest subarray

For Example:
l=[2,3,3,2,3,1,1,1,1,1,1,1,1,8,8]
SubArray :
[2,3,3]
[3,3,2]
[3,2,3]
[1,1,1,1,1,1,1]
[8]
[8]


Count of largest Subarray : [1,1,1,1,1,1,1] : 1
Count of shortest Subarray : [8] : 2
"""


"""
Brute force Approach
"""
l=[2,3,3,2,3,1,1,1,1,1,1,1,1,8,8]
k=8
m=[]
m1=[]
max_s=0
min_s=10000000
for i in range(len(l)):
    s=0
    for j in range(i,len(l)):
        s=s+l[j]
        if s==k and j-i+1>=max_s:
            max_s=j-i+1
            m.append(max_s)
        if s==k and j-i+1<=min_s:
            min_s=j-i+1
            m1.append(min_s)
print(max(m))
c=0
for i in m:
    if max(m)==i:
        c=c+1
print(c)
c=0
print(m1)
for i in m1:
    if min(m1)==i:
        c=c+1
print(c)


"""
Optimized Approach : WE will use Hashmap and then we will store the presum and then if max_length is hit we will check for count
"""



l=[2,3,2,3,2,1,1,1,1,1,1,1,1,8,8]
l=[2,3,2,3,2,3,2,3,2,3,8,8]
d={}
c=0
s=0
k=8
m=[]
m1=[]
max_s=0
min_s=1000000000
for i in range(len(l)):
    s=s+l[i]
    
    if s-k in d:
        j=d[s-k]+1
        cur_len=i-j+1
        if cur_len>=max_s:
            max_s=cur_len
            m.append(max_s)
        if cur_len<=min_s:
            min_s=cur_len
            m1.append(min_s)
        
    if s not in d:
        d[s]=i
        
print(d)
for i in m:
    if max(m)==i:
        c=c+1
print(c)
c=0
for i in m1:
    if min(m1)==i:
        c=c+1
print(c)
    