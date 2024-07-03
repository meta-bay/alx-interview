#!/usr/bin/python3
"""
Open boxes.
"""


def canUnlockAll(boxes):
    """ Unlock Boxes """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False
