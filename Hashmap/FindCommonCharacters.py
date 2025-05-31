"""




"""

words = ["bella","label","roller"]
 
min_freq=dict()
for ch in range(ord('a'), ord('z') + 1):
	min_freq[chr(ch)] = float('inf')


for i in range(len(words)):
    d={}
    for j in words[i]:
        
        print(j,end='')
        if j in d:
            d[j]+=1
        else :
            d[j]=1
    print(d)
        
    
    for k in range(26):
        if chr(k+97) in d:
            min_freq[chr(k+97)]=min(min_freq[chr(k+97)],d[chr(k+97)])
        else:
            min_freq[chr(k+97)]=0
    print()
print(min_freq)
l=[]
for i in min_freq:
    if min_freq[i]<0:
        pass
    else :
        for j in range(min_freq[i]):
            l.append(i)
print(l)
    


