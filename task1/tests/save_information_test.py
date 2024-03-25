"""Unittests for write_info([...])."""

import unittest
from unittest.mock import patch

from save_information import write_info

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for write_info([...])."""
    
    @patch('builtins.open', create=True)
    def test_write_info(self, mock_open):
        """Test Information Being Saved"""

        budget_tracker = ['2024-03-10', '09:30:43.3432', 'income', 'salary', 12000, 13000]

        write_info(budget_tracker)

        mock_open.assert_called_once_with('budget.csv', 'a', newline='')
        
if __name__ == '__main__':
    unittest.main()