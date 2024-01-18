from models.classes import SinSlots, ConSlots
from utils.prints import print_box
from pympler import asizeof
import timeit


def usage():
    """
    Demonstrates the usage of classes with and without __slots__.

    This function creates instances of two classes, `SinSlots` and `ConSlots`. 
    `SinSlots` is a regular class without the use of __slots__, while `ConSlots` 
    is defined with __slots__ to optimize memory usage.

    It then prints the attributes of these instances in a formatted box using the 
    `print_box` function. The printed attributes include the 'name' and 'identifier' 
    of each instance.

    Returns: None
    """
    sin_slots = SinSlots('Test', 123)
    con_slots = ConSlots('Test', 123)

    print_box(
        title="Sin Slots",
        rows=[
            f"name: {sin_slots.name}",
            f"identifier: {sin_slots.identifier}"
        ]
    )

    print_box(
        title="Con Slots",
        rows=[
            f"name: {con_slots.name}",
            f"identifier: {con_slots.identifier}"
        ]
    )


def faster_access(execution_times=50000000):
    """
    Measures and compares the attribute access times of instances of classes with and without __slots__.

    This function creates instances of two classes, `SinSlots` and `ConSlots`, which represent a 
    regular class and a class with __slots__ respectively. It then measures the time taken to 
    access attributes of these instances repeatedly, providing a comparison of the performance 
    in terms of attribute access speed.

    After measuring, the function prints the results using the `print_box` function, displaying 
    the execution times for both `SinSlots` and `ConSlots` in a formatted box.

    Parameters:
    - execution_times (int, optional): The number of times the attribute access operation is executed 
      for the time measurement. Default is 50,000,000.

    Returns: None
    """
    sin_slots = SinSlots('Test', 123)
    con_slots = ConSlots('Test', 123)

    # measure execution times
    time_sin_slots = timeit.timeit(sin_slots.attributes_access, number=execution_times)
    time_con_slots = timeit.timeit(con_slots.attributes_access, number=execution_times)

    print_box(
        title="Access Times",
        rows=[
            f"time_sin_slots: {time_sin_slots:4f}",
            f"time_con_slots: {time_con_slots:4f}"
        ]
    )


def memory_saving(number_of_instances=1000):
    """
    Compares memory usage between classes with and without __slots__.

    This function creates a specified number of instances for two classes, 
    `SinSlots` and `ConSlots`, and measures their memory usage. `SinSlots` 
    is a regular class, while `ConSlots` uses __slots__ for potentially 
    reduced memory usage. 

    The memory consumption of the created instances is measured using 
    `asizeof.asizeof` from the Pympler module, providing a comparison 
    of how __slots__ can impact memory efficiency in Python classes.

    Parameters:
    - number_of_instances (int, optional): The number of instances to create 
      for each class. Default is 1000.

    Returns: None
    """
    sin_slots = [SinSlots('Test', 123) for _ in range(number_of_instances)]
    con_slots = [ConSlots('Test', 123) for _ in range(number_of_instances)]

    memory_sin_slots = asizeof.asizeof(sin_slots)
    memory_con_slots = asizeof.asizeof(con_slots)

    print_box(
        title="Memory Consumption",
        rows=[
            f"memory_sin_slots: {memory_sin_slots:,.0f}",
            f"memory_con_slots: {memory_con_slots:,.0f}"
        ]
    )


def secure_access():
    sin_slots = SinSlots('age_sin_slots', 123)
    con_slots = ConSlots('age_con_slots', 123)
    results = []

    for c in (sin_slots, con_slots):
        try:
            c.identifier = 1234
            c.age = 25
            results.append(f"{c.name}: identifier({c.identifier}) age({c.age})")
        except Exception as e:
            results.append(f"{c.name}: identifier({c.identifier}) age({repr(e)})")

    print_box(
        title="Secure Access",
        rows=results
    )
