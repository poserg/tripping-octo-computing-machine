n = int(raw_input())
t = map(int, raw_input().split(" "))

result = []
chet = {}
chet_count = 0
noll = []
for i in range(n):
    if (t[i] == 0):
        noll.append(i)
        chet[i] = chet_count
        chet_count += 1
    elif (t[i] % 2 == 0):
        chet_count += 1
        
s = ""
n = len(noll)
for i in range(n):
    t = chet[noll[i]] + n - i - 1
    s += str(t) + " "

print s
