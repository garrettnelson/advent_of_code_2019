import itertools
from opcomputer import OPcodeComputer,Amplifiers
ampers = [0,1,2,3,4]
max_result = 0
max_amps = None
for test in itertools.permutations(ampers):
	a = Amplifiers("input.txt",test)
	result = int(a.fire_amps())
	if result > max_result:
		max_result = result
		max_amps = test
print max_result
print max_amps