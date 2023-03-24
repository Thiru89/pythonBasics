#!/usr/bin/python3
import sys

# List = [1, 2, 3, 4, 5]
# it = iter(List)
# print(next(it))
# print(next)
#
# for i in List:
#     print(i, end=" ")
#
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit("Complete")


# # Pyramid pattern of numbers
# for i in range(2, 6):
#     for j in range(1, i):
#         print(j, end=' ')
#     print('')
# Number Pattern
# for i in range(0, 6):
#     for j in range(0, i):
#         print(i, end=' ')
#     print('')

# # decreasing Star Pattern
# for i in range (1, 6):
#     for j in range(0, i):
#         print("*", end =' ')
#     print(' ')
# # # Increasing  Star Pattern
# for i in range (1, 6):
#     for j in range(0, i):
#         print("*", end =' ')
#     print(' ')

# # # Reverse increasing Star Pattern
# rows = 6
# columns = 6
# for i in range(1, rows, 1):
#     for j in range(columns, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print("*", end=' ')
#     print('')

# # diagonal star
# rows = 6
# columns = 6
# for i in range(0, rows, 1):
#     for j in range(columns, 0, -1):
#         if i == j:
#             print("*", end=' ')
#         else:
#             print(" ", end=' ')
#     print(" ")
#
# # reverse diagonal
# rows = 6
# columns = 6
# for i in range (0, rows, 1):
#     for j in range(0, columns, 1):
#         if i == j:
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print(' ')

rows = 4
columns = 5
for i in range(1, rows, 1):
    for j in range(2, columns, 1):
        if i % j == 0:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print(' ')
