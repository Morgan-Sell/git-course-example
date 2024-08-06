var: str = 1


def sum_first_column_of_csv(csv):
    pass


class Duck:
    def __init__(self): ...

    def __getattr__(self, attr):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


duck = Duck()

duck.quack()
duck.walk()

var: int = 1
var = "hi"


def consume_many_types(
    num: int, decimal: float, boolean: bool, string: str, binary: bytes, obj: object
) -> None: ...


from collections import namedtuple
from dataclasses import dataclass
from typing import (
    Any,
    Dict,
    Iterable,
    List,
    NamedTuple,
    Optional,
    Set,
    Tuple,
    Type,
    TypedDict,
    Union,
)

nums: List[int] = []
x: int = 1
three_dimensional_vector: Tuple[int, float, str] = (1, 2.0, "hi")
n_dimensional_vector: Tuple[float, ...] = (1, 2, 3, 4, 5)
students_to_ages: Dict[str, int] = {
    "bobby": 25,
    "muprh": 27,
    "alice": 21,
}
fruits: Set[str] = {"apple", "kiwi", "banana"}


class Animal: ...


miscellaneous_values: List[Union[int, float, str, Type]] = [1, 1.0, "hi", object]

"""
student: Dict[str, Union[str, int]]= {
    "name": "Marcy",
    "age": 25,
}
"""


class Point(NamedTuple):
    x: int
    y: int


point2d = Point(1, 2)
point2d.x
point2d.y


# Looser than a class.
# Do not need to set all attributes because it is a dictionary.
class Student(TypedDict):
    name: str
    age: int
    position: Point
    friends: List["Student"]


student: Student = {
    "name": "Marcy",
    "age": 25,
    "position": Point(1, 2),
    "friends": [
        {
            "name": "Marcy",
            "age": 25,
            "position": Point(1, 2),
            "friends": [],
        }
    ],
}

@dataclass
class Student(TypedDict):
    name: str
    age: int
    position: Point
    friends: List["Student"]

TStudentArgsDictKeys = Union[str, int, Point, List[Student]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]

def add(a, b):
    return a + b