m = int(input("array length"))
A = []
b = 0
for i in range(m):
    A.append(int(input()))
print("original", A)
b = A[0]
A[0] = A[m - 1]
A[m - 1] = b
print("resulting", A)

