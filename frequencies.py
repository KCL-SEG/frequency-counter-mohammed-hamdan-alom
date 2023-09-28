"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

from collections import defaultdict


def frequencies(items):
    frequencies = {}

    map = defaultdict(int)

    for item in items:
        map[str(item)] += 1

    frequencies = map

    return frequencies

