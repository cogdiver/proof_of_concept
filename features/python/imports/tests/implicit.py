from utils.prints import print_box
import modules
import modules.one


def implicit_imports():
    """
    Demonstrates the use of an implicit import within a package.

    This function imports the `modules` package and prints the value of 
    the `PACKAGE_LEVEL_IMPORT` variable, which is set at the package level 
    in the `__init__.py` file of the `modules` package. The purpose of this 
    function is to showcase how implicit imports work in Python packages, 
    allowing access to package-level variables or settings.
    """
    print_box(
        title="implicit_imports function execution",
        rows=[
            modules.PACKAGE_LEVEL_IMPORT,
            modules.one.PACKAGE_LEVEL_IMPORT,
        ]
    )
