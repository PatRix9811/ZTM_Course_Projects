import unittest
import do_testow


class TestMain(unittest.TestCase):
	def test1(self):
		num = 0
		result  = do_testow.suma(num)
		self.assertEqual(result,5)

	def test2(self):
		num = 'dt'
		result = do_testow.suma(num)
		self.assertIsInstance(result,ValueError)

	def test3(self):
		num = None
		result = do_testow.suma(num)
		self.assertEqual(result,'pleas enter number')


if __name__ == '__main__':
	unittest.main()