from retrieval.stack import Stack
import unittest


class TestStack(unittest.TestCase):

    def setUp(self):
       self.my_stack = Stack()

    def test_checkStackIsEmptyAtInit(self):
        self.assertEqual(self.my_stack.size(),0)

    def test_checkPushOneItem(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.assertEqual(self.my_stack.size(),2)
        self.assertEqual(self.my_stack.peek(),2)

    def test_checkRemoveOnteItem(self):
        self.my_stack.push(1)
        self.my_stack.push(2)
        self.assertEqual(self.my_stack.pop(),2)
        self.assertEqual(self.my_stack.size(),1)
        self.assertEqual(self.my_stack.peek(),1)
        self.assertEqual(self.my_stack.pop(),1)
        self.assertRaises(IndexError,self.my_stack.peek)
            
if __name__ == '__main__':
    unittest.main()   
    

