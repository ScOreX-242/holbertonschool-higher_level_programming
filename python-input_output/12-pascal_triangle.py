#!/usr/bin/python3
"""Module that generates Pascal's triangle."""


def pascal_triangle(n):
    """Returns Pascal's triangle with n rows."""
    triangle = []

    if n <= 0:
        return triangle

    for i in range(n):
        new_row = [1] * (i + 1)

        if i >= 2:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                new_row[j] = prev_row[j - 1] + prev_row[j]

        triangle.append(new_row)

    return triangle
