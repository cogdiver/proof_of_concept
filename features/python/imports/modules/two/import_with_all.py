from modules.two.with_all import *


def show_imports():
    try:
        print(PUBLIC_VARIABLE)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")

    try:
        print(public_function)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")

    try:
        print(PublicClass)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")

    try:
        print(_PRIVATE_VARIABLE)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")

    try:
        print(_private_function)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")

    try:
        print(_PrivateClass)
    except Exception as e:
        print(f"[ERROR]: {repr(e)}")
