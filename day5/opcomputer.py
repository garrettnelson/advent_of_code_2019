debug = False
op_debug = False
param_debug = False
op_codes = {
	'99':{'param':0,
			'position':0},
	'01':{'param': 2,
			'position':3},
	'02':{'param' : 2,
			'position':3},
	'03':{'param':0,
			'position': 1},
	'04':{'param': 0,
			'position':1},
	'05':{'param':2,
		'position':0},
	'06':{'param':2,
		'position':0},
	'07':{'param' : 2,
			'position':3},
	'08':{'param' : 2,
			'position':3},			
}
class OPcodeComputer(object):
	def __init__(self,input_path=None,parm=None,test_override=None,debug=False,op_debug=False,param_debug=False):
		self.last_output = None
		self.debug = debug
		self.op_debug = op_debug
		self.param_debug = param_debug
		self.parm = parm
		if test_override == None:
			f = open(input_path)
			self.instructions = f.read().split(",")
			f.close()
		else:
			self.instructions = test_override
		self.current_position = 0
	def process_instructions(self):
		self.process_instruction(self.current_position)
		return self.last_output
	def current_instruction(self):
		return self.instructions[self.current_position]
	def process_instruction(self,position):
		

		self.current_position = position
		if self.debug:
			print "Processing instruction %s opcode %s" % (position,self.get_op_code())
		result_position = self.get_result_position()
		params = self.get_params()
		if params == None:
			params = {}
		if not result_position == None:
			params['position'] = result_position
		if self.param_debug:
			print params
		#perform operation
		result = getattr(self, "op_%s" % self.get_op_code())(**params)
		if result != None:
			if result == -1:
				self.process_instruction(self.get_next_op_position())
			else:
				self.process_instruction(result)
	def op_99(self):
		return None
	def op_01(self,position,param1,param2):
		if self.op_debug == True:
			print "param1:%s param2:%s" % (param1,param2)
		if self.debug == True:
			print "Setting Position %s to %s + %s" % (position,param1,param2)
		self.instructions[position] = "%s" % (param1 + param2)
		return -1
	def op_02(self,position,param1,param2):
		if self.debug == True:
			print "Setting Position %s to %s * %s" % (position,param1,param2)
		self.instructions[position] = "%s" % (param1 * param2)
		return -1
	def op_03(self,position):
		if self.debug == True:
			print "Setting Position %s to %s" % (self.get_result_position(),self.parm)
		self.instructions[self.get_result_position()] = "%s" % (self.parm)
		return -1
	def op_04(self,position):
		if self.debug == True:
			print "Returning position %s" % position
		print self.instructions[position]
		self.last_output = self.instructions[position]
		return -1
	def op_05(self,param1,param2):
		if self.debug == True:
			print "Checking whether %s is not equal to 0 and setting result to position %s" % (param1,param2)
		if param1 != 0:
			return param2
		else:
			return -1
	def op_06(self,param1,param2):
		if self.debug == True:
			print "Checking whether %s is equal to 0 and setting result to position %s" % (param1,param2)
		if param1 == 0:
			return param2
		else:
			return -1
	def op_07(self,param1,param2,position):
		if self.debug == True:
			print "Checking whether %s < %s and setting result to %s" % (param1,param2,position)
		if param1 < param2:
			self.instructions[position] = "1"
		else:
			self.instructions[position] = "0"
		return -1
	def op_08(self,param1,param2,position):
		if self.debug == True:
			print "Checking whether %s == %s and setting result to %s" % (param1,param2,position)
		if param1 == param2:
			self.instructions[position] = "1"
		else:
			self.instructions[position] = "0"
		return -1
	def get_params(self):
		modes = self.get_param_modes()
		params = {}
		for i in range(self.get_current_num_params()):
			param_name = "param%s" % (i+1)
			param_mode = modes[param_name]
			parameter_position = self.current_position+i+1
			if self.param_debug == True:
				print "Extracting parameter: %s from position %s in mode %s" % (param_name,parameter_position,param_mode)
				print self.instructions
			parameter = int(self.instructions[parameter_position])
			if param_mode == 0:
				number = int(self.instructions[parameter])
			else:
				number = parameter
			params[param_name] = number
		return params
	def get_param_modes(self):
		#set default modes
		modes = {'param1':0,
				'param2':0,
				'param3':0}
		if not self.get_mode_string():
			return modes
		for i in range(len(self.get_mode_string())):
			param_string = 'param%s' % (i+1)
			length = len(self.get_mode_string())
			modes[param_string] = int(self.get_mode_string()[length-i-1:length-i])
		return modes
	def get_op_code(self):
		instruction_length = len(self.current_instruction())
		if instruction_length== 1:
			op_code =  "0"+self.current_instruction()
		else:
			op_code = self.current_instruction()[instruction_length-2:instruction_length]
		if not op_code in op_codes:
			raise Exception("invalid code %s at position %s" % (op_code,self.current_position))
		return op_code
	def get_mode_string(self):
		instruction_length = len(self.current_instruction())
		if instruction_length == 1:
			return None
		else:
			return self.current_instruction()[0:instruction_length-2]
	def get_result_position(self):
		position_index = op_codes[self.get_op_code()]['position']
		if position_index == 0:
			return None
		else:
			return int(self.instructions[int(position_index) + self.current_position])
	def get_next_op_position(self):
		op_code_setup = op_codes[self.get_op_code()]
		return max(op_code_setup['position'],op_code_setup['param']) + 1 +self.current_position
	def get_current_num_params(self):
		return op_codes[self.get_op_code()]['param']