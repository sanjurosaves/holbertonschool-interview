canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes))

boxes = [[1,3],[3,0,1],[2],[0]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes),  "\t: False")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6], [7]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6], [7]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[2], [3, 4], [1, 5]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [[2]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = []
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1, 2, 3], [], [], [], []]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = None
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = 'hello, is it me you looking for?'
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[0, 4, 4], [5], [3], [1], [2], [5]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [[1, 4], [2], [0, 4, 1], [6], [3], [4, 1], [5, 6], [7]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[1], [1], [1]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[], [2], [4]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [{}, [2, 3], {}, None]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[0, 1], [2, 3], [7, 4], [2]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [{}]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')

boxes = [[2]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: True")
print('-----------------------------')

boxes = [[], [1, 2, 7], [0, 3]]
print('{} {}'.format('boxes = ', boxes))
print(canUnlockAll(boxes), "\t: False")
print('-----------------------------')
