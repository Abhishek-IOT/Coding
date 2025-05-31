"""

Zscalar OA Question :
Question was that we had to update the largest with second largest until it is equal to minimum value and we needed to count the steps that how many steps are required in it.
 



"""


def second_largest_number(l):
    ll=-1
    sl=-1
    
    for i in range(len(l)):
        if l[i]>ll:
            sl=ll
            ll=l[i]
        
        elif l[i]< ll and l[i]>sl:
            sl=l[i]
    return sl

def largest_number(l):
    ll=-1
    val=[]
    for i in range(len(l)):
        if l[i]>ll:
            ll=l[i]
    for i in range(len(l)):
        if l[i]==ll:
            val.append(i)
           
    return val



l=[4,5,5,5,2,4]

u=0
c=0
while(u==0):
    if max(l)==min(l):
        u=1
        break
    sec=second_largest_number(l)
    li=largest_number(l)
    print(li, l)
    for i in li:
       
        l[i]=sec
        c=c+1
print(c)
print(l)
    
    
    
    

    
    
    
    