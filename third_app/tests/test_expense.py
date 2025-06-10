import pytest

from expense_tracker_v2.main import add_expense, Category, _expenses
from datetime import date


# Pytest will look for a function named setup_function and run it before every test in that module.
def setup_function():
    _expenses.clear()


# The function name starts with test_ so pytest discovers it.
def test_add_valid_expense():
    add_expense(80, date(2025, 5, 25), Category.GIRLFRIEND, 'French Restaurant dinner ')
    assert len(_expenses) == 1
    first_expense = _expenses[0]
    assert first_expense.amount == 80
    assert first_expense.date_of_expense == date(2025, 5, 25)
    assert first_expense.category == Category.GIRLFRIEND
    assert first_expense.description == 'French Restaurant dinner'


def test_invalid_category_raises():
    with pytest.raises(TypeError):
        add_expense(10, date(2024, 4, 24), "Souvlaki", 'Souvlaki apo lemona')


@pytest.mark.parametrize("bad_amount", [0, -5, 'five', None], ids=["zero", "negative", "non-numeric string", "None"])
def test_invalid_amount_raises(bad_amount):
    with pytest.raises(ValueError):
        add_expense(bad_amount, date.today(), Category.ENTERTAINMENT, 'Cinema tickets')


@pytest.mark.parametrize("bad_date", ["2025-05-12", 1234, None], ids=["string date", "int", "None"])
def test_invalid_date_raises(bad_date):
    with pytest.raises(TypeError):
        add_expense(20, bad_date, Category.HOBBY, "Testing dates")


@pytest.mark.parametrize("bad_description", ['', '  ', None], ids=['empty', 'spaces', 'None'])
def test_invalid_description_raises(bad_description):
    with pytest.raises(ValueError):
        add_expense(200.00, date(2022, 5, 5), Category.RENT, bad_description)
