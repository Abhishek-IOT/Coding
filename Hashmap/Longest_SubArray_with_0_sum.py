"""
https://www.geeksforgeeks.org/find-the-largest-subarray-with-0-sum/

Intuition : We will use prefix sum. If in the Predix Sum Array there are two matching sum that means the array in between has a sum of
0 and we will have find the max so we will use max variable.


"""





l=[15,0,0, -2, 2, -8, 1, 7, 10, 23]
#l=[1,2,3]
#l=[1,0,3]
#l=[0,0,0,0,0]
d={}
d[0]=-1
s=0
max_sub=0
for i in range(len(l)):
    s=s+l[i]
   
    if s not in d:
        d[s]=i
    else :
   #     print(i,s,l[i])
        max_sub=max(max_sub,i-d[s])
print(max_sub)
print(d)
        
    