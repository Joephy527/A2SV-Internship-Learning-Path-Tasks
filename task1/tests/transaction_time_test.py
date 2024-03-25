"""Unittests for get_time_of_transaction()."""

import unittest
from datetime import datetime as dt

from transaction_time import get_time_of_transaction

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for get_time_of_transaction()."""
    
    def test_return_non_empty_list(self):
        """Test For Empty String"""
        
        date, time = get_time_of_transaction()
        
        self.assertIsNotNone(date)
        self.assertIsNotNone(time)
    
    def test_return_type(self):
        """Test The Return Type Is A String."""
        
        date, time = get_time_of_transaction()
        
        self.assertIsInstance(date, str)
        self.assertIsInstance(time, str)

    def test_get_time_of_transaction(self):
        mock_dt = str(dt.now())

        date, time = get_time_of_transaction()

        self.assertEqual(date, '2024-03-10')
        self.assertAlmostEqual(time, mock_dt[11:])

if __name__ == '__main__':
    unittest.main()