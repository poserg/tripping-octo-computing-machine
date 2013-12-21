primer = int(raw_input())

n, m = map(int, raw_input().split(" "))

person = []
for i in range(n):
    t = raw_input().split(" ")
    person.append([t[0], int(t[1]), int(t[2])])
    
events = []
for i in range(m):
    t = raw_input().split(" ")
    events.append([t[0], t[2], t[5]])
    

result = []
for i in events:
    
