"""
https://www.programiz.com/python-programming/online-compiler/

Intuition : We are storing the prefix sum and if we are getting sum as 0 that means we will increase count and if we are getting sum
as one that is already present in dictionary that means that many times the subarray has been formed in between so we will increase count
with frequency

"""





l=[1,0,0,1]
d={}
s=0
c=0
for i in l :
    if i==0:
        i=-1
    s=s+i
    print(s, end=' ')
    print(d,c)
    if s==0:
        c=c+1
    if s in d:
        c+=d[s]
    if s not in d:
        d[s]=1
    else :
        d[s]+=1
print(c)
print(d)
