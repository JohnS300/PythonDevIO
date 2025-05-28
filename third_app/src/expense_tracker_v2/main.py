from enum import Enum
from dataclasses import dataclass
from datetime import date


_expenses = []
# module-level list to hold all Expense objects


class Category(Enum):
    INVESTMENT = 'investment'
    HOBBY = 'hobby'
    GIRLFRIEND = 'girlfriend'
    RENT = 'rent'
    GROCERIES = 'groceries'
    ELECTRICITY = 'electricity'
    PHONE = 'phone'
    ENTERTAINMENT = 'entertainment'


@dataclass
class Expense:
    amount: float
    date_of_expense: date
    category: Category
    description: str


def add_expenses(amount, date_of_expense, category, description):
    if not isinstance((amount), (int, float)) or (amount <= 0):
        raise ValueError(f"Amount must be positive number, got {amount!r}")
    if not (isinstance(date_of_expense, date)):
        raise TypeError(f"date_of_expense must be datetime.date, got {type(date_of_expense).__name__}")
    if not (isinstance(category, Category)):
        raise TypeError(f"category must be Category, got {type(category).__name__}")
    if not isinstance(description, str) or not description.strip():
        raise ValueError("description must be a non-empty string")
    expense = Expense(amount, date_of_expense, category, description.strip())
    _expenses.append(expense)


def list_expenses():
    return list(_expenses)
    # return a shallow copy of the list so caller can’t mutate it


def total_expenses():
    sum = 0.0
    if _expenses:
        for i in _expenses:
            sum = sum + i.amount
    else:
        print("No expenses registered yet.")
    return sum


def filter_by_category(category):
    if not isinstance(category, Category):
        raise TypeError(f"category must be Category, got {type(category).__name__}")
    _filtered_expenses = []
    for i in _expenses:
        if i.category == category:
            _filtered_expenses.append(i)
    return _filtered_expenses


def remove_expense(index):
    _expenses.pop(index)


def clear_expenses():
    _expenses.clear()
