import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

from UVSimulator import UVSimulator

class TestUVSimulator(unittest.TestCase):
  def setUp(self):
    self.uvsim = UVSimulator()

  def test_load_program_from_file(self):
    filename = "Test1.txt"
    program+content = "1010\n2009\n4300"
    with open(filename, "w") as file:
      file.write(program_content)
    self.uvsim.load_program_from_file(filename):
    self.assertEqual(self.uvsim.memory[:3], [10, 9, 43])
    os.remove(filename)

  @patch('builtins.input, side_effect=[5])
  def test_execute_program_write(self, mock_stdout):
    
