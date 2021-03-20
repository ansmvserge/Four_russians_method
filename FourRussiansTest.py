import main
import unittest
import numpy as np


class TestFourRussians(unittest.TestCase):

    def test_simple(self):
        left_matrix = np.random.randint(2, size=(2,2))
        right_matrix = np.random.randint(2, size=(2,2))
        res1 = np.dot(left_matrix.astype(bool), right_matrix.astype(bool))
        res1 = res1.astype(int)
        res2 = main.four_russians_method(left_matrix, right_matrix)
        res2 = res2.astype(int)
        np.testing.assert_array_equal(res1, res2)

    def test_medium(self):
        left_matrix = np.random.randint(2, size=(5,5))
        right_matrix = np.random.randint(2, size=(5,5))
        res1 = np.dot(left_matrix.astype(bool), right_matrix.astype(bool))
        res1 = res1.astype(int)
        res2 = main.four_russians_method(left_matrix, right_matrix)
        res2 = res2.astype(int)
        np.testing.assert_array_equal(res1, res2)

    def test_complex(self):
        left_matrix = np.random.randint(2, size=(25,25))
        right_matrix = np.random.randint(2, size=(25,25))
        res1 = np.dot(left_matrix.astype(bool), right_matrix.astype(bool))
        res1 = res1.astype(int)
        res2 = main.four_russians_method(left_matrix, right_matrix)
        res2 = res2.astype(int)
        np.testing.assert_array_equal(res1, res2)

if __name__ == '__main__':
    unittest.main()
