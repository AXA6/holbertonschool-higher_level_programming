#!/usr/bin/python3
for a in range(10):
    for b in range(a + 1, 10):
        print("{}{}".format(a, b), end=", " if a != 8 or b != 9 else "\n")
