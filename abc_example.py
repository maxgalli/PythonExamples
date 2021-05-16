from abc import ABC, abstractmethod

class AbstractBaseClass(ABC):
    @abstractmethod
    def do_something(self, val):
        print(val)

class DerivedClass(AbstractBaseClass):
    """Example of a class derived from an abstract class 
    where the abstract method is reimplemented
    """
    def do_something(self, val):
        print("From derived")

class DerivedClass2(AbstractBaseClass):
    """Example of a class derived from an abstract class
    where the abstract method is NOT reimplemented
    """
    def do_something(self, val):
        return super().do_something(val)

obj1 = DerivedClass()
obj1.do_something(40)

obj2 = DerivedClass2()
obj2.do_something(40)