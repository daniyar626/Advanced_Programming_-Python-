n = int(input())

for i in range(1, n + 1):
    s = str(i)
    count = 1   # предполагаем, что число подходит

    for j in range(len(s)):
        a = int(s[j])

        if a == 0 or i % a != 0:
            count = 0
            break

    if count == 1:
        print(i, end=" ")
