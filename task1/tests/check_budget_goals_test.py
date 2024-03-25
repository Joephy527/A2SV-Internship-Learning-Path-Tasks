"""Unittests for analize_budget(int, int, '...')."""

import sys
import unittest
from io import StringIO

from check_budget_goals import analize_budget

class TestAnalizeBudget(unittest.TestCase):
    """Define Unittests for analize_budget(int, int, '...')."""
    
    def test_expense_over_budget(self):
        """Test For When Expense Is Over Budget."""
        
        captured_output = StringIO()
        sys.stdout = captured_output

        analize_budget(150, 200, "expense")
        printed_text = captured_output.getvalue().strip()
                
        sys.stdout = sys.__stdout__

        self.assertIn("You've Gone Over Budget By 50", printed_text)
                
    def test_expense_under_budget(self):
        """Test For When Expense Is Under Budget."""

        captured_output = StringIO()
        sys.stdout = captured_output

        analize_budget(200,150, "expense")
        printed_text = captured_output.getvalue().strip()
                
        sys.stdout = sys.__stdout__

        self.assertIn("Congratulations For Keeping Your Expense Under Budget", printed_text)
        self.assertIn("You Have A Remaining Balance Of 200", printed_text)
        
    def test_income_over_budget(self):
        """Test For When Income Isn't Enough."""
        
        captured_output = StringIO()
        sys.stdout = captured_output

        analize_budget(150, 200, "income")
        printed_text = captured_output.getvalue().strip()
                
        sys.stdout = sys.__stdout__

        self.assertEqual("You're Still Recovering From Your Last Expenses, Keep Saving", printed_text)
        
    def test_income_under_budget(self):
        """Test For When income Is Enough."""

        captured_output = StringIO()
        sys.stdout = captured_output

        analize_budget(200,150, "income")
        printed_text = captured_output.getvalue().strip()
                
        sys.stdout = sys.__stdout__

        self.assertIn("You Have A Remaining Balance Of 200", printed_text)
    
if __name__ == "__main__":
    unittest.main()