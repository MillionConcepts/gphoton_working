from collections.abc import Callable

import objgraph
from pympler import muppy
from pympler.asizeof import asizeof


def get_biggest_vars(how_many: int):
    return muppy.sort(muppy.get_objects())[-how_many:]


def get_size_and_id(obj):
    return f"{asizeof(obj)/1024**2} {id(obj)}"


def make_big_ref_graph(how_many: int, callback: Callable = get_size_and_id):
    biggest = get_biggest_vars(how_many)
    objgraph.show_backrefs(biggest, extra_info=callback, filename="back.dot")
    objgraph.show_refs(biggest, extra_info=callback, filename="ref.dot")
