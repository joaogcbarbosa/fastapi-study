from data import books


def increment_id() -> int:
    return 1 if len(books) == 0 else books[-1].id + 1
