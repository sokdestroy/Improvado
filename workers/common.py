import re


def sorting(unsorted):
    convert = lambda text: int(text) if text.isdigit() else text
    if isinstance(unsorted, dict):
        return dict(sorted(unsorted.items(), key=lambda key: [convert(c) for c in re.split('([0-9]+)', key[0])]))
    return sorted(unsorted, key=lambda key: [convert(c) for c in re.split('([0-9]+)', key)])