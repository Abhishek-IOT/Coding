"""
Using two pointers we check for the subarray from i to j and we will increase i if sum is greater than k.At current index j-i+1 
will be the count. 

"""


def main():
    n = int(input())
    k = int(input())
    b = [int(x) for x in input().split()]
    
    count = 0
    sum_val = 0
    i = 0
    
    for j in range(n):
        sum_val += b[j]
        
        while sum_val > k:
            sum_val -= b[i]
            i += 1
        
        count += (j - i + 1)
    
    print(count)

if __name__ == "__main__":
    main()
