from models.classes import SinSlots, ConSlots
from utils.prints import print_box


def slots_as_list():
    sin_slots = SinSlots('age_sin_slots', 123)
    con_slots = ConSlots('age_con_slots', 123)


def weakref_access():
    sin_slots = SinSlots('age_sin_slots', 123)
    con_slots = ConSlots('age_con_slots', 123)


def dict_access():
    sin_slots = SinSlots('age_sin_slots', 123)
    con_slots = ConSlots('age_con_slots', 123)


def inheritance():
    sin_slots = SinSlots('age_sin_slots', 123)
    con_slots = ConSlots('age_con_slots', 123)
