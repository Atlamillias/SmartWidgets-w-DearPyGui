from dearpygui.core import *
from dearpygui.simple import *
import inspect
import functools

DPG = {k:v for k,v in globals().items() if "mv" in k}


def logging(func):
    @functools.wraps(func)
    def deco(*args, **kwargs):
        returned = func(*args, **kwargs)
        log(f"{inspect.getframeinfo()}", level = 0)
        return returned

    return deco


def debuglog(func, **vars):
    if get_log_level() > 0:
        vars = '\n    '.join(f'{k}: {v}' for k,v in vars.items())
        log_debug(f"| {type(func)} '{func.__name__}'| vars:\n    {vars}")


if __name__ == "__main__":
    for k in DPG.items():
        print(k)

    print(len(DPG))



