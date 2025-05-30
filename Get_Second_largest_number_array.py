"""
When we need to get the second largest number in list what we can do is we can iterate over array and check if current value is greater than 
largest we will assign value of largest to secnd largest and current value to largest sum.

Suppose we have got the largest value in middle then we will iterate the remaining array and check for 2nd largest value by giving condition that
current_val < largest and more then largest sum. 

"""


l=[1,4,5,10,12,34]

largest=-1
second_largest=-1

for i in range(len(l)):
    if l[i]>largest:
        second_largest=largest
        largest=l[i]
    
    if l[i]< largest and l[i]>second_largest:
        second_largest=l[i]
print(largest)
print(second_largest)


