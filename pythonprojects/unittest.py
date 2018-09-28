import unittest
from homework import reverseList, isPalindrome, removeNegatives


class reverseListTest(unittest.TestCase):
    def test1(self):
        return self.assertEqual(reverseList([1,3,5]), [5,3,1])
    def test2(self):
        return self.assertEqual(reverseList(2,4,-3), [-3,4,2])

class isPalindromeTest(unittest.TestCase):
    def test1(self):
       return self.assertEqual(isPalindrome("racecar"), True)
    def test2(self):
       return self.assertEqual(isPalindrome("rabbit", False))

    def setUp(self):

    	print('running setup')

    def tearDown(self):

    	print('running teardown')


if __name__ == '__main__':
	unittest.main()