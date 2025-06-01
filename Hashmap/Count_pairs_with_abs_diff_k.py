"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

Intuition : We are finding the frequency of all the elements in hashmaps and then iterating the array again and check current value with 
difference of k is present in hashmap or not if present we are increasing count. but this will have count twice so at end we need to divide it by 2.
"""

l=[1,2,2,1]
l=[1,2,2,1,1,2]
l=[1,3]
t=1

# c=0
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if abs(l[j]-l[i])==t:
#             c=c+1
# print(c)

d={}
for i in l:
    if i in d:
        d[i]+=1
    else :
        d[i]=1
c=0
k=1
print(d)
for i in l:
    print(i,i+k,i-k,d)
    if i+k in d:
        c=c+d[i+1]
    if i-k in d:
        c=c+d[i-1]
print(c//2)
