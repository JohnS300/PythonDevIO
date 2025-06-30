import os
from enum import Enum
from dataclasses import dataclass
from datetime import date


_expenses = []
# module-level list to hold all Expense objects


_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
# Abs path to the folder containing *this* file


_PROJECT_ROOT = os.path.abspath(os.path.join(_THIS_DIR, os.pardir, os.pardir))
# Repo root


DATA_DIR = os.path.join(_PROJECT_ROOT, 'data')
DATA_FILE = os.path.join(DATA_DIR, 'expenses.json')
ARCHIVE_FMT = "expense-{:%Y-%m-%d}_backup.json"


class Category(Enum):
    """Fixed set of categories for every expense."""
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
    """
    Immutable record of a single out-going amount.

    Attributes
    ----------
    amount : float
        Positive monetary value.
    date_of_expense : datetime.date
        Calendar day the expense occurred.
    category : Category
        One of the predefined Category enum members.
    description : str
        Short, free-form explanation (no leading/trailing spaces).
    """
    amount: float
    date_of_expense: date
    category: Category
    description: str

    def __repr__(self) -> str:
        # Override the auto-repr for a cleaner, one-liner
        return (
            f"<Expense {self.amount:.2f} "
            f"{self.category.name} "
            f"{self.date_of_expense.isoformat()} "
            f"'{self.description}'>"
        )


def add_expense(amount, date_of_expense, category, description):
    """
    Record one new expense after validating all inputs.

    Raises
    ------
    ValueError
        If amount ≤ 0 or description is blank.
    TypeError
        If date_of_expense is not datetime.date or category is not Category.
    """
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


def list_expenses() -> list:
    """Return **a shallow copy** of all currently stored expenses."""
    return list(_expenses)
    # return a shallow copy of the list so caller can’t mutate it


def total_expenses() -> float:
    """Return the sum of every stored expense amount."""
    total = 0.0
    for i in _expenses:
        total = total + i.amount
    return total


def filter_by_category(category) -> list:
    """Return only expenses whose '.category' matches *category*."""
    if not isinstance(category, Category):
        raise TypeError(f"category must be Category, got {type(category).__name__}")
    _filtered_expenses = []
    for i in _expenses:
        if i.category == category:
            _filtered_expenses.append(i)
    return _filtered_expenses


def remove_expense(index):
    """
    Delete the expense at *index* from the internal list.

    Raises
    ------
    IndexError
        If index is out of range **or** list is empty.
    """
    _expenses.pop(index)


def clear_expenses():
    """Remove every stored expense (idempotent)."""
    _expenses.clear()


def filter_by_date(start: date, end: date) -> list:
    """
    Return expenses whose date_of_expense is between start and end (inclusive).
    """
    if start > end:
        raise ValueError("Start date must be before or on the end date")
    _filtered_expenses = []
    for i in _expenses:
        if i.date_of_expense >= start and i.date_of_expense <= end:
            _filtered_expenses.append(i)
    return _filtered_expenses


def to_csv() -> str:
    """
    Return all expenses as a CSV string with header line.
    Columns: amount,date,category,description
    """
    _expenses_csv = ["amount,date,category,description"]
    for i in _expenses:
        newLine = f"{i.amount},{i.date_of_expense},{i.category},'{i.description}'"
        _expenses_csv.append(newLine)
    return "\n".join(_expenses_csv)
