arrow = str(input())
count = 0
long = 0
for i in range (len(arrow)):
    if i + 4 < len(arrow) and arrow[i] == ">" and  arrow[i+1] == ">" and arrow[i+2] == "-" and arrow[i+3] == "-" and arrow[i+4] == ">":
        count += 1
        long = count
    elif i + 4 < len(arrow) and arrow[i] == "<" and  arrow[i+1] == "-" and arrow[i+2] == "-" and arrow[i+3] == "<" and arrow[i+4] == "<":
        count += 1
        long = count
print(long)

