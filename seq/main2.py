n = int(raw_input())
t = map(int, raw_input().split(" "))

result = []
chet = 0
noll = 0
for i in range(n):
    if (t[i] == 0):
        result = list(map(lambda x: x + 1, result))
        result.append(chet)
        chet = chet + 1
    elif (t[i] % 2 == 0):
        chet = chet + 1
        
s = ""
for i in result[:-1]:
    s += str(i) + " "
s += str(result[-1])

print s
