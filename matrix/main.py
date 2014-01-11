def inc(t):
    return t + 1

def dec(t):
    return t - 1

def calc(x_c, y_c, s, mx, my, d, new_direction, condition, next_x, next_y):
    for i in range(len(x_c)):
        x = x_c[i]
        y = y_c[i]
        t = 0
        x_t, y_t = x, y
        while condition(x_t, y_t):
            t += matrix[y_t][x_t]
            x_t = next_x(x_t)
            y_t = next_y(y_t)
        if (t > s):
            s = t
            mx = x + 1
            my = y + 1
            d = new_direction
    return s, mx, my, d

while 1:
    n, m = map(int, raw_input().split(" "))
    if n == 0 and m == 0:
        break

    matrix = []
    for i in range(n):
        matrix.append(map(int, raw_input().split(" ")))

    s = 0
    x = 0
    y = 0
    d = ""

    x_c = [0 for x in range(n - 2)]
    x_c = x_c + range(m - 1)
    y_c = range(n - 2, -1, -1)
    y_c += [0 for x in range(m - 2)]

    s, mx, my, d = calc(x_c, y_c, 0, 0, 0, "", "DOWN", (lambda x, y: x < m and y < n), inc, inc)
            
    y_c = range(1, n)
    y_c += [n - 1 for x in range(m-2)]

    s, mx, my, d = calc(x_c, y_c, s, mx, my, d, "UP", (lambda x, y: x < m and y >=0), inc, dec)

    print my, mx, d, s

            
