
"""
Longest subarray with sum equal or less than k.
We are checking it using Two pointers and every time we will calculate the current length and check it with max length and udpate max 
length with current length if current length is greater.

"""


l=[1,2,3,4,5,6,7,8,9,10]
k=10
i=0
s=0
max_len=0
for j in range(len(l)):
    s=s+l[j]
    
    while(s>k):
        s=s-l[i]
        i=i+1
    
    max_len=max(max_len,j-i+1)
    
print(max_len)
        
        