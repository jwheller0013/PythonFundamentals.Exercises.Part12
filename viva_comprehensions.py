from typing import List, Dict, Set, Callable
import enum


class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    method is checking for parity (odd or even) between a set of int (start to stop)

    :param start:
    :param stop:
    :param parity:
    :return:
    """
    pass

    if parity == Parity.ODD:
        list_result = [int(value) for value in range(start, stop) if (value % 2 == 1)]
        return list_result
    if parity == Parity.EVEN:
        list_result = [int(value) for value in range(start, stop) if (value % 2 == 0)]
        return list_result


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    in range start to stop run strategy() on said number

    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    pass
    gen = {i: strategy(i) for i in range(start, stop)}
    return gen

def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    only take lowercase letters from word making a set

    :param val_in:
    :return:
    """
    pass

    gen = {val_in.upper() for val_in in val_in if val_in.islower()}
    return gen