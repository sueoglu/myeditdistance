from importlib.metadata import version

from . import pl, pp, tl

__all__ = ["pl", "pp", "tl"]

__version__ = version("firsttask")


def edit_distance(string1, string2):
    return tl.edit_distance(string1, string2)
