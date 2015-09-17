# RES Accounting Service
# Copyright © 2015 InvestGroup, LLC


import argparse
import inspect
import sys


def get_argument_parser(description):
    return argparse.ArgumentParser(description=description)


def gather_parsers(parser, packages=tuple()):
    packages = (sys.modules[__name__].__package__,) + packages
    for pkg in packages:
        for _, mod in inspect.getmembers(pkg, inspect.ismodule):
            initfn = getattr(mod, "init_argument_parser", None)
            if initfn is not None:
                parser = initfn(parser)
    return parser
