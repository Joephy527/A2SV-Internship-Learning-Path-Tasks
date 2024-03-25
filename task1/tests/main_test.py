"""Unittests for main()."""

import unittest
from unittest.mock import patch

from main import main

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for main()."""
    
    @patch('builtins.print')
    @patch('main.get_time_of_transaction', return_value=("2024-03-10", "18:00:43.25"))
    @patch('main.get_current_balance', return_value=1200)
    @patch('main.handle_transaction_type', return_value="expense")
    @patch('main.process_transaction', return_value=("Groceries", -50))
    @patch('main.record_info')  
    @patch('main.write_info')
    @patch('main.analize_budget')
    @patch('main.show_expenditure')
    def test_expense_main(self, mock_get_time_of_transaction, mock_get_current_balance, mock_handle_transaction_type, mock_process_transaction, mock_record_info, mock_write_info, mock_analize_budget, mock_show_expenditure, mock_print):
        """Test That Imported Functions Were Called"""
        
        main()

        mock_get_time_of_transaction.assert_called_once()
        mock_get_current_balance.assert_called_once()
        mock_handle_transaction_type.assert_called_once()
        mock_process_transaction.assert_called_once()
        mock_record_info.assert_called_once()
        mock_write_info.assert_called_once()
        mock_analize_budget.assert_called_once()
        mock_show_expenditure.assert_called_once()

if __name__ == '__main__':
    unittest.main()