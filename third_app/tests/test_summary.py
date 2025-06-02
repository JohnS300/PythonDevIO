import pytest
from datetime import date
from expense_tracker_v2.main import total_expenses, filter_by_category, remove_expense, clear_expenses, _expenses, add_expenses, Category


@pytest.fixture(autouse=True)
def setup_function():
    clear_expenses()  # or _expenses.clear()
    yield  # teardown = clean and reset the resources and configurations created using Setup
    clear_expenses()  # or _expenses.clear()


def test_get_valid_total_expenses():
    add_expenses(10, date(2025, 5, 25), Category.GIRLFRIEND, 'Coffe')
    add_expenses(20.5, date(2025, 5, 25), Category.GIRLFRIEND, 'Brunch')
    add_expenses(5, date(2025, 5, 25), Category.GIRLFRIEND, 'Kiosk')
    assert len(_expenses) == 3
    assert total_expenses() == 35.5


# Testing Category filter

@pytest.mark.parametrize('first_test,second_test,third_test',
                         [(
                            [
                                (5.0, Category.GROCERIES, "apples"),
                                (10.0, Category.GROCERIES, "bread"),
                                (100.0, Category.RENT, "May rent"),
                            ],
                          ),
                          (
                              
                          ),
                          (
                              
                          )])

@pytest.mark.parametrize("category_filter", ['', 'negative', 123, None], ids=['empty_str', 'invalid_str', 'int', 'None'])
def test_filter_by_category(category_filter):
    with pytest.raises(TypeError):
        filter_by_category(category_filter)


# Testing Clear function
def invalid_clear_expenses():
    _expenses.clear()
    # somehow test what we get when calling the clear function