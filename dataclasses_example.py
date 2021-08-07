"""
Documentation: https://docs.python.org/3/library/dataclasses.html


"""

from dataclasses import dataclass
from dataclasses import FrozenInstanceError
from dataclasses import field
from typing import List


@dataclass
class Comment1:
    # this is a field
    id: int

    # this is another field
    text: str

# a read-only class
@dataclass(frozen=True)
class Comment2:
    id: int
    text: str

# default values can also be specified using field
# for fields with mutable default values, it is suggested to use the default_factory argument
# (see https://www.youtube.com/watch?v=vBH6GRJ1REM)
@dataclass
class Comment3:
    id: int
    text: str = field(default="default text")
    # this can be simply list from Python 3.9
    replies: List[str] = field(default_factory=list)


def main():
    print("Instantiating Comment1 object...")
    c1 = Comment1(1, "text 1")
    print("c1 = {}".format(c1))

    print("Creating object Comment2 and trying to assign")
    c2 = Comment2(2, "text 2")
    print("c2 = {}".format(c2))
    try:
        c2.id = 3
    except FrozenInstanceError as e:
        print("Tried to assign value to attribute of class Comment2... {}".format(e))

    c3 = Comment3(3)
    print("c3 = {}".format(c3))

if __name__ == "__main__":
    main()
