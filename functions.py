def indentify_operation(opcode):
	if opcode == 99:
		return 'exit'
	elif opcode == 1:
		return 'add'
	elif opcode == 2:
		return 'mult'
	else
		return 'unknown'
def process_text_array(file_path):
	f = open(file_path)
	text = f.read()
	f.close()
	items = text.split(',')
	for i in range(len(items)):
		items[i] = int(items[i])
	return items
