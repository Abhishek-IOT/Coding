"""
https://www.geeksforgeeks.org/count-subarrays-equal-number-1s-0s/

"""



l=[1,0,0,1,0,1,1]
l=[1, 0, 0, 1, 1, 0, 0, 1]

c=0
for i in range(len(l)):
    start=i
    end=i+1
    c0=0
    c1=0
    if l[start]==0:
        c0=c0+1
    else :
        c1=c1+1
    while(start<end and end<len(l)):
        if l[end]==1:
            c1=c1+1
        else :
            c0=c0+1
        if c0==c1:
            c+=1
        end=end+1
print(c)


