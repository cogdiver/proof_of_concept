# Understanding slots in Python

## Project Overview
This repository contains a series of proof of concept scripts designed to demonstrate and explore the use of `__slots__` in Python classes. Utilizing `__slots__` can offer performance and memory usage improvements over the standard class behavior in Python. This repository serves as both an educational resource and a starting point for those interested in implementing `__slots__` in their Python classes.

## Data Structure

```python
# Definition of classes to use
class SinSlots:
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def attributes_access(self):
        return self.name, self.identifier

class ConSlots:
    __slots__ = ('name', 'identifier')

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier

    def attributes_access(self):
        return self.name, self.identifier

class ConSlotsList:
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
```
```python
# Class instances are created
sin_slots = SinSlots('Test', 123)
con_slots = ConSlots('Test', 123)
list_slots = ConSlotsList('Test', 123)
```

## Advantages

- **Similar use:** Attributes are accessed in the same way. [see function](./tests/advantages.py#L7-L38)
```bash
python main.py usage
```
```python
print(sin_slots.name)
print(sin_slots.identifier)

print(con_slots.name)
print(con_slots.identifier)
```
```
+ ----------------- +
|     Sin Slots     |
+ ----------------- +
| name: Test        |
| identifier: 123   |
+ ----------------- +

+ ----------------- +
|     Con Slots     |
+ ----------------- +
| name: Test        |
| identifier: 123   |
+ ----------------- +
```

- **Access speed:** It may be a little faster in accessing class attributes, however, it is not as significant. [see function](./tests/advantages.py#L41-L72)
```bash
python main.py faster_access
```
```python
import timeit

execution_times=50000000
time_sin_slots = timeit.timeit(sin_slots.attributes_access, number=execution_times)
time_con_slots = timeit.timeit(con_slots.attributes_access, number=execution_times)

print(time_sin_slots)
print(time_con_slots)
```
```
+ --------------------- +
|      Access Times     |
+ --------------------- +
| sin_slots: 9.518278   |
| con_slots: 8.489578   |
+ --------------------- +
```

- **Memory space:** It is more efficient in terms of memory used when instantiating objects. [see function](./tests/advantages.py#L75-L106)
```bash
python main.py memory_saving
```
```python
from pympler import asizeof

number_of_instances=1000
sin_slots = [SinSlots('Test', 123) for _ in range(number_of_instances)]
con_slots = [ConSlots('Test', 123) for _ in range(number_of_instances)]

print(asizeof.asizeof(sin_slots))
print(asizeof.asizeof(con_slots))
```
```
+ -------------------- +
|  Memory Consumption  |
+ -------------------- +
| sin_slots: 161,064   |
| con_slots: 56,944    |
+ -------------------- +
```

- **Secure access:** Avoid the creation of attributes that are not defined in the class. [see function](./tests/advantages.py#L109-L139)
```bash
python main.py secure_access
```
```python
sin_slots.identifier = 1234
sin_slots.age = 25
print(sin_slots.identifier)
print(sin_slots.age)

con_slots.identifier = 1234
con_slots.age = 25
print(con_slots.identifier)
print(con_slots.age)
```
```
+ ---------------------------------------------------------------------------- +
|                                Secure Access                                 |
+ ---------------------------------------------------------------------------- +
| sin_slots: identifier(1234)                                                  |
| sin_slots: age(25)                                                           |
| con_slots: identifier(1234)                                                  |
| con_slots: age(AttributeError("'ConSlots' object has no attribute 'age'"))   |
+ ---------------------------------------------------------------------------- +
```

## Drawbacks
- **`__slots__` with lists:** The declaration of slots can be done with any iterable that is not a string, therefore, defining it with lists instead of tuples can allow its modification, which would also affect other instances. [see function](./tests/drawbacks.py#L6-L54)
```bash
python main.py slots_as_list
```
```python
con_slots = ConSlots('Test', 123)
list_slots = ConSlotsList('Test', 123)
list_slots_2 = ConSlotsList('Test', 123)

print(list_slots.__slots__)
print(list_slots_2.__slots__)
print(con_slots.__slots__)

list_slots.__slots__[0] = "change_name"
con_slots.__slots__[0] = "change_name"
# >>> TypeError: 'tuple' object does not support item assignment

print(list_slots.__slots__)
print(list_slots_2.__slots__)
print(con_slots.__slots__)
```
```
+ -------------------------------------- +
|           Initial __slots__            |
+ -------------------------------------- +
| list_slots: ['name', 'identifier']     |
| list_slots_2: ['name', 'identifier']   |
| con_slots: ('name', 'identifier')      |
+ -------------------------------------- +

+ ------------------------------------------------------------------------- +
|                              Final __slots__                              |
+ ------------------------------------------------------------------------- +
| list_slots: ['change_name', 'identifier']                                 |
| list_slots_2: ['change_name', 'identifier']                               |
| con_slots: TypeError("'tuple' object does not support item assignment")   |
+ ------------------------------------------------------------------------- +
```

- **Use of `__weakref__`:** When a class in Python does not define `__slots__`, a `__weakref__` attribute is automatically added to each instance of that class. This attribute is required for weak references to the instance to work correctly. [see function](./tests/drawbacks.py#L57-L93)
```bash
python main.py weakref_access
```
```python
import weakref

print(sin_slots)
print(con_slots)

weak_sin_slots = weakref.ref(sin_slots)
print(weak_sin_slots)
weak_con_slots = weakref.ref(con_slots)
# >>> TypeError: cannot create weak reference to 'ConSlots' object
```
```
+ -------------------------------------------------------------------------------- +
|                             Creating Weak References                             |
+ -------------------------------------------------------------------------------- +
| sin_slots: <models.classes.SinSlots object at 0x7fd9ce84dd60>                    |
| weak_sin_slots: <weakref at 0x7fd9ce7b65e0; to 'SinSlots' at 0x7fd9ce84dd60>     |
| con_slots: <models.classes.ConSlots object at 0x7fd9c31a4130>                    |
| weak_con_slots: TypeError("cannot create weak reference to 'ConSlots' object")   |
+ -------------------------------------------------------------------------------- +
```

- **Access to `__dict__`:** A `__slots__` declaration uses less memory than a dictionary, and direct memory access is faster than dictionary lookups, so the `__dict__` attribute is not created. [see function](./tests/drawbacks.py#L96-L128)
```bash
python main.py dict_access
```
```python
print(sin_slots.__dict__)
# >>> {'name': 'Test', 'identifier': 123}

print(con_slots.__dict__)
# >>> AttributeError: 'ConSlots' object has no attribute '__dict__'
```
```
+ ---------------------------------------------------------------------------- +
|                               __dict__ Access                                |
+ ---------------------------------------------------------------------------- +
| sin_slots: {'name': 'Test', 'identifier': 123}                               |
| con_slots: AttributeError("'ConSlots' object has no attribute '__dict__'")   |
+ ---------------------------------------------------------------------------- +
```

- **Inheritance:** Classes derived from a class with `__slots__` do not automatically inherit `__slots__`. If you want a subclass to have its own `__slots__`, you must define them explicitly. [see function](./tests/drawbacks.py#L131-L184)
```bash
python main.py inheritance
```
```python
class BaseConSlots1(ConSlots):
    pass

class BaseConSlots2(ConSlots):
    __slots__ = ("age")

class BaseConSlots3(ConSlots):
    __slots__ = ("age")
    def __init__(self, name, identifier, age):
        super().__init__(name, identifier)
        self.age = age

base_1 = BaseConSlots1('Test', 123)
base_2 = BaseConSlots2('Test', 123)
base_3 = BaseConSlots3('Test', 123)

base_1.__slots__
# >>> ('name', 'identifier')
base_2.__slots__
# >>> 'age'
base_3.__slots__
# >>> 'age'

base_1.__dict__
# >>> {}
base_2.__dict__
# >>> AttributeError: 'BaseConSlots2' object has no attribute '__dict__'
base_3.__dict__
# >>> AttributeError: 'BaseConSlots2' object has no attribute '__dict__'

# Modification of existing attributes
base_1.identifier = 1234
base_2.identifier = 1234
base_3.identifier = 1234

base_1.last_name = "Test" # deja crear nuevos atributos
base_2.last_name = "Test"
# >>> AttributeError: 'BaseConSlots2' object has no attribute 'last_name'
base_3.last_name = "Test"
# >>> AttributeError: 'BaseConSlots2' object has no attribute 'last_name'
```
```
+ ----------------------------------------------------------------------------------------- +
|                                    Inheritance Behavior                                   |
+ ----------------------------------------------------------------------------------------- +
| base_1.__slots__: ('name', 'identifier')                                                  |
| base_1.__dict__: {}                                                                       |
| base_1.last_name: Test # new attributes                                                   |
| base_2.__slots__: age                                                                     |
| base_2.__dict__: AttributeError("'BaseConSlots2' object has no attribute '__dict__'")     |
| base_2.last_name: AttributeError("'BaseConSlots2' object has no attribute 'last_name'")   |
| base_3.__slots__: age                                                                     |
| base_3.__dict__: AttributeError("'BaseConSlots3' object has no attribute '__dict__'")     |
| base_3.last_name: AttributeError("'BaseConSlots3' object has no attribute 'last_name'")   |
+ ----------------------------------------------------------------------------------------- +
```


## Conclusions

In conclusion, the proof of concept scripts in this repository effectively demonstrate the advantages and limitations of using `__slots__` in Python classes. The key takeaways include:

1. **Similar Usage:** The manner in which attributes are accessed remains unchanged, providing a familiar interface for those accustomed to standard Python classes.

2. **Access Speed:** A marginal increase in attribute access speed is observed, indicating potential performance benefits in certain applications.

3. **Memory Efficiency:** A significant reduction in memory usage is noted when instantiating objects, highlighting `__slots__` as a viable option for memory-sensitive applications.

4. **Secure Access:** `__slots__` contributes to more secure attribute access by preventing the creation of unintended attributes, thereby enforcing a stricter class structure.

However, it is important to consider the drawbacks, such as the peculiarities in declaring slots with lists, the absence of `__weakref__` and `__dict__` attributes, and the implications for class inheritance. These limitations suggest that while `__slots__` can be beneficial in specific contexts, careful consideration and understanding of its behavior are essential when integrating it into Python projects. This repository not only sheds light on these aspects but also serves as a practical guide for those looking to implement `__slots__` in their Python development endeavors.

## References
- [UssingSlots documentation](https://wiki.python.org/moin/UsingSlots)