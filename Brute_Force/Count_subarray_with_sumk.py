
"""
https://www.geeksforgeeks.org/number-subarrays-sum-exactly-equal-k/

"""


l=[10, 2, -2, -20, 10]
l=[9, 4, 20, 3, 10, 5]
l=[1, 3, 5]

k=-10
k=33
k=2
c=0
for i in range(len(l)):
    start=i
    end=i+1
    s=l[start]
    if s==k:
        c=c+1
    while(start<end and end <len(l)):
        s=s+l[end]
        if s==k:
            c=c+1
        end=end+1
print(c)