"""Add two numbers."""


def suma(*numbers) -> int:
    result = 0
    for number in numbers:
        result += number
    print(result)


suma(2, 5)
suma(2, 5, 6, 7, 8, 9, 10)
suma(2, 3, 4, 5, 6)
