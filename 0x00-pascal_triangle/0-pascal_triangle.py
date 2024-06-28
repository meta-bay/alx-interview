#!/usr/bin/python3
"""
Pascal Triangle
"""


def pascal_triangle(n):
    """ Returns Pascal Triangle list """
    trig = []
    if n <= 0:
        return trig

    for i in range(n):
        if i == 0:
            row = [i + 1]
            trig.append(row)
        if i == 1:
            row = [i, i]
            trig.append(row)
            priv_row = row

        if i > 1:
            new_row = [priv_row[i] + priv_row[i + 1]
                       for i in range(len(priv_row)) if i + 1 < len(priv_row)]
            new_row = [1] + new_row + [1]
            trig.append(new_row)
            priv_row = new_row

    return trig
