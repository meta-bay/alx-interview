#!/usr/bin/python3
'''
UTF-8 Validation module
'''


def validUTF8(data):
    '''
        determines if a given data set represents
        a valid UTF-8 encoding
    '''
    num_bytes = 0
    num1 = 1 << 7
    num0 = 1 << 6

    for byte in data:
        if num_bytes == 0:
            while byte & num1:
                num_bytes += 1
                byte >>= 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & num1) & (not (byte & num2)):
                return True
        num_bytes -= 1
    return num_bytes == 0
