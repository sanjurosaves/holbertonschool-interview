#!/usr/bin/python3


def addKey(key, keyset, boxes):
    if key > 0:
        keyset.add(key)


def canUnlockAll(boxes):
    if ((type(boxes) is not list) or (not boxes)):
        return(False)

    keyset = set()

    for box, keys in enumerate(boxes):
        if ((box in keyset) or (box == 0)):
            for key in keys:
                addKey(key, keyset, boxes)
        if box not in keyset:
            for nextbox, nextboxkeys in enumerate(boxes[(box + 1):(len(boxes))]):
                nextboxindex = 1 + box + nextbox
                if nextboxindex in keyset:
                    keyset.update(nextboxkeys)
        if ((box not in keyset) and (box != 0)):
            return(False)

    return(True)