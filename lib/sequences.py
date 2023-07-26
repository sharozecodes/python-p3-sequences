#!/usr/bin/env python3

def print_fibonacci(n):
    if n == 0:
        print([])
    elif n == 1:
        print([0])
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        print(fib_seq)