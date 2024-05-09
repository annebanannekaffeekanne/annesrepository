from math import sqrt
import pytest


# multiples of 3 or 5
# Find the sum of all the multiples of 3 or 5 below 1000.
def problem1(n):
    list = []  # empty list
    sum = 0  # sets variable sum = 0
    for i in range(0, n - 1):
        list.append(i)  # creates list with numbers from 0 to 999
        if list[i] // 3 or list[i] // 5:  # checks if listindex is a multiple of 3 or 5
            sum += list[i]  # if it is, the listindex is added to the sum
    print(sum)


problem1(1000)


# even ficonacci numbers
# By considering the terms in the Fibonacci sequence whose values
# do not exceed four million, find the sum of the even-valued terms.
def problem2(n):
    a = 0
    b = 1
    list = []  # empty list
    sum = 0
    if n < 4000000:  # upper border 4 mio
        for i in range(n):
            c = a + b  # fibonacci-algorithm
            a = b
            b = c
            if b % 2 == 0:  # selects the even numbers
                list.append(b)  # adds them to the list
                sum += b  # adds value to the sum
        print(list)
        print(sum)


problem2(10)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# largest prime factor
# What is the largest prime factor of n?
def problem3(n):
    primes = []  # empty list
    for i in range(2, n):
        if is_prime(i):  # checks if it is a prime number
            primes.append(i)  # if it is it adds the number to the list
    # print(primes)
    list = []  # new empty list
    for j in range(len(primes)):  # runs through the prime numbers
        if n % primes[j] == 0:  # checks if the number is divisible by one of the primes
            list.append(primes[j])  # if it is, it is added to the list
    print(max(list))  # returns the highest number of the list = largest prime factor


problem3(13546)


# largest palindrome product
# Find the largest palindrome made from the product of two 3-digit numbers.
def is_palindromic(n):
    return str(n) == str(n)[::-1]


def problem4(m, n):  # m= lower border, n = upper border
    max_palindrome = 0  # set variable = 0
    for i in range(m, n):  # first number to the last
        for j in range(m, n):
            product = i * j
            if is_palindromic(product) and is_palindromic(product) > max_palindrome:
                max_palindrome = product
    print(max_palindrome)


problem4(100, 1000 - 1)  # 3-digit, upper and lower border

if __name__ == '__projecteuler__':
    pytest.projecteuler()
