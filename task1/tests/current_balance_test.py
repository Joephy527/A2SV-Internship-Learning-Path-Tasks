"""Unittests for get_current_balance()."""

import unittest
import csv
from unittest.mock import patch
from io import StringIO

from current_balance import get_current_balance

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for get_current_balance()."""
    
    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_get_current_balance_no_data(self, mock_csvreader, mock_open):
        "Test For When There Is No Data Saved."

        mock_csvreader.return_value = []
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(get_current_balance(),0)
            self.assertIn("Enter Income or Expenses and Start Tracking Your Budget", fake_out.getvalue().strip())

    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_get_current_balance_with_data(self, mock_csvreader, mock_open):
        "Test For When There Is Data Saved Previously."
        
        mock_csvreader.return_value = [{"balance": "1000"}]
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(get_current_balance(), 1000)
            self.assertIn("Your Current Balance is: 1000", fake_out.getvalue().strip())
    
    @patch('builtins.open')
    @patch('csv.DictReader')
    def test_get_current_balance_with_multiple_data(self, mock_csvreader, mock_open):
        "Test For When There Is Multiple Data Saved Previously."
        
        mock_csvreader.return_value = [{"balance": "1000"}, {"balance": "4000"}, {"balance": "3000"}, {"balance": "2000"}]
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(get_current_balance(), 2000)
            self.assertIn("Your Current Balance is: 2000", fake_out.getvalue().strip())
    
if __name__ == "__main__":
    unittest.main()