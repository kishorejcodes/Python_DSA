def solve(N, X, A):
        if max(A[X:]) > A[-1]:
            return -1
        lMax = A[X]
        countL = []
        main_count = forwardSteps(lMax, X, A, count=0)
        countL.append(main_count)
        lMax = A[X]
        for i in range(X-1, -1, -1):
            count = 0
            if A[i] < lMax:pass
            else:
                count += 1
                if count > main_count: break
                lMax = A[i]
                count = forwardSteps(lMax, i, A, count)
                countL.append(count)
        return min(countL)

def forwardSteps(lMax, X, A, count):
            for j in range(X+1, len(A)):
                    if A[j] < lMax:pass
                    else:
                        count += 1
                        lMax = A[j]
            return count
        
print(solve(7,2,[8, 10, 4, 6, 9, 1, 11]))

'''
Problem Statement:
You are given an array A[] with N integr. You are initially
at index X. In one move, you can go from index I to any other index J such
that A[j] > A[i], and there is no such index k in between i and j
such that A[k]>A[i]. Find the minimum number of steps to reach the last index
of the array; if you can't get to the last index of the array, return -1.

Note: It is given that all element of array A is distinct.

TestCase:
Input : N = 4
        X = 0
        A[] = {1,2,4,7}
Output : 3

TestCase:
Input : N = 3
        X = 0
        A[] = {2,1,4}
Output: 1




7 2
8 10 4 6 9 1 11
2

7 1
12 8 9 10 11 13 14
3
'''