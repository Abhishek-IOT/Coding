"""

Here the intution is that we will store the current sum every time in dictionary and everytime loop runs we will check 
for the current_sum - k(desired sum) if this value is present in dictionary or not if it is present we will 
add the current frequency of that sum.

"""





from collections import defaultdict

def subarraywithsumk(arr,k):
    d=defaultdict(int)
    d[0]=1
    s=0
    c=0
    for i in arr:
        s=s+i
        print(s,d)
        if (s-k) in d:
            print(s-k)
            c+=d[s-k]
        
        d[s]+=1
    return c
            

l=[1,2,3,4,5]
l=[1,0,1,2,10,5]
k=3
ans=subarraywithsumk(l,k)
print(ans)
    
    
    
