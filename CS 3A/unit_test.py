""" Allow the user to see the unit test for the Air Quality menu code.
"""

'''
Verify that 6147 lines of Purple Air data were loaded

Call the load_file method using the object
Reach in to a protected object to verify that the correct number of lines were loaded.
Your unit test must use the techniques in the Advanced Unit Testing module.
'''
import unittest
import final


class EmptyDatasetError(Exception):
    pass


class NoMatchingItemsError(Exception):
    pass


final.DataSet("test")

class TestCC(unittest.TestCase):

	def test_loading_csv_data(self):

		expected = 6147
		actual = len(test._data)
		self.assertEqual(actual, expected)

	def test_bad_object_instantiation(self):
		with self.assertRaises(ValueError):  # failing header = no object
			final.DataSet("extremelylongheaderinputthatisover30characterslong")

	def test_return_values(self):
		self.assertEqual(6147, )

if __name__ == "__main__":
	unittest.main()