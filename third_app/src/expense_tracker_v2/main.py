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
    if not isinstance((amount), (int, float)) or (amount < 0):
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
