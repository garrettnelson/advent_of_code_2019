from opcomputer import OPcodeComputer
import unittest
import sys
class TestModes(unittest.TestCase):
	def setUp(self):
		self.c = OPcodeComputer(input_path=None,parm=1,test_override=["1"])
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
		c = OPcodeComputer(input_path=None,parm=1,test_override=test_data.split(","))
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
		c = OPcodeComputer(input_path=None,parm=8,test_override=['3', '9', '8', '9', '10', '9', '4', '9', '99', '-1', '8'])
		self.assertEqual(c.process_instructions(),'1')

		c = OPcodeComputer(input_path=None,parm=9,test_override=['3', '9', '8', '9', '10', '9', '4', '9', '99', '-1', '8'])
		self.assertEqual(c.process_instructions(),'0')

		c = OPcodeComputer(input_path=None,parm=7,test_override=['3', '9', '8', '9', '10', '9', '4', '9', '99', '-1', '8'])
		self.assertEqual(c.process_instructions(),'0')

	def test_immediate_equal_to(self):
		c = OPcodeComputer(input_path=None,parm=8,test_override=['3', '3', '1108', '-1', '8', '3', '4', '3', '99'])
		self.assertEqual(c.process_instructions(),'1')

		c = OPcodeComputer(input_path=None,parm=9,test_override=['3', '3', '1108', '-1', '8', '3', '4', '3', '99'])
		self.assertEqual(c.process_instructions(),'0')

		c = OPcodeComputer(input_path=None,parm=7,test_override=['3', '3', '1108', '-1', '8', '3', '4', '3', '99'])
		self.assertEqual(c.process_instructions(),'0')
	def test_position_less_than(self):
		c = OPcodeComputer(input_path=None,parm=7,test_override=['3', '9', '7', '9', '10', '9', '4', '9', '99', '-1', '8'],debug=True,op_debug=True,param_debug=True)
		self.assertEqual(c.process_instructions(),'1')
if __name__ == '__main__':
    unittest.main()