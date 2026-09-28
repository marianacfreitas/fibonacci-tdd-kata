from fibonacci_tdd_kata.core import fibonacci


def test_fibonacci1():
    assert fibonacci(0) == 0


def test_fibonacci2():
    assert fibonacci(1) == 1


def test_fibonacci3():
    assert fibonacci(2) == 1


def test_fibonacci4():
    assert fibonacci(3) == 2
