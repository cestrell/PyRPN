import unittest
import rpn
import rpn_instr

class TestBasics(unittest.TestCase):
	def test_add(self):
		result1 = rpn.calculate("1 1 +")
		result2 = rpn_instr.calculate("1 1 +")
		self.assertEqual(2, result1)
		self.assertEqual(2, result2)

	def test_sub(self):
		result1 = rpn.calculate("4 3 -")
		result2 = rpn_instr.calculate("4 3 -")
		self.assertEqual(1, result1)
		self.assertEqual(1, result2)

	def test_div(self):
		result1 = rpn.calculate("4 2 /")
		result2 = rpn_instr.calculate("4 2 /")
		self.assertEqual(2, result1)
		self.assertEqual(2, result2)
	
	def test_mul(self):
		result1 = rpn.calculate("3 4 *")
		result2 = rpn_instr.calculate("3 4 *")
		self.assertEqual(12, result1)
		self.assertEqual(12, result2)

	def test_exp(self):
		result1 = rpn.calculate("2 3 ^")
		result2 = rpn_instr.calculate("2 3 ^")
		self.assertEqual(8, result1)
		self.assertEqual(8, result2)
