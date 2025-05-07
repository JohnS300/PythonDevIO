import pytest
from expense_tracker.main import add_expense, list_expenses, Category, Expense  # type : ignore


def setup_function():
    """
    Clear our in-memory list before each test
    """
    list_expenses().clear()


def test_add_and_list_single():
    add_expense(12.5, Category.FOOD, "lunch")
    expenses = list_expenses()
    assert len(expenses) == 1
    exp = expenses[0]
    # Check it's an expense and has correct fields
    assert isinstance(exp, Expense)
    assert exp.amount == 12.5
    assert exp.category == Category.FOOD
    assert exp.description == 'lunch'


def test_invalid_category_raises():
    with pytest.raises(ValueError):
        """
        Check that ValueError is thrown when someone passes a bad
          category string
        """
        add_expense(123.0, "not-a-category", "mistake")
