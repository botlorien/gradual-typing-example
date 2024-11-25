from collections import abc

# Got error by mypy cause abc.Sequence don't implement __mul__

def double(x: abc.Sequence):
    return x * 2
