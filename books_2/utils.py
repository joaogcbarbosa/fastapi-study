from data import books


def increment_id() -> int:
    return books[-1].id + 1
