a = input()
b = a.split(" ")

print("Purchase frequency:")
for i in range(len(b)):
    c = b.count(b[i])
    if b.index(b[i]) == i:
        print(b[i], ":", c)

count = 0
popular = 0

for i in range(len(b)):
    c = b.count(b[i])
    if c > count:
        count = c
        popular = b[i]

print("Most popular item:", popular)

print("Purchased once:", end=" ")
printed = []
for i in range(len(b)):
    if b.count(b[i]) == 1 and b[i] not in printed:
        print(b[i], end=" ")
        printed.append(b[i])
print()

print("Sorted by frequency:")
used = []
for _ in range(len(set(b))):
    max_count = 0
    max_item = 0
    for item in b:
        if item not in used:
            c = b.count(item)
            if c > max_count:
                max_count = c
                max_item = item
    print(max_item, max_count)
    used.append(max_item)
