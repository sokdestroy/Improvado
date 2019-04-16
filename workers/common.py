import re


def sorting(unsorted):
    convert = lambda text: int(text) if text.isdigit() else text
    if isinstance(unsorted, dict):
        return dict(sorted(unsorted.items(), key=lambda key: [convert(c) for c in re.split('([0-9]+)', key[0])]))
    return sorted(unsorted, key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)])


def check_for_bad_symbols(some_dict):
    for item in some_dict.items():
        if item[0][0] == 'D':
            if not isinstance(item[1], str):
                return False
        if item[0][0] == 'M':
            if not isinstance(item[1], int):
                return False
    return True