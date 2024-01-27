import unittest

def no_space(x):
    x = x.split(" ")
    return "".join(x)

class TestAddition(unittest.TestCase):
    def test_no_space(self):
        self.assertEqual(no_space("hallo apa k a bar"), "halloapakabar")
        self.assertEqual(no_space('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd'), '88Bifk8hB8BB8BBBB888chl8BhBfd')
        self.assertEqual(no_space('8aaaaa dddd r     '), '8aaaaaddddr')
        self.assertEqual(no_space('jfBm  gk lf8hg  88lbe8 '), 'jfBmgklf8hg88lbe8') 
        self.assertEqual(no_space('8j aam'), '8jaam')
if __name__ == "__main__":
    unittest.main()