def process_items(items):
	for i in range(len(items)):
			items[i] = int(items[i])
	for i in range(len(items)/4):
		index = i*4
		code = items[index]
		if code == 99:
			break
		elif code == 1:
			items[items[index+3]] = items[items[index+1]] + items[items[index+2]]
		elif code == 2:
			items[items[index+3]] = items[items[index+1]] * items[items[index+2]]
		else:
			print "ERROR"
	return items[0]
file_path = "input2.txt"
f = open(file_path)
items = f.read().split(',')
print process_items(items)