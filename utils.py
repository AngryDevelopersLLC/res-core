# RES Service Package
# Copyright © 2015 InvestGroup, LLC


from sys import stdin
from pytrie import StringTrie


def filter_argv(argv, option_strings, *blacklist):
    ptree = StringTrie({v: i for i, v in enumerate(blacklist)})
    filtered = []
    boolean_args = set(option_strings)
    i = -1
    while i + 1 < len(argv):
        i += 1
        arg = argv[i]
        has_value = arg.startswith("-") and \
            not any(arg.startswith(b) for b in boolean_args) \
            and '=' not in arg and arg != "-"
        if ptree.longest_prefix(arg, None) is None:
            filtered.append(arg)
            if has_value:
                i += 1
                filtered.append(argv[i])
        elif has_value:
            i += 1
    return filtered


def is_interactive():
    try:
        import __main__
        return getattr(__main__, "__loader__",
                       getattr(__main__, "__file__", None)) is None
    except ImportError:
        return False


def has_colors():
    return is_interactive() or (not stdin.closed and stdin.isatty())


def ellipsis(arr):
    return arr[:40], "..." if len(arr) > 40 else ""
