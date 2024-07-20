from utils.prints import print_box
import importlib


def dynamic_imports():
    """
    Demonstrates the use of dynamic imports in Python using both importlib.import_module()
    and __import__() functions.
    The function showcases the flexibility of Python's import system, allowing for dynamic 
    module loading and access to module-level variables.
    """
    # Import modules dynamicly
    m1 = importlib.import_module("modules")
    m2 = importlib.import_module("modules.one")
    m3 = __import__("modules")
    m4 = __import__("modules.one")

    print_box(
        title="dynamic_imports function execution",
        rows=[
            m1.PACKAGE_LEVEL_IMPORT,
            m2.PACKAGE_LEVEL_IMPORT,
            m3.PACKAGE_LEVEL_IMPORT,
            m4.PACKAGE_LEVEL_IMPORT,
        ]
    )

    # Reload moduls if there were changes
    importlib.reload(m1)
    importlib.reload(m2)
