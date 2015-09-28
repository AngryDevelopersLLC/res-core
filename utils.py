# RES Service Package
# Copyright © 2015 InvestGroup, LLC


from six.moves import range as xrange
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


def dameraulevenshtein(seq1, seq2):
    """Calculate the Damerau-Levenshtein distance between sequences.

    This distance is the number of additions, deletions, substitutions,
    and transpositions needed to transform the first sequence into the
    second. Although generally used with strings, any sequences of
    comparable objects will work.

    Transpositions are exchanges of *consecutive* characters; all other
    operations are self-explanatory.

    This implementation is O(N*M) time and O(M) space, for N and M the
    lengths of the two sequences.

    >>> dameraulevenshtein('ba', 'abc')
    2
    >>> dameraulevenshtein('fee', 'deed')
    2

    It works with arbitrary sequences too:
    >>> dameraulevenshtein('abcd', ['b', 'a', 'c', 'd', 'e'])
    2
    """
    # codesnippet:D0DE4716-B6E6-4161-9219-2903BF8F547F
    # Conceptually, this is based on a len(seq1) + 1 * len(seq2) + 1 matrix.
    # However, only the current and two previous rows are needed at once,
    # so we only store those.
    oneago = None
    thisrow = list(range(1, len(seq2) + 1)) + [0]
    for x in xrange(len(seq1)):
        # Python lists wrap around for negative indices, so put the
        # leftmost column at the *end* of the list. This matches with
        # the zero-indexed strings and saves extra calculation.
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            # This block deals with transpositions
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1] and
                    seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]
