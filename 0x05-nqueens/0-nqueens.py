#!/usr/bin/python3
'''Nqueens'''
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])

def NQsearch():
    """find possible solutions"""
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from NQsearch(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

def solve(n):
    """ solve """
    k = []
    i = 0
    for solution in search(n, 0):
        for s in solution:
            k.append([i, s])
            i += 1
        print(k)
        k = []
        i = 0

