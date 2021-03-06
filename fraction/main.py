accuracy = 6

precision = 0.00000001
exs = []

count = raw_input()
for i in range(int(count)):
    t = raw_input()
    exs.append(t.split())
    
def getFrac(n, m):
    s = 0
    for i in range(1, n + 1):
        k = (m + i)*1.0/fact(i)
        s += k

        if k < precision:
            break
    return s
        
def fact(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*fact(n-1)

    
result = []
for i in exs:
    result.append(getFrac(int(i[0]), int(i[1])))
    
for i in result:
    print round(i, accuracy)
    
