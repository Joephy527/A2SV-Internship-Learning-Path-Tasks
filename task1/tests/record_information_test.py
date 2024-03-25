"""Unittests for record_info(int, "...", "...", "...", "...", int)."""

import unittest

from record_information import record_info

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for record_info(int, "...", "...", "...", "...", int)."""
    
    def test_positive_transaction(self):
        """Test A Positive Transaction (income)."""
        
        latest_balance = 1000
        date = "2024-03-10"
        time = "09:30:46.67"
        transaction_type = "income"
        category = "freelance"
        amount = 2000
        
        expected_result = [date, time, transaction_type, category, amount, 3000]
        
        self.assertEqual(record_info(latest_balance, date, time, transaction_type, category, amount), expected_result)

    def test_negative_transaction(self):
        """Test A Negative Transaction (expense)."""
    
        latest_balance = 1200
        date = "2024-03-10"
        time = "14:45:27.46"
        transaction_type = "expense"
        category = "groceries"
        amount = -50
        
        expected_result = [date, time, transaction_type, category, amount, 1150]
        
        self.assertEqual(record_info(latest_balance, date, time, transaction_type, category, amount), expected_result)
        
    def test_return_non_empty_list(self):
        """Test For Empty List."""
        
        latest_balance = 1500
        date = "2024-03-10"
        time = "18:00:43.25"
        transaction_type = "income"
        category = "salary"
        amount = 12000
        
        self.assertIsNotNone(record_info(latest_balance, date, time, transaction_type, category, amount))
        
    def test_return_type(self):
        """Test The Return Type Is A List."""
        
        latest_balance = 1500
        date = "2024-03-10"
        time = "18:00:43.25"
        transaction_type = "income"
        category = "salary"
        amount = 12000
        
        self.assertIsInstance(record_info(latest_balance, date, time, transaction_type, category, amount), list)
        
    def test_lengths(self):
        """Test The Result Is Of Length 6."""
        
        latest_balance = 1500
        date = "2024-03-10"
        time = "18:00:43.25"
        transaction_type = "income"
        category = "salary"
        amount = 12000
        
        self.assertEqual(len(record_info(latest_balance, date, time, transaction_type, category, amount)), 6)

if __name__ == "__main__":
    unittest.main()