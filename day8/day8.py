class Layer(object):
	def __init__(self,layer_number,content):
		self.layer_number = layer_number
		self.content = content
	def count_of_number(self,number):
		count = 0
		for i in range(len(self.content)):
			for k in range(len(self.content[i])):
				if self.content[i][k] == number:
					count+=1
		return count

f = open("input.txt")
text = f.read()
f.close()
width = 25
height = 6

'''
text = "0222112222120000"
width = 2
height = 2
'''
num_of_layers = len(text)/width/height

#print num_of_layers 
layers = []
for i in range(num_of_layers):
	layer_length = width*height
	start = layer_length*i
	end = start+layer_length
	layer_text = text[start:end]
	#print len(layer_text)
	#print "Making layer %s starting at %s and ends at %s" % ((i+1),start,end)
	layer = []
	for x in range(height):
		layer.append([])
		for y in range(width):
			#print x,y
			layer[x].append(layer_text[(x*height)+y])
	layers.append(Layer(i+1,layer))
	print layer
min_layer = None
for layer in layers:
	#print "layer %s" % layer.layer_number
	#print layer.content
	if min_layer == None:
		min_layer = layer
	if layer.count_of_number("0") < min_layer.count_of_number("0"):
		min_layer = layer
print min_layer.count_of_number("1") * min_layer.count_of_number("2")

final_output = []
for x in range(height):
	final_output.append([])
	for y in range(width):
		final_output[x].append("2")
print final_output
for i in range(len(layers)):
	l = layers[i].content
	for x in range(len(l)):
		for y in range(len(l[x])):
			if final_output[x][y] == "2" and not l[x][y] == "2":
				final_output[x][y] = int(l[x][y])
#print final_output
for l in final_output:
	print l
	