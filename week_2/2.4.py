a = int(input())
b = int(input())
c = str(input())
count = 0
set_words = set()
for i in range(len(c) + 1 - b):
    d = c[i : i + b]
    set_words.add(d)
print(len(set_words))