import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate random id, this function is provided by subject"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


"""
About data class:
1. Auto generate boilerplate code: __init__, __repr__, __str__, etc.
2. Need to provide type annotation while specify class attributes
3. field() - a factory function used to specify additional info about
             the fields of a dataclass
"""


@dataclass
class Student:

    """student class"""

    name: str
    surname: str
    is_active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """post init, will be called after __init__"""
        self.login = self.name[0] + self.surname
