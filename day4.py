import re
def valid_number(input):
	has_double = False
	decreases = False


	number = input
	str_rep = str(number)
	doubles = []
	for str_index in range(len(str_rep)-1):
		digit = str_rep[str_index]
		next_digit = str_rep[str_index+1]

		num_digit = int("%s" % digit)
		num_next_digit = int("%s" % next_digit)
		if num_next_digit < num_digit:
			decreases = True
			break
		if num_digit == num_next_digit:
			has_double = True
			if not digit in doubles:
				doubles.append(digit)
	if has_double == True and decreases == False:
		has_at_least_one_solo_double = False
		for d in doubles:
			if str_rep.count(d) == 2:
				has_at_least_one_solo_double = True
		if has_at_least_one_solo_double == True:
			return True
		else:
			return False
	else:
		return False


test1 = 111111
test2 = 223450
test3 = 123789
print "Test 1 is %s" % (valid_number(test1))
print "Test 2 is %s" % (valid_number(test2))
print "Test 3 is %s" % (valid_number(test3))
print "Test 4 is %s" % (valid_number(29336))
values = []
start = 367479
end = 893698
r = abs(367479-893698)
for i in range(r):
	test = i+start
	if valid_number(test):
		values.append(test)
print values
print len(values)
