#!/usr/bin/python3
""" Defines the pascal_triangle function"""


def pascal_triangle(n):
    """ A function that returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    if n > 0:
        for i in range(n):
            row = [1]
            if triangle:
                last_row = triangle[-1]
                row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
                row.append(1)
            triangle.append(row)
    return triangle
