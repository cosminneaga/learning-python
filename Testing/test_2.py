import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        '''
        HIIIII!!!!
        '''
        param = 10
        result = main.do_stuff(param)
        self.assertEqual(result, 15)
        # self.assertEqual(result, 14)

    def test_do_stuff2(self):
        param = 'djkashdjas'
        result = main.do_stuff(param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        param = None
        result = main.do_stuff(param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        param = ''
        result = main.do_stuff(param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
