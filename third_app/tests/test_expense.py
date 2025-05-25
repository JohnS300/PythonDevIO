import pytest

from src.expense_tracker_v2.main import add_expenses, Category, _expenses
from datetime import date


# Pytest will look for a function named setup_function and run it before every test in that module.
def setup_function():
    _expenses.clear


# The function name starts with test_ so pytest discovers it.
def test_add_valid_expense():
    add_expenses(80, date(2025, 5, 25), Category.GIRLFRIEND, 'French Restaurant dinner ')
    assert len(_expenses) == 1
    first_expense = _expenses[0]
    assert first_expense.amount == 80
    assert first_expense.date_of_expense == date(2025, 5, 25)
    assert first_expense.category == Category.GIRLFRIEND
    assert first_expense.description == 'French Restaurant dinner'


def test_invalid_category_raises():
    add_expenses(10, date(2024, 4, 24), Category.Souvlaki, 'Souvlaki apo lemona')


@pytest.mark.parametrize("bad_amount", [0, -5, five, None], ids=["zero", "negative", "non-numeric string", "None"])
def test_invalid_amount_raises():
    with pytest.raises(ValueError):
        add_expenses(bad_amount, date.today(), Category.ENTERTAINMENT, 'Cinema tickets')


