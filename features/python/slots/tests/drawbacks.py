from models.classes import SinSlots, ConSlots, ConSlotsList
from utils.prints import print_box
import weakref


def slots_as_list():
    """
    Demonstrates the behavior of __slots__ when defined as a list in Python classes.

    This function creates instances of two classes: `ConSlots` and `ConSlotsList`. 
    Both classes are expected to use __slots__, but `ConSlotsList` is specifically 
    designed to define __slots__ as a mutable list. The function then attempts to 
    modify the __slots__ attribute of these instances to observe the behavior.

    It first prints the initial __slots__ of each instance using `print_box`, a 
    function that displays the information in a formatted box. Then, it attempts 
    to modify the __slots__ of `list_slots` (which should succeed) and `con_slots` 
    (which should fail and raise an exception), capturing the results or exceptions 
    in each case.

    The final state of the __slots__ for each instance is then displayed, illustrating 
    the difference in behavior when __slots__ is defined as a mutable list compared 
    to the typical immutable tuple.

    Returns: None
    """
    con_slots = ConSlots('Test', 123)
    list_slots = ConSlotsList('Test', 123)
    list_slots_2 = ConSlotsList('Test', 123)

    print_box(
        title="Initial __slots__",
        rows=[
            f"list_slots: {list_slots.__slots__}",
            f"list_slots_2: {list_slots_2.__slots__}",
            f"con_slots: {con_slots.__slots__}",
        ]
    )

    results= []
    list_slots.__slots__[0] = "change_name"
    results.append(f"list_slots: {list_slots.__slots__}")
    results.append(f"list_slots_2: {list_slots_2.__slots__}")

    try:
        con_slots.__slots__[0] = "change_name"
        results.append(f"con_slots: {con_slots.__slots__}")
    except Exception as e:
        results.append(f"con_slots: {repr(e)}")

    print_box(
        title="Final __slots__",
        rows=results,
    )


def weakref_access():
    """
    Demonstrates the creation and access of weak references to objects.

    This function creates instances of two classes, `SinSlots` and `ConSlots`, and then 
    attempts to create weak references to these instances using the `weakref.ref` method. 
    It captures the results of these attempts, including any exceptions that might occur 
    during the creation of weak references, especially in the case of objects that may not 
    support weak references (like those without `__weakref__` in their `__slots__`).

    The function records the outcomes and then prints them in a structured format using 
    the `print_box` function. This includes the original objects and their corresponding 
    weak references, providing insight into how weak references behave with different types 
    of objects in Python.

    Returns: None
    """
    sin_slots = SinSlots('Test', 123)
    con_slots = ConSlots('Test', 123)

    results = []

    results.append(f"sin_slots: {sin_slots}")
    weak_sin_slots = weakref.ref(sin_slots)
    results.append(f"weak_sin_slots: {weak_sin_slots}")

    try:
        results.append(f"con_slots: {con_slots}")
        weak_con_slots = weakref.ref(con_slots)
        results.append(f"weak_con_slots: {weak_con_slots}")
    except Exception as e:
        results.append(f"weak_con_slots: {repr(e)}")

    print_box(
        title="Creating Weak References",
        rows=results,
    )


def dict_access():
    """
    Demonstrates the access to the __dict__ attribute in objects with and without __slots__.

    This function creates instances of two classes, `SinSlots` and `ConSlots`. The `SinSlots` class
    is a regular Python class that allows dynamic attribute assignment, while `ConSlots` is defined 
    with __slots__ which may restrict dynamic attribute assignment and the presence of a __dict__ attribute.

    The function attempts to access the __dict__ attribute of both instances and records the results.
    For the `ConSlots` instance, which might not have a __dict__ attribute due to the use of __slots__,
    it handles any exceptions that occur and records them.

    The outcomes, including the content of the __dict__ attribute for `SinSlots` and any exception 
    messages for `ConSlots`, are then printed in a structured format using the `print_box` function.
    This helps in understanding the implications of using __slots__ in terms of object attribute storage.

    Returns: None
    """
    sin_slots = SinSlots('Test', 123)
    con_slots = ConSlots('Test', 123)

    results = []
    results.append(f"sin_slots: {sin_slots.__dict__}")

    try:
        results.append(f"con_slots: {con_slots.__dict__}")
    except Exception as e:
        results.append(f"con_slots: {repr(e)}")

    print_box(
        title="__dict__ Access",
        rows=results,
    )


def inheritance():
    """
    Demonstrates the behavior of __slots__ and __dict__ in class inheritance.

    This function defines three classes, `BaseConSlots1`, `BaseConSlots2`, and `BaseConSlots3`, 
    each inheriting from `ConSlots`. `BaseConSlots1` does not define additional __slots__, 
    while `BaseConSlots2` and `BaseConSlots3` add an 'age' slot. Additionally, `BaseConSlots3` 
    includes a custom constructor to initialize the 'age' attribute.

    Instances of these three classes are created and stored in a dictionary. The function 
    iterates over these instances to:
    1. Display their __slots__.
    2. Attempt to access their __dict__ attribute and catch exceptions if they occur.
    3. Try to add a new attribute 'last_name' to each instance and catch any exceptions.

    Returns: None
    """
    class BaseConSlots1(ConSlots):
        pass

    class BaseConSlots2(ConSlots):
        __slots__ = ("age")

    class BaseConSlots3(ConSlots):
        __slots__ = ("age")
        def __init__(self, name, identifier, age):
            super().__init__(name, identifier)
            self.age = age

    base_obj = {
        "base_1": BaseConSlots1('Test', 123),
        "base_2": BaseConSlots2('Test', 123),
        "base_3": BaseConSlots3('Test', 123, 25),
    }

    results = []
    for k, b in base_obj.items():
        results.append(f"{k}.__slots__: {b.__slots__}")

        try:
            results.append(f"{k}.__dict__: {b.__dict__}")
        except Exception as e:
            results.append(f"{k}.__dict__: {repr(e)}")

        try:
            b.last_name = "Test"
            results.append(f"{k}.last_name: {b.last_name} # new attributes")
        except Exception as e:
            results.append(f"{k}.last_name: {repr(e)}")

    print_box(
        title="Inheritance Behavior",
        rows=results,
    )
