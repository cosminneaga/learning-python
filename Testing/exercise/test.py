import unittest
import index


class Test(unittest.TestCase):

    def test_input(self):
        ans = 5
        gus = 5
        res = index.run_guess(gus, ans)
        self.assertTrue(res)

    def test_input_wrong_answer(self):
        res = index.run_guess(5, 0)
        self.assertFalse(res)

    def test_input_between_1_10(self):
        res = index.run_guess(5, 11)
        self.assertFalse(res)

    def test_input_as_string(self):
        res = index.run_guess(5, '11')
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
