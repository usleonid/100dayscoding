# Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x.

# This python program tells if there exists a pair in array whose sum results in x.

# Function to find and print pair


def chkPair(A, size, x):
    for i in range(size - 1):
        for j in range(i + 1, size):
            if (A[i] + A[j] == x):
                print(A[i], A[j])
                return 1
    return 0


A = [0, -1, 2, -3, 1]
x = -2
size = len(A)

if (chkPair(A, size, x)):
    print("Yes")

else:
    print("No")
