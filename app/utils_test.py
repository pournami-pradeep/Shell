import unittest
from utility import echo_v2

class TestCommands(unittest.TestCase):
    def test_echo(self):
        cases = {
            "hello     world": "hello world",
            "\"hello   world\"": "hello   world",
            '"hello"  "shell\'s"  example""world':"hello shell's exampleworld",
            '"world"  "example\'s"  hello""script': "world example's helloscript"
        }

        for case in cases:
            self.assertEqual(echo_v2(case), cases[case])




if __name__ == '__main__':
    unittest.main()