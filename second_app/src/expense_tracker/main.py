from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class Expense:
    """
    Represents a single expense entry
    """
    amount: float  # How much was spent
    category: "Category"  # type : ignore  # we'll define Category next
    description: str  # a short note on the expense


class Category(Enum):
    # Enum gives you Category.FOOD, Category.TRANSPORT, etc.,
    # instead of free-form strings—so you can’t mistype "Food" vs "food"
    FOOD = "food"
    TRANSPORT = "transport"
    UTILITIES = "utilities"
    OTHER = "other"

# keep imports at top: dataclass, Enum, List

# in-memory store


_expenses: List[Expense] = []
# A name starting with _ tells other developers (and tools) “this is for
#  internal use—don’t import or rely on it.
# Variable names beginning with _ are not imported


def add_expense(amount: float, category: Category, description: str) -> None:
    """
    Create a new Expense and add it to the in-memory List
    """
    _expenses.append(Expense(amount, category, description))


def list_expenses() -> List[Expense]:
    """
    Return all recorded expenses
    """
    return list(_expenses)
