"""Unittests for show_expenditure()."""

import unittest
from unittest.mock import patch

from show_budget_chart import show_expenditure

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for show_expenditure()."""

    @patch('matplotlib.pyplot.show')
    def test_show_expenditure(self, mock_show):
        """Test If Plot Is Shown"""
        
        show_expenditure()
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()