class ImpossibleError(Exception):
    pass

class EndError(Exception):
    pass

def calc(players, s):
    players.sort(key = lambda x: x[0])

    result = []

    try:
        result.append(filter(lambda x: x[2] == "G", players)[0])
        result += filter(lambda x: x[2] == "D", players)[:s[0]]
        result += filter(lambda x: x[2] == "M", players)[:s[1]]
        result += filter(lambda x: x[2] == "S", players)[:s[2]]

        if len(result) != sum(s) + 1:
            raise ImpossibleError
        
        captain = [0, 0, 0, 0]
        flag = True
        for i in result[1:]:
            if (i[-1] > captain[-1]) or (i[-1] == captain[-1] and i[0] > captain[0]):
                captain = i
                flag = False
        if flag:
            raise ImpossibleError
        result.remove(captain)
        result.insert(0, captain)

        for i in result[:-1]:
            print i[0], i[1], i[2]
        print "%d %s %s\n" % (result[-1][0], result[-1][1], result[-1][2])
    except ImpossibleError:
        print "IMPOSSIBLE TO ARRANGE\n"

while 1:
    try:
        players = []
        s = []
        for i in range(22):
            t = raw_input()
            if t == "0":
                raise EndError
            player = t.split(" ")
            pl = []
            pl.append(int(player[0]))
            pl.append(player[1])
            pl.append(player[2])
            
            pl.append(0)
            for i in player[3:]:
                y = map(int, i.split("-"))
                pl[-1] = pl[-1] + y[1] - y[0] + 1
                    
            players.append(pl)
        
        s = map(int, raw_input().split("-"))
        calc(players, s)
    except EndError:
        break
