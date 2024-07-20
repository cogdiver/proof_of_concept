# Exploring Python Imports

## Project Overview
This repository hosts a proof of concept project centered around the exploration and management of imports in Python. It delves into the nuances of Python's import system, examining both standard and dynamic importing techniques, and their implications on code efficiency, readability, and maintainability. This project not only demonstrates various importing strategies but also serves as a foundation for those looking to optimize and refine their use of imports in Python programming.


## Practice

### Implicit imports

Implicit imports in Python allow you to access package-level variables, functions, or objects defined in the `__init__.py` file of a module. When you perform a module-level import, the `__init__.py` file of the respective module is executed. Any variables, functions, or objects defined in `__init__.py` become available through the module object. [see function](./tests/implicit.py.py#L6-L22)

```bash
# Bash
python main.py implicit
```
```python
# python
import modules
import modules.one
print(modules.PACKAGE_LEVEL_IMPORT)
print(modules.one.PACKAGE_LEVEL_IMPORT)
```
_output:_
```terminal
PACKAGE_LEVEL_IMPORT: implicit modules
PACKAGE_LEVEL_IMPORT: implicit modules.one
implicit modules
implicit modules.one
```

### Dynamic Imports

Dynamic imports in Python enable you to import modules at runtime using the `importlib.import_module` or `__import__` function. This approach allows for the flexible and on-the-fly importation of modules based on variable values or runtime conditions. By utilizing this functions, you can dynamically specify the module name, which can be particularly useful in scenarios where the modules to be imported are not known until the code is executed. [see function](./tests/dynamic.py#L5-L30)

```bash
# Bash
python main.py dynamic
```
```python
# python
import importlib
m1 = importlib.import_module("modules")
m2 = importlib.import_module("modules.one")
m3 = __import__("modules")
m4 = __import__("modules.one")
print(m1.PACKAGE_LEVEL_IMPORT)
print(m2.PACKAGE_LEVEL_IMPORT)
print(m3.PACKAGE_LEVEL_IMPORT)
print(m4.PACKAGE_LEVEL_IMPORT)
```
_output:_
```terminal
PACKAGE_LEVEL_IMPORT: implicit modules!!!!
PACKAGE_LEVEL_IMPORT: implicit modules.one
implicit modules
implicit modules.one
implicit modules
implicit modules
```
>The most important difference between these two functions is that import_module() returns the specified package or module (e.g. pkg.mod), while __import__() returns the top-level package or module (e.g. pkg).

<br/>

_To reload modules:_ [see](./tests/dynamic.py#L28-L30)
```python
importlib.reload(m1)
importlib.reload(m2)
print(m1.PACKAGE_LEVEL_IMPORT)
print(m2.PACKAGE_LEVEL_IMPORT)
```
_output:_
```terminal
PACKAGE_LEVEL_IMPORT: implicit modules
PACKAGE_LEVEL_IMPORT: implicit modules.one
implicit modules
implicit modules.one
```

### Dynamic Execution

Dynamic execution in Python refers to the ability to call functions or execute code that is determined at runtime. This can be achieved by using functions such as `getattr`, which allows you to retrieve attributes (including functions) from a module or object by name, specified as a string. This technique is useful for executing functions whose names are not known until the program is running. [see function](./tests/execution.py#L26-L41)


```bash
# Bash
python main.py execution
```
```python
# python
def import_and_execute(module_name, function_name, *args, **kwargs):
    # Import the module dynamically
    module = importlib.import_module(module_name)
    # Get the function from the module
    func = getattr(module, function_name)
    # Execute the function with provided arguments
    return func(*args, **kwargs)

l1 = import_and_execute("modules", "print_pkg_level_import")
l2 = import_and_execute("modules.one", "print_pkg_level_import")
print(l1)
print(l2)
```
_output:_
```terminal
PACKAGE_LEVEL_IMPORT: implicit modules
PACKAGE_LEVEL_IMPORT: implicit modules.one
PACKAGE_LEVEL_IMPORT: implicit modules
PACKAGE_LEVEL_IMPORT: implicit modules.one
PACKAGE_LEVEL_IMPORT: implicit modules
PACKAGE_LEVEL_IMPORT: implicit modules.one
```
>NOTE: The first two lines for the implicit import,
the second two by the import_and_execute function and
the last two for printing the variables l1 and l2

<br/>

### Use import *

`import *` in Python involves importing all public symbols from a module dynamically at runtime. 
This can be controlled using the `__all__` attribute within the module, which explicitly defines the list of names to be imported when `import *` is used. By specifying `__all__`, you can selectively include or exclude certain symbols. Conversely, omitting `__all__` allows for all non-private (non-underscore prefixed) symbols to be imported by default.

This approach is particularly useful when you need to dynamically import a large number of symbols from a module without explicitly listing each one. However, it is essential to use `__all__` to prevent the unintentional import of public symbols and to enforce the import of private symbols if needed. This method ensures better control over the namespace and avoids potential naming conflicts. [see function](./tests/execution.py#L26-L41)


```bash
# Bash
python main.py asterisk
```
```python
# python
from modules.two.without_all import *
print(PUBLIC_VARIABLE)
print(public_function)
print(PublicClass)
print(_PRIVATE_VARIABLE)
print(_private_function)
print(_PrivateClass)
```
_output:_
```terminal
+ ------------------------------ +
|  Import without all specified  |
+ ------------------------------ +
This is a public variable
<function public_function at 0x7f0b1376f940>
<class 'modules.two.without_all.PublicClass'>
[ERROR]: NameError("name '_PRIVATE_VARIABLE' is not defined")
[ERROR]: NameError("name '_private_function' is not defined")
[ERROR]: NameError("name '_PrivateClass' is not defined")
```
```python
# python
from modules.two.with_all import *
print(PUBLIC_VARIABLE)
print(public_function)
print(PublicClass)
print(_PRIVATE_VARIABLE)
print(_private_function)
print(_PrivateClass)
```
_output:_
```terminal
+ --------------------------- +
|  Import with all specified  |
+ --------------------------- +
This is a public variable
<function public_function at 0x7f0b1376fca0>
[ERROR]: NameError("name 'PublicClass' is not defined")
This is a private variable
[ERROR]: NameError("name '_private_function' is not defined")
[ERROR]: NameError("name '_PrivateClass' is not defined")
```

## Conclusions

In this proof of concept project, we have explored various importing strategies in Python, including implicit imports, dynamic imports, dynamic execution, and the use of `import *`. Each technique offers unique advantages and potential drawbacks:

1. **Implicit Imports**: These are useful for organizing code and making package-level variables, functions, or objects readily accessible. They improve readability by encapsulating common functionalities at the package level.

2. **Dynamic Imports**: These provide flexibility by allowing modules to be imported at runtime based on variable values or conditions. This is particularly useful in scenarios where the modules to be imported are not known until the code is executed.

3. **Dynamic Execution**: This allows for the execution of code or functions determined at runtime. It offers a powerful way to handle dynamic function calls but requires careful handling to avoid runtime errors.

4. **Import**: This can be useful for importing a large number of symbols without explicitly listing each one. However, it should be used cautiously to avoid namespace pollution and potential naming conflicts. Using the `__all__` attribute helps control which symbols are imported.

By understanding and appropriately using these techniques, developers can improve the efficiency, readability, and maintainability of their code. However, it is crucial to balance flexibility with clarity, ensuring that the code remains understandable and manageable.

## Recommendations

1. **Use Explicit Imports Where Possible**: Explicit imports improve readability and make dependencies clear. Avoid using `import *` unless absolutely necessary and control it using the `__all__` attribute.

2. **Leverage Dynamic Imports Sparingly**: While dynamic imports provide flexibility, overusing them can make the code harder to understand and debug. Use them only when the imported modules cannot be determined beforehand.

3. **Document Dynamic Execution**: When using dynamic execution techniques like `getattr`, ensure thorough documentation to clarify the expected behavior and possible runtime values.

4. **Regularly Review Imports**: Periodically review the imports in your codebase to ensure they are still necessary and optimally used. Remove any unused or redundant imports.

5. **Understand Performance Implications**: Be aware of the performance impact of different import strategies, especially in performance-critical applications. Measure and optimize as needed.

## References

1. [Python Documentation - The import system](https://docs.python.org/3/reference/import.html)
2. [PEP 328 - Imports: Multi-Line and Absolute/Relative](https://www.python.org/dev/peps/pep-0328/)
3. [PEP 302 - New Import Hooks](https://www.python.org/dev/peps/pep-0302/)
4. [Importing Python Modules](https://realpython.com/python-import/)
5. [Dynamic Imports in Python](https://www.pythoncentral.io/dynamically-import-module-python/)
6. [Understanding the Python Import System](https://docs.python-guide.org/writing/structure/#understanding-the-imports)
