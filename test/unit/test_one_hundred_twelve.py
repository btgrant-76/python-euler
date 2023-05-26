from py_euler import one_hundred_twelve as test_me

from pytest import mark


@mark.parametrize(
    "number, is_bouncy",
    [
        (134468, False),
        (66420, False),
        (155349, True),
        (5545, True),
        (545, True),
        (123456789, False),
        (9876543210, False),
        (11111111112, False),
        (5555555553, False),
        (111121, True),
        (555535, True),
    ],
)
# @mark.skip
def test_is_number_bouncy(number: int, is_bouncy: bool) -> None:
    assert is_bouncy == test_me.is_number_bouncy(number)


@mark.parametrize("n", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
def test_single_digit_numbers_are_never_bouncy(n: int) -> None:
    assert test_me.is_number_bouncy(n) is False


@mark.parametrize("n", range(1, 101))
def test_two_digit_numbers_are_never_bouncy(n: int) -> None:
    assert test_me.is_number_bouncy(n) is False


@mark.parametrize("n", [1111, 99, 5555555, 333, 11, 2, 666])
def test_numbers_with_all_the_same_digits_are_never_bouncy(n: int) -> None:
    assert test_me.is_number_bouncy(n) is False


@mark.parametrize(
    "numbers, count",
    [
        (
            [
                134468,
                66420,
                155349,
            ],
            1,
        ),
        (list(range(1, 1000)), 525),
        (
            list(range(1, 21781)),
            19602,
        ),
    ],
)
def test_count_bouncy_numbers(numbers: [int], count: int) -> None:
    assert count == test_me.count_bouncy_numbers(numbers)
