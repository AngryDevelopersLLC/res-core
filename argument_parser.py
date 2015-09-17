# RES Accounting Service
# Copyright © 2015 InvestGroup, LLC


import argparse
import inspect
import sys


ARGPARSE_DESCRIPTION = "Change res.core.argument_parser.ARGPARSE_DESCRIPTION!"

def get_argument_parser():
    return argparse.ArgumentParser(description=ARGPARSE_DESCRIPTION)


def gather_parsers(parser, packages=tuple()):
    packages = (sys.modules[sys.modules[__name__].__package__],) + \
        tuple(packages)
    for pkg in packages:
        for _, mod in inspect.getmembers(pkg, inspect.ismodule):
            initfn = getattr(mod, "init_argument_parser", None)
            if initfn is not None:
                parser = initfn(parser)
    return parser
