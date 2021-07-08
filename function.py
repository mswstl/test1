#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    x=5
    kitten(x)
    print(f'in main, x is {x}')

def kitten(n):
    n=3
    print('Meow.')
    print(n)
if __name__ == '__main__': main()
