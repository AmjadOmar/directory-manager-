import unittest
from unittest.mock import patch
from directories import Directory

class TestDirectory(unittest.TestCase):
    
    def setUp(self):
        self.dir_manager = Directory()

    def test_create(self):
        self.dir_manager.create("fruits")
        self.assertIn("fruits", self.dir_manager.directories)

    def test_move(self):
        self.dir_manager.create("grains/squash")
        self.dir_manager.move("grains/squash", "vegetables")
        self.assertNotIn("squash", self.dir_manager.directories["grains"])
        self.assertIn("squash", self.dir_manager.directories["vegetables"])

    def test_delete(self):
        self.dir_manager.create("fruits/apples")
        self.dir_manager.delete("fruits/apples")
        self.assertNotIn("apples", self.dir_manager.directories["fruits"])

    @patch('builtins.print')
    def test_list(self, mock_print):
        self.dir_manager.create("fruits/apples")
        self.dir_manager.create("grains")
        self.dir_manager.list_directories()

        # Expected output as a list of calls to print
        expected_calls = [
            unittest.mock.call('fruits'),
            unittest.mock.call('  apples'),
            unittest.mock.call('grains')
        ]

        # Check if the print calls match the expected output
        mock_print.assert_has_calls(expected_calls, any_order=False)

if __name__ == '__main__':
    unittest.main()
