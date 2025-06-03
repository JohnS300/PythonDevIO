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

@pytest.mark.parametrize('expense_list, filter_category, expected_count',
                         [(
                            [
                                # First scenario: “two groceries, one rent”
                                (5.0, date(2025, 5, 1), Category.GROCERIES, "apples"),
                                (10.0, date(2025, 5, 1), Category.GROCERIES, "bread"),
                                (100.0, date(2025, 5, 1), Category.RENT, "May rent"),
                            ],
                            Category.GROCERIES,
                            2,
                          ),
                          (
                            [
                                # Second scenario: “same three expenses, but filter rent”
                                (5.0, date(2025, 5, 2), Category.GROCERIES, "apples"),
                                (10.0, date(2025, 5, 2), Category.GROCERIES, "bread"),
                                (100.0, date(2025, 5, 2), Category.RENT, "May rent"),
                            ],
                            Category.RENT,
                            1,
                          ),
                          (
                            [
                                # Second scenario: “same three expenses, but filter rent”
                                (5.0, date(2025, 5, 3), Category.GROCERIES, "apples"),
                                (10.0, date(2025, 5, 3), Category.GROCERIES, "bread"),
                                (100.0, date(2025, 5, 3), Category.RENT, "May rent"),
                            ],
                            Category.HOBBY,
                            0,
                          )], ids=['first_test', 'second_test', 'third_test'])
def test_filter_by_valid_category(expense_list, filter_category, expected_count):
    for vamount, vdate, vcategory, vdescription in expense_list:
        add_expenses(vamount, vdate, vcategory, vdescription)

    result = filter_by_category(filter_category)

    assert isinstance(result, list)
    assert len(result) == expected_count

    for exp in result:
        assert exp.category == filter_category


@pytest.mark.parametrize("category_filter", ['', 'negative', 123, None], ids=['empty_str', 'invalid_str', 'int', 'None'])
def test_filter_by_invalid_category(category_filter):
    with pytest.raises(TypeError):
        filter_by_category(category_filter)


# Testing Clear function
def invalid_clear_expenses():
    _expenses.clear()
    # somehow test what we get when calling the clear function