

l=[-10,-5,2,4,-15,-20,1,2]


max_sum=0
curr_sum=0
for i in range(len(l)):
    curr_sum=curr_sum+l[i]
    if curr_sum<0:
        curr_sum=0
    if max_sum<curr_sum:
        max_sum=curr_sum
print(max_sum)

