"""
https://projecteuler.net/problem=112

Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called
a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.
"""
from typing import Optional


def is_bouncy_by_recursion(number: int) -> bool:
    def assess_direction(cur_num: str, next_num: str, direction: Optional[str]) -> str:
        cur_int = int(cur_num)
        next_int = int(next_num)

        cur_next_comparison = None

        if cur_int > next_int:
            cur_next_comparison = "dec"
        elif cur_int < next_int:
            cur_next_comparison = "inc"

        # no direction had been detected prior to this
        if cur_next_comparison is None and direction is not None:
            cur_next_comparison = direction

        return cur_next_comparison

    def record_bounce(
        cur_num: str, next_num: str, direction: Optional[str], remainders: [str] = None
    ) -> bool:
        cur_next_comparison = assess_direction(cur_num, next_num, direction)

        if direction != cur_next_comparison and direction is not None:
            return True  # direction changed, so it's bouncy

        if len(remainders) == 0:
            return False  # no more numbers

        return record_bounce(
            next_num, remainders.pop(), cur_next_comparison, remainders
        )

    num_str = list(number.__str__())
    num_str_len = len(num_str)

    if num_str_len in [1, 2]:
        return False

    return record_bounce(num_str.pop(), num_str.pop(), None, num_str)


def is_bouncy_by_list_comparison(number: int) -> bool:
    num_str = list(number.__str__())
    num_str_len = len(num_str)

    if num_str_len in [1, 2]:
        return False

    sorted_num_str = sorted(num_str)

    if sorted_num_str == num_str:
        return False  # increasing

    sorted_num_str.reverse()
    if sorted_num_str == num_str:
        return False  # decreasing

    return True


is_bouncy = is_bouncy_by_list_comparison  # is_number_bouncy_recursively


def find_number_with_bouncy_percentage(percent: int) -> int:
    test_number = 0
    numbers_tested = 0
    bouncy_count = 0

    while True:
        test_number += 1
        number_bounces = is_bouncy(test_number)
        numbers_tested += 1

        if number_bounces:
            bouncy_count += 1
            percent_bouncy_numbers = int((bouncy_count / numbers_tested) * 100)
            if percent_bouncy_numbers == percent:
                return test_number


if __name__ == "__main__":
    percentage = 99
    number_with_percentage = find_number_with_bouncy_percentage(percentage)
    print(f"{percentage}% of the numbers under {number_with_percentage} are bouncy")
