"""Unittests for handle_transaction_type([...])."""

from io import StringIO
import unittest
from unittest.mock import patch

from transaction_type import handle_transaction_type

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for handle_transaction_type([...])."""
        
    @patch('builtins.input', side_effect=['income'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_of_valid_transaction(self, mock_stdout, mock_input):
        """Test Handle Of Valid Transaction"""
        
        transaction_types = ['income', 'expense']

        transaction_type = handle_transaction_type(transaction_types)

        expected_output = "Choose What Type Of Transaction You Want To Make\n"
        expected_output += "1: Income\n"
        expected_output += "2: Expense\n"
        
        self.assertEqual(transaction_type, 'income')
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['invalid', 'invalid', 'expense'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_handle_of_invalid_transaction(self, mock_stdout, mock_input):
        """Test Handle Of Invalid Transaction"""
        
        transaction_types = ['income', 'expense']

        transaction_type = handle_transaction_type(transaction_types)

        expected_output = "Choose What Type Of Transaction You Want To Make\n"
        expected_output += "1: Income\n"
        expected_output += "2: Expense\n"
        expected_output += "Invalid Transaction\n"
        expected_output += "Here Is A List Of Available Transactions\n"
        expected_output += "1: Income\n"
        expected_output += "2: Expense\n"
        expected_output += "Invalid Transaction\n"
        expected_output += "Here Is A List Of Available Transactions\n"
        expected_output += "1: Income\n"
        expected_output += "2: Expense\n"
        
        self.assertEqual(transaction_type, 'expense')
        self.assertIn(expected_output, mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()