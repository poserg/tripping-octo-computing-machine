n, m = map(int, raw_input().split(" "))

matrix = []
for i in range(n):
    matrix.append(map(int, raw_input().split(" ")))
    
    
s = 0
x = 0
y = 0
d = ""
# for i in range(1,n):
#     t = 0
#     if (i > m):
#         k = m
#     else:
#         k = i
#     for j in range(0,k):
#         t += matrix[i][j]
#     if t > s:
#         s = t
#         x = i + 1
#         y = k + 1
#         d = "UP"

x_c = []
for i in range(m):
    x_c.append(0)
x_c = x_c + range(n)
y_c = []
y_c = range(m)
for i in range(n):
    y_c.append(0)

s = 0
mx = 0
my = 0
d = ""
for i in range(len(x_c)):
    x = x_c[i]
    y = y_c[i]
    t = 0
    r = min(n - x, m - y)
    if r <=1:
        break
    for j in range(r):
        t += matrix[x + j][y + j]
    if (t > s):
        s = t
        mx = x
        my = y
        d = "DOWN"
        
print s, x, y, d

        
