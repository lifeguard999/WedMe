import os


def memoize(f):
    """ Cache function results, similar to py3.7 functools.lru_cache """
    memo = {}
    def helper(*args):
        key = tuple(args)
        if key not in memo:
            memo[key] = f(*args)
        return memo[key]
    return helper


@memoize
def get_project_path():
    """ Returns (absolute) path to project's root folder """
    path = os.path.abspath(__file__)
    while True:
        path, file = os.path.split(path)
        if file == 'src':  # assume the 'src' folder is in root folder (!!)
            return path
        elif file == '':
            raise RuntimeError("Could not find project's root directory")


@memoize
def get_abs_path(rel_path):
    """ finds absolute path of a file, given it's relative path from project's root folder """
    return os.path.join(get_project_path(), rel_path)


def fmt_price(amt):
    """ Format price as string with 2 decimals """
    return '{:,.2f}'.format(amt)
