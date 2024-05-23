from erweiterte_programmierkonzepte.practice2 import projecteuler


def test_1_1():
    """
    test input 10
    :return:
    sum of multiples of 3 and 5
    """
    assert projecteuler.problem2("10"), "is 23"


test_1_1()


def test_1_2():
    """
    test input equal 1000
    :return:
    sum of multiples of 3 and 5
    """
    assert projecteuler.problem1("1000"), "233168 is the sum"


test_1_2()


def test_1_3():
    """
    test input is 0
    :return:
    sum is 0
    """
    assert projecteuler.problem1("0") == 0, "grenze null ist null"


test_1_3()


def test_1_4():
    """
    input negativ
    :return:
    sum is 0
    """
    assert projecteuler.problem1("-10") == 0, "negative grenzen ergeben 0"


def test_2_1():
    """
    test 100
    :return:
    sum of even fibonacci numbers
    """
    assert projecteuler.problem2("100"), "44 is the sum"


test_2_1()


def test_2_2():
    """
    test 1
    :return:
    no even numbers, 0
    """
    assert projecteuler.problem2("1") == 0, "no multiples"


test_2_2()


def test_2_3():
    """
    upper border
    :return:
    sum of even fibonacci numbers
    """
    assert projecteuler.problem2("4000000"), "4613732 is the sum"


test_2_3()


def test_2_4():
    """
    negative input
    :return:
    no even numbers for negative input
    """
    assert projecteuler.problem2("-10") == 0, "negative grenzen sind 0"


test_2_4()


def test_3_1():
    """
    test 13195
    :return:
    largest prime factor
    """
    assert projecteuler.problem3("13195"), "29 is the largest prime factor"


test_3_1()


def test_3_2():
    """
    test 1
    :return:
    largest prime factor of 1 is 1 itself
    """
    assert projecteuler.problem3("1"), "1"


test_3_2()


def test_3_3():
    """
    test high number
    :return:
    largest prime factor
    """
    assert projecteuler.problem3("600851475143"), "6857"


test_3_3()


def test_3_4():
    """
    test negative input
    :return:
    largest prime factor
    """
    assert projecteuler.problem3("-10"), "10"


test_3_4()


def test_4_1():
    """
    test 2-digit number
    :return:
    no palindrome
    """
    assert projecteuler.problem4(123), "False"


test_4_1()


def test_4_2():
    """
    test 1-digit number
    :return:
    is palindrome
    """
    assert projecteuler.problem4(101), "True"


test_4_2()


def test_4_3():
    """
    test 90
    :return:
    90 is no 3-digit number
    """
    assert projecteuler.problem4(90) == 0, "False"


test_4_3()


def test_4_4():
    """
    test 1000
    :return:
    1000 is a 4-digit number
    """
    assert projecteuler.problem4(1000) == 0, "False"


test_4_4()
