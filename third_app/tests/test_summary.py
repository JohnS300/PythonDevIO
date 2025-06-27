import pytest
from datetime import date
from expense_tracker_v2.main import (total_expenses, filter_by_category,
                                     remove_expense, clear_expenses,
                                     _expenses, add_expense, Category,
                                     list_expenses, filter_by_date, to_csv)


@pytest.fixture(autouse=True)
def setup_function():
    clear_expenses()  # or _expenses.clear()
    yield  # teardown = clean and reset the resources and configurations created using Setup
    clear_expenses()  # or _expenses.clear()


def test_get_valid_total_expenses():
    add_expense(10, date(2025, 5, 25), Category.GIRLFRIEND, 'Coffe')
    add_expense(20.5, date(2025, 5, 25), Category.GIRLFRIEND, 'Brunch')
    add_expense(5, date(2025, 5, 25), Category.GIRLFRIEND, 'Kiosk')
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
        add_expense(vamount, vdate, vcategory, vdescription)

    result = filter_by_category(filter_category)

    assert isinstance(result, list)
    assert len(result) == expected_count

    for exp in result:
        assert exp.category == filter_category


@pytest.mark.parametrize("category_filter", ['', 'negative', 123, None], ids=['empty_str', 'invalid_str', 'int', 'None'])
def test_filter_by_invalid_category(category_filter):
    with pytest.raises(TypeError):
        filter_by_category(category_filter)


# Testing remove function
@pytest.mark.parametrize('valid_test_data', [[
    (5.0, date(2025, 6, 4), Category.HOBBY, 'Gym expenses'),
    (4.5, date(2025, 6, 4), Category.GROCERIES, 'Food'),
    (10.0, date(2025, 6, 4), Category.ENTERTAINMENT, 'Movie tickets')
    ]], ids=['first_test'])
def test_remove_expense(valid_test_data):
    for vamount, vdate, vcategory, vdescription in valid_test_data:
        add_expense(vamount, vdate, vcategory, vdescription)
    assert len(_expenses) == 3
    original_expense_list = list(_expenses)
    remove_expense(1)

    assert len(_expenses) == 2

    assert _expenses[0] == original_expense_list[0]
    assert _expenses[1] == original_expense_list[2]
    with pytest.raises(IndexError):
        remove_expense(5)


# Testing Clear function
@pytest.mark.parametrize('valid_test_data', [
    [
        (5.0, date(2025, 6, 4), Category.HOBBY, 'Gym expenses'),
        (4.5, date(2025, 6, 4), Category.GROCERIES, 'Food')
    ]
    ], ids=['two_exp'])
def test_clear_expenses(valid_test_data):
    for vamount, vdate, vcategory, vdescription in valid_test_data:
        add_expense(vamount, vdate, vcategory, vdescription)
    assert len(_expenses) == 2

    clear_expenses()

    assert len(_expenses) == 0
    assert list_expenses() == []
    assert total_expenses() == 0.0
    clear_expenses()
    assert len(_expenses) == 0


@pytest.mark.parametrize('three_expenses', [
    [
        (5.0, date(2025, 6, 4), Category.HOBBY, 'Gym expenses'),
        (4.5, date(2025, 6, 20), Category.GROCERIES, 'Food'),
        (10.0, date(2025, 6, 28), Category.ENTERTAINMENT, 'Movie tickets')
    ]
], ids=['filter_by_date'])
def test_filter_by_date(three_expenses):
    for vamount, vdate, vcategory, vdescription in three_expenses:
        add_expense(vamount, vdate, vcategory, vdescription)
    assert len(_expenses) == 3
    result = filter_by_date(date(2025, 6, 4), date(2025, 6, 20))
    assert isinstance(result, list)
    assert len(result) == 2

    with pytest.raises(ValueError):
        filter_by_date(date(2025, 6, 21), date(2025, 6, 20))


@pytest.mark.parametrize('three_expenses', [
    [
        (5.0, date(2025, 6, 4), Category.HOBBY, 'Gym expenses'),
        (4.5, date(2025, 6, 20), Category.GROCERIES, 'Food'),
        (10.0, date(2025, 6, 28), Category.ENTERTAINMENT, 'Movie tickets')
    ]
], ids=['to_csv'])
def test_to_csv(three_expenses):
    for vamount, vdate, vcategory, vdescription in three_expenses:
        add_expense(vamount, vdate, vcategory, vdescription)
    assert len(_expenses) == 3

    csv_output = to_csv().splitlines()

    assert csv_output[0] == "amount,date,category,description"
    assert len(csv_output) == 4

    # content check: at least one line contains the word “Movie”
    assert any('Movie' in line for line in csv_output[1:])
