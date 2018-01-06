from datetime import timedelta


def trim_microseconds(t):
    return t - timedelta(microseconds=t.microsecond)