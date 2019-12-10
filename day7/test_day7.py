from opcomputer import OPcodeComputer,Amplifiers
import unittest
import sys
class TestModes(unittest.TestCase):
	def setUp(self):
		self.c = OPcodeComputer(input_path="1",parm=1)
	def test_0_modes(self):
		modes = self.c.get_param_modes()
		self.op_asserter(modes,0,0,0)
	def test_1_mode(self):
		for i in range(2):
			one = i
			string = str(one) + "00"
			self.c.instructions[self.c.current_position] = string
			modes = self.c.get_param_modes()
			self.op_asserter(modes,one,0,0)
	def test_2_modes(self):
		for i in range(2):
			one = i
			for j in range(2):
				two = j
				string = "%s%s" % (two,one) + "00"
				self.c.instructions[self.c.current_position] = string
				modes = self.c.get_param_modes()
				self.op_asserter(modes,one,two,0)

	def test_3_modes(self):
		for i in range(2):
			one = i
			for j in range(2):
				two = j
				for k in range(2):
					three = k
					string = "%s%s%s" % (three,two,one) + "00"
					self.c.instructions[self.c.current_position] = string
					modes = self.c.get_param_modes()
					self.op_asserter(modes,one,two,three)
	def op_asserter(self,modes,one,two,three):
		self.assertEqual(modes['param1'],one)
		self.assertEqual(modes['param2'],two)
		self.assertEqual(modes['param3'],three)
class TestGetParams(unittest.TestCase):
	def test_param_getter(self):
		pass
class TestOps(unittest.TestCase):
	def test_op01(self):
		test_data = "01,6,5,7,99,10,11,6"
		c = OPcodeComputer(input_path="01,6,5,7,99,10,11,6",parm=1)
		self.assertEqual(c.get_result_position(),7)
		c.process_instructions()
		self.assertEqual('21',c.instructions[7])
		c.instructions = test_data.split()

class TestPart1(unittest.TestCase):
	def setUp(self):
		self.c = OPcodeComputer(input_path="input5.txt",parm=1)
	def test_the_run(self):
		result = self.c.process_instructions()
		self.assertEqual(result,"16348437")
class TestPart2(unittest.TestCase):
	def test_position_equal_to(self):
		text = "3,9,8,9,10,9,4,9,99,-1,8"
		c = OPcodeComputer(input_path=text,parm=8)
		self.assertEqual(c.process_instructions(),'1')

		text = "3,9,8,9,10,9,4,9,99,-1,8"
		c = OPcodeComputer(input_path=text,parm=9)
		self.assertEqual(c.process_instructions(),'0')

		text = "3,9,8,9,10,9,4,9,99,-1,8"

		c = OPcodeComputer(input_path=text,parm=7)
		self.assertEqual(c.process_instructions(),'0')

	def test_immediate_equal_to(self):
		text = "3,3,1108,-1,8,3,4,3,99"
		c = OPcodeComputer(input_path=text,parm=8)
		self.assertEqual(c.process_instructions(),'1')

		text = "3,3,1108,-1,8,3,4,3,99"
		c = OPcodeComputer(input_path=text,parm=9)
		self.assertEqual(c.process_instructions(),'0')

		text = "3,3,1108,-1,8,3,4,3,99"
		c = OPcodeComputer(input_path=text,parm=7)
		self.assertEqual(c.process_instructions(),'0')
	def test_position_less_than(self):
		text = "3,9,7,9,10,9,4,9,99,-1,8"
		c = OPcodeComputer(input_path=text,parm=7,debug=False,op_debug=False,param_debug=False)
		self.assertEqual(c.process_instructions(),'1')
class TestDay7(unittest.TestCase):
	def test_part1(self):
		import itertools
		ampers = [0,1,2,3,4]
		test_input = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
		a = Amplifiers(test_input,[4,3,2,1,0])
		self.assertEqual(a.fire_amps(),"43210")

		max_result = 0
		max_amps = None
		for test in itertools.permutations(ampers):
			a = Amplifiers(test_input,test)
			result = int(a.fire_amps())
			if result > max_result:
				max_result = result
				max_amps = test
		self.assertEqual(max_result,43210)
		self.assertEqual(max_amps,(4,3,2,1,0))

		test_input = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
		a = Amplifiers(test_input,[0,1,2,3,4])
		self.assertEqual(a.fire_amps(),"54321")

		max_result = 0
		max_amps = None
		for test in itertools.permutations(ampers):
			a = Amplifiers(test_input,test)
			result = int(a.fire_amps())
			if result > max_result:
				max_result = result
				max_amps = test
		self.assertEqual(max_result,54321)
		self.assertEqual(max_amps,(0,1,2,3,4))

		test_input = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
		a = Amplifiers(test_input,[1,0,4,3,2])
		self.assertEqual(a.fire_amps(),"65210")

		max_result = 0
		max_amps = None
		for test in itertools.permutations(ampers):
			a = Amplifiers(test_input,test)
			result = int(a.fire_amps())
			if result > max_result:
				max_result = result
				max_amps = test
		self.assertEqual(max_result,65210)
		self.assertEqual(max_amps,(1,0,4,3,2))
	def test_part2(self):
		test_input = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
		a = Amplifiers(test_input,[9,8,7,6,5])
		self.assertEqual(a.fire_amps(),"139629729")
if __name__ == '__main__':
    unittest.main()