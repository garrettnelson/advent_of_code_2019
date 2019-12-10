from opcomputer import OPcodeComputer
import unittest
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

if __name__ == '__main__':
    unittest.main()