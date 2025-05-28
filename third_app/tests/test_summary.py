import pytest

from expense_tracker_v2.main import total_expenses, filter_by_category, remove_expense, clear_expenses, _expenses


def setup_function():
    _expenses.clear()


def test_invalid_total_expenses_call():
    


@pytest.mark.parametrize("bad_category_filter", ['', ' ', 'Tomato', 'None'], ids=['empty', 'spaces', 'string', None])
def test_filter_by_category(bad_category_filter):
    with pytest.raises(TypeError):
        filter_by_category(bad_category_filter)
