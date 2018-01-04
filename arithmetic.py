"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""

    return num1 + num2


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return num1 - num2


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return num1 * num2


def divide(num1, num2):
    """Divide the first input by the second and return the result."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    return num1 ** 2


def cube(num1):
    """Return the cube of the input."""

    return num1 ** 3


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return num1 ** num2


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return num1 % num2

def add_mult(num1, num2, num3):
    """Adds the first two and multiples sum with third"""

    return (num1 + num2) * num3

def add_cubes(num1, num2):
    """Cubes two numbers and returns the sum of the cubes"""

    return num1 ** 3 + num2 ** 3

print add(1, 2)
print subtract(10, 5)
print multiply(3, 4)
print divide(10, 2)
print square(5)
print cube(2)
print power(3, 2)
print mod(10, 3)
print add_mult(1, 2, 3)
print add_cubes(2, 3)