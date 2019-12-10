def calculate_gas(mass):
	gas_needed =  int((mass)/3)-2
	if gas_needed <= 0:
		return 0
	else:
		return gas_needed + calculate_gas(gas_needed)

file_path = "input1.txt"
f = open(file_path)
text = f.read()
items = text.split("\n")
for i in range(len(items)):
	numeric = int(items[i])
	items[i] = numeric
total_gas = 0
for item in items:
	total_gas += calculate_gas(item)
print total_gas

