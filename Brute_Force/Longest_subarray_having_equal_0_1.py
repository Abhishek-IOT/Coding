"""

https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/

"""



l=[1, 0, 1, 1, 1, 0, 0]
l=[0, 0, 1, 1, 0]
l=[1]

if len(l)==1:
    print(0)
    exit()
max_sub=0
for i in range(len(l)):
    c0=0
    c1=0
    start=i
    end=i+1
    if l[start]==1:
        c1=c1+1
    else :
        c0=c0+1
    while(start<end and end<len(l)):
        
        if  l[end]==0:
            c0=c0+1
        if  l[end]==1:
            c1=c1+1
        print(c0,c1,l[start:end+1])
        if c0==c1:
            max_sub=max(max_sub,end-start)
        
        end=end+1
print(max_sub+1)
        
    






