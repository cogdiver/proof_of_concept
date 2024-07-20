from utils.prints import print_box
import importlib


def import_and_execute(module_name, function_name, *args, **kwargs):
    """
    Imports a module and executes a specified function with provided arguments.

    Parameters:
        module_name (str): Name of the module to import.
        function_name (str): Name of the function to execute.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.
    """
    # Import the module dynamically
    module = importlib.import_module(module_name)

    # Get the function from the module
    func = getattr(module, function_name)

    # Execute the function with provided arguments
    # and return the results
    return func(*args, **kwargs)


def dynamic_execution():
    """
    Demonstrates the use of dynamic execution in Python by retrieving and
    calling functions at runtime using the getattr() function.
    The function showcases the flexibility of Python's attribute access system,
    allowing for the dynamic invocation of functions based on their names,
    which are specified as strings. This approach is particularly useful for
    executing functions whose names are not known until the code is running.
    """
    l1 = import_and_execute("modules", "print_pkg_level_import")
    l2 = import_and_execute("modules.one", "print_pkg_level_import")

    print_box(
        title="dynamic_execution function",
        rows=[ l1, l2 ]
    )
