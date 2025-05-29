"""
We kept the count of the values in dictionary and then according to the character values we appended it in new lists.

"""



s='abaacbd'
print(ord('a'))

d={}
for i in s:
    if i in d:
        d[i]+=1
    else :
        d[i]=1

print(d)
m=''
for i in range(97,124):
    if chr(i) in d:
        for j in range(d[chr(i)]):
            m=m+chr(i)
print(m)
            
        
    

    
    