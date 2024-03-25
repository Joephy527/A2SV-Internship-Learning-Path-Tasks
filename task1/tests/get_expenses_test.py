"""Unittests for get_all_expenses()."""

import unittest

from get_expenses import get_all_expenses

class TestGetAllExpenses(unittest.TestCase):
    """Define Unittests for get_all_expenses()."""
    
    def test_return_non_empty_list(self):
        """Test For Empty List"""
        
        expenses, expense_amount = get_all_expenses()
        
        self.assertIsNotNone(expenses)
        self.assertIsNotNone(expense_amount)
        
    def test_return_type(self):
        """Test The Return Type Is A List."""
        
        expenses, expense_amount = get_all_expenses()
        
        self.assertIsInstance(expenses, list)
        self.assertIsInstance(expense_amount, list)
        
    def test_lengths(self):
        """Test The Two Results Have Equal Length."""
        
        expenses, expense_amount = get_all_expenses()
        
        self.assertEqual(len(expenses), len(expense_amount))
        
if __name__ == "__main__":
    unittest.main()