"""
https://leetcode.com/problems/longest-consecutive-sequence/description/

Intution: We sorted the array and have two pointers to check for longest sequence.
"""





l=[100,4,200,1,3,2]
l=[0,3,7,2,5,8,4,6,0,1]

l.sort()
j=0
start=0
end=0
for i in range(len(l)-1):
    print(l[i],l[i+1])
    if l[i]==l[i+1]-1:
        end=end+1
        j=max(j,end-start+1)
    
    else :
        start=i+1
        end=i+1
print(j)