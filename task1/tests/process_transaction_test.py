"""Unittests for process_transaction("...")."""

import unittest
from unittest.mock import patch
from io import StringIO

from process_transaction import process_transaction

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for process_transaction("...")."""
    
    @patch('builtins.input', side_effect=["Salary", "2000"])
    def test_income_transaction(self, mock_input):
        """Test Income Transaction."""
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(process_transaction("income"), ("salary", 2000))
            self.assertIn("Please State Your Source Of Income", fake_out.getvalue().strip())
            self.assertIn("Enter Income Amount in ETB e.g(1000)", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=["Groceries", "500"])
    def test_expense_transaction(self, mock_input):
        """Test Expense Transaction."""
        
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertEqual(process_transaction("expense"), ("groceries", -500))
            self.assertIn("Please State Where Your Expenditure Went", fake_out.getvalue().strip())
            self.assertIn("Enter Income Amount in ETB e.g(1000)", fake_out.getvalue().strip())

if __name__ == '__main__':
 unittest.main()