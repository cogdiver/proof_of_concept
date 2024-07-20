from utils.prints import print_box
from modules.two.import_without_all import show_imports as s_without
from modules.two.import_with_all import show_imports as s_with


def use_of_all():
    print_box(title="Import without all specified")
    s_without()

    print_box(title="Import with all specified")
    s_with()
