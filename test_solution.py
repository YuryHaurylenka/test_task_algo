import unittest
from solution import can_jump

class TestCanJump(unittest.TestCase):
    def test_example_true(self):
        self.assertTrue(can_jump([2, 3, 1, 1, 4]))

    def test_example_false(self):
        self.assertFalse(can_jump([3, 2, 1, 0, 4]))

    def test_single_element(self):
        self.assertTrue(can_jump([0]))

    def test_all_zeroes(self):
        self.assertFalse(can_jump([0, 0, 0]))

    def test_large_jump(self):
        self.assertTrue(can_jump([4, 0, 0, 0, 0]))

    def test_unreachable_case(self):
        self.assertFalse(can_jump([1, 0, 1, 0]))

if __name__ == "__main__":
    unittest.main()
