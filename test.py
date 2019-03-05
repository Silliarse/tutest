import unittest

from main import add

assert add(1,2) == 3
assert add(1, -1) == 0

class TestFonctionAdd(unittest.TestCase):
	def test_add_OK(self):
		element = add(1,2)
		self.assertEqual(element, 3)
	
	def test_add_str(self):
		element = add("a",2)
		self.assertEqual(element, "error")
		
	def test_add_float(self):
		element = add(20.3, 3)
		self.assertEqual(element, 23.3)
	
	def test_add_long(self):
		element = add(1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000, 4)
		self.assertEqual(element, 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004)
		
if __name__ == '__main__':
	unittest.main()