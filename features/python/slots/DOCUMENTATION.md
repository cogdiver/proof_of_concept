# Understanding slots in Python

## Project Overview
This repository contains a series of proof of concept scripts designed to demonstrate and explore the use of __slots__ in Python classes. Utilizing __slots__ can offer performance and memory usage improvements over the standard class behavior in Python. This repository serves as both an educational resource and a starting point for those interested in implementing __slots__ in their Python classes.

## Advantages

- **Similar use:** Attributes are accessed in the same way. [see function](./tests/advantages.py#L7-L38)
```bash
python main.py usage
```
```
+ ------------------- +
|      Sin Slots      |
+ ------------------- +
| name: Test          |
| identifier: 123     |
+ ------------------- +

+ ------------------- +
|      Con Slots      |
+ ------------------- +
| name: Test          |
| identifier: 123     |
+ ------------------- +
```

- **Access speed:** It may be a little faster in accessing class attributes, however, it is not as significant. [see function](./tests/advantages.py#L41-L72)
```bash
python main.py faster_access
```
```
+ ---------------------------- +
|         Access Times         |
+ ---------------------------- +
| time_sin_slots: 8.841553     |
| time_con_slots: 8.657250     |
+ ---------------------------- +
```

- **Memory space:** It is more efficient in terms of memory used when instantiating objects. [see function](./tests/advantages.py#L75-L106)
```bash
python main.py memory_saving
```
```
+ ----------------------------- +
|       Memory Consumption      |
+ ----------------------------- +
| memory_sin_slots: 161,064     |
| memory_con_slots: 56,944      |
+ ----------------------------- +
```

- **Secure access:** Avoid the creation of attributes that are not defined in the class. [see function](./tests/advantages.py#L109-L125)
```bash
python main.py secure_access
```
```
+ --------------------------------------------------------------------------------------------------- +
|                                            Secure Access                                            |
+ --------------------------------------------------------------------------------------------------- +
| age_sin_slots: identifier(1234) age(25)                                                             |
| age_con_slots: identifier(1234) age(AttributeError("'ConSlots' object has no attribute 'age'"))     |
+ --------------------------------------------------------------------------------------------------- +
```

## Drawbacks
- Declaración de slots con listas: La declaracion de slots se puede hacer con cualquier iterable que no sea string, por lo tanto, al definirlo con listas en lugar de tuplas puede permitir su modificación que además afectaría a otras instancias. 

- uso de __weakref__: Cuando una clase en Python no define __slots__, se le agrega automáticamente un atributo __weakref__ a cada instancia de esa clase. Este atributo es necesario para que las referencias débiles a la instancia funcionen correctamente.

- No permite el acceso a __dict__: a __slots__ declaration uses less memory than a dictionary, and direct memory access is faster than dictionary lookups, por lo que no se crea el atributo __dict__

- **Herencia:** Las clases derivadas de una clase con __slots__ no heredan automáticamente los __slots__. Si quieres que una subclase tenga sus propios __slots__, debes definirlos explícitamente.


## Conclusions

In conclusion, the proof of concept scripts in this repository effectively demonstrate the advantages and limitations of using `__slots__` in Python classes. The key takeaways include:

1. **Similar Usage:** The manner in which attributes are accessed remains unchanged, providing a familiar interface for those accustomed to standard Python classes.

2. **Access Speed:** A marginal increase in attribute access speed is observed, indicating potential performance benefits in certain applications.

3. **Memory Efficiency:** A significant reduction in memory usage is noted when instantiating objects, highlighting `__slots__` as a viable option for memory-sensitive applications.

4. **Secure Access:** `__slots__` contributes to more secure attribute access by preventing the creation of unintended attributes, thereby enforcing a stricter class structure.

However, it is important to consider the drawbacks, such as the peculiarities in declaring slots with lists, the absence of `__weakref__` and `__dict__` attributes, and the implications for class inheritance. These limitations suggest that while `__slots__` can be beneficial in specific contexts, careful consideration and understanding of its behavior are essential when integrating it into Python projects. This repository not only sheds light on these aspects but also serves as a practical guide for those looking to implement `__slots__` in their Python development endeavors.

## References
- [UssingSlots documentation](https://wiki.python.org/moin/UsingSlots)