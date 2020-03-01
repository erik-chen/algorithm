import random
def counting_sort(A):
    n = len(A)
    k = max(A)
    B = [0] * n
    C = [0] * k
    for i in range(n):
        C[A[i]-1] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    print(C)
    for i in range(n-1, -1, -1):
        B[C[A[i]-1]-1] = A[i]
        C[A[i]-1] -= 1
    print(B)


A = [random.randint(1, 255) for _ in range(500)]
print(counting_sort([3,4,4,4,4]))