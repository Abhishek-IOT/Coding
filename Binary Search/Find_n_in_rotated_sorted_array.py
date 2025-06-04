"""

In this problem the array is sorted but it rotated unanonymus times.We need to find the element in array.

Intiution : We will calculate mid and check if it is less or more than first value of array . If it is greater that means mid is in first sorted range
Then we will check from 0 to mid if target element lies in that range or not . if yes we will make r=mid-1 or else we will l=mid+1 to 
check next sorted subarray.

"""







arr=[3,4,5,6,7,1,2]
t=7

l=0
r=len(arr)
while(l<=r):
    mid=(l+r)//2
    if arr[mid]==t:
        print(mid)    

    if arr[mid]>=arr[0]:
        if t>arr[mid] or t<arr[0]:
            l=mid+1
        else :
            r=mid-1
        
        #print('kkskk',l,r)  
    else:
        if t<arr[mid] or t>arr[len(arr)-1]:
            r=mid-1
        else :
            l=mid+1
        #print('aaaa',l,r)

    #print(arr[mid])




