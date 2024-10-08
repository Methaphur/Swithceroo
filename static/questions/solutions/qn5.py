#!/usr/bin/env python
# 
# Solution to Project Euler problem 187
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import  math

def is_prime(x: int) -> bool:
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, math.isqrt(x) + 1, 2):
			if x % i == 0:
				return False
		return True

def list_primality(n: int):
	# Sieve of Eratosthenes
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(math.isqrt(n) + 1):
		if result[i]:
			for j in range(i * i, len(result), i):
				result[j] = False
	return result

def list_primes(n: int):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


# LIMIT is the highest number that we will test for being semiprime.
# Make a list of primes: 2, 3, 5, 7, ... . Stop beyond LIMIT/2, because one of the prime factors in the semiprime is at least 2.
# For each prime p in the list, look at the set of numbers q such that q >= p and pq <= LIMIT.
# Actually, we can stop when p^2 > LIMIT, as we'll see later.
# In this algorithm, we find the index 'end' such that primes[i] * primes[end] > LIMIT.
# So for that p, we have (end - i) different choices for q. Since q >= p, all these pairs are unique.
# Furthermore, by the fundamental theorem of arithmetic, all the products pq are unique.
def compute():
    LIMIT = 10**8 - 1
    ans = 0
    primes = list_primes(LIMIT // 2)
    sqrt = math.isqrt(LIMIT)
    for (i, p) in enumerate(primes):
        if p > sqrt:
            break
        end = binary_search(primes, LIMIT // p)
        ans += (end + 1 if end >= 0 else -end - 1) - i
    return str(ans)


# Given a sorted list and a value, this returns an index i such that lst[i] == x if it exists,
# otherwise this returns (-i - 1) where i is the index that x should be inserted at.
def binary_search(lst, x):
    start = 0
    end = len(lst)
    while start < end:
        mid = (start + end) // 2
        if x < lst[mid]:
            end = mid
        elif x > lst[mid]:
            start = mid + 1
        elif x == lst[mid]:
            return mid
        else:
            raise AssertionError()
    return -start - 1


if __name__ == "__main__":
    print(compute())
