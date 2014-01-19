from math import sqrt

def get_dim(person1, person2):
	return sqrt((person1[0] - person2[0])**2 + (person1[1] - person2[1])**2)

def update_item(result, person, dim):
	if result.has_key(person):
		result[person][0] += dim
		result[person][1] += 1
	else:
		result[person] = [dim, 1]

primer = int(raw_input())
for p in range(primer):
	n, m = map(int, raw_input().split(" "))

	person = {}
	for i in range(n):
	    t = raw_input().split(" ")
	    person[t[0]]=[int(t[1]), int(t[2])]
	    
	events = []
	for i in range(m):
	    t = raw_input().split(" ")
	    events.append([t[0], t[2], t[5]])
	    

	result = {}
	for i in events:
		visor = person[i[0]]
		person1 = person[i[1]]
		person2 = person[i[2]]
		d1 = get_dim(visor, person1)
		d2 = get_dim(visor, person2)

		update_item(result, i[1], d1)
		update_item(result, i[2], -d2)

	result_list = []
	for i in result:
		result_list.append([i, result[i]])
	
	if len(filter(lambda x: x[1][1] < 2, result_list)) > 0:
		print "UNKNOWN"
	else:
		result_list.sort(key = lambda x: x[1][0])

		str = ""
		is_impossible = False
		for i in range(len(result_list) - 1):
			if result_list[i][1][0] == result_list[i+1][1][0]:
				is_impossible = True
				break
			str += result_list[i][0] + " "
		
		if is_impossible:
			print "IMPOSSIBLE"
		else:
			str += result_list[-1][0]
			print str