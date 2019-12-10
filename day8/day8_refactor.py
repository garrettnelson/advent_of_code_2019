def count_of_items(l,item):
	count = 0
	for i in range(len(l)):
		count+= l[i].count(item)
	return count
f = open("input.txt")
text = f.read()
f.close()


width = 25
height = 6


total_chars = height*width
num_of_layers = len(text)/width/height

values = text
layers = []
combination = []
#initialize combination array
for x in range(height):
	combination.append([])
	for y in range(width):
		combination[x].append(2)
for i in range(num_of_layers):
	start_position = i*total_chars
	end_position = start_position+total_chars
	layer_text = values[start_position:end_position]
	#print layer_text
	layers.append([])
	for x in range(height):
		layers[i].append([])
		for y in range(width):
			#print x,y
			value = int(layer_text[x*width+y])
			layers[i][x].append(value)
			if combination[x][y] == 2:
				combination[x][y] = value
	#print "layer %s" % i
	#print layers[i]


min_layer = None
for i in range(len(layers)):
	l = layers[i]
	if min_layer == None or count_of_items(l,0) < count_of_items(min_layer,0):
		min_layer = l
print count_of_items(min_layer,1) * count_of_items(min_layer,2)

for x in range(len(combination)):
	print combination[x]

