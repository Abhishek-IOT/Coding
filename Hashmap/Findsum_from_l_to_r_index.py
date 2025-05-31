"""

William Macfarlane wants to look at an array.

You are given a list of N numbers and Q queries. Each query is specified by two numbers i and j; the answer to each query is the sum of every number between the range [i, j] (inclusive).

Note: the query ranges are specified using 0-based indexing.

Input
The first line contains N, the number of integers in our list (N ≤ 100,000). The next line holds N numbers that are guaranteed to fit inside an integer. Following the list is a number Q (Q ≤ 10,000). The next Q lines each contain two numbers i and j which specify a query you must answer (0 ≤ i, j ≤ N-1).

Output
For each query, output the answer to that query on its own line in the order the queries were made.

Example
Input:
3
1 4 1
3
1 1
1 2
0 2

Output:
4
5
6

"""

def find_sum(l,left,right):
    if right==len(l)-1 and left==0:
        return sum(l)

    if left==right and left<len(l)+1:
        return l[left]
    p=[0]*(len(l))

    p[0]=l[0]

    for i in range(1,len(l)):
        p[i]=p[i-1]+l[i]
    print(p)
    return p[right]-p[left-1]


l=int(input())
arr= list(map(int, input("Enter space-separated numbers: ").split()))
print(arr)

q=int(input())
for i in range(q):
    left=int(input())
    right=int(input())
    print(find_sum(arr,left,right))    



