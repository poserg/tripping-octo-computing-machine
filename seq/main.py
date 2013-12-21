n = int(raw_input())
t = map(int, raw_input().split(" "))

result = []
for i in range(n):
    if (t[i] == 0):
        k = len(filter(lambda x: x%2 == 0, t[0:i]))
        k += len(filter(lambda x: x == 0, t[i+1:]))
        result.append(k)
        
s = ""
for i in result[:-1]:
    s += str(i) + " "
s += str(result[-1])

print s
