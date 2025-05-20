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
    expense = Expense(amount, date_of_expense, category, description)
    _expenses.append(expense)


def list_expenses():
    return list(_expenses)
    # return a shallow copy of the list so caller can’t mutate it
