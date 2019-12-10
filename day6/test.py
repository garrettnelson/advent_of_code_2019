import unittest
from orbitalobject import ObjectMap
class Test1(unittest.TestCase):
	def test_case_1(self):
		o = ObjectMap("test1.txt")
		#print o.orbit_directory
		self.assertEqual(42,o.calculate_check_sum())
	def test_case_2(self):
		o = ObjectMap("test2.txt",debug=True)
		self.assertEqual(4,o.distance_from_you_to_san())

if __name__ == '__main__':
    unittest.main()