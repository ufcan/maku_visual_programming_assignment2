#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def mini_max_sum(n):
    minsum = 0
    maxsum = 0
    i = 0

    if (len(n) == 5):
        n.sort()

        while True:
            minsum += n[i]
            i += 1
            if (i == 4):
                i = 1
                break

        while True:
            maxsum += n[i]
            i += 1
            if (i == 5):
                break
    else:
        print(-1)
    print(minsum, maxsum)

g = [9,7,5,3,1]

mini_max_sum(g)