#!/usr/bin/python3
"""
Log parsing
"""
import sys


def display_stats(file_size, status_code):
    """display the currenct stats"""
    print('File size: {}'.format(file_size))
    for key, val in status_code.items():
        if val != 0:
            print('{}: {}'.format(key, val))


file_size = 0
status_code = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
    '404': 0, '405': 0, '500': 0
}

no_inputs = 0

try:
    for line in sys.stdin:
        ln = line.split()

        if len(ln) > 2:
            no_inputs += 1

            if no_inputs <= 10:
                file_size += int(ln[-1])
                code = ln[-2]

                if (code in status_code.keys()):
                    status_code[code] += 1

            if (no_inputs == 10):
                display_stats(file_size, status_code)
                no_inputs = 0

finally:
    display_stats(file_size, status_code)

