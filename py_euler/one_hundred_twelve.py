"""
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


def __assess_direction(cur_num: str, next_num: str, direction: Optional[str]) -> str:
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


def is_number_bouncy(number: int) -> bool:
    # TODO try to rewrite this as iterative instead of recursive
    def record_bounce(
        cur_num: str, next_num: str, direction: Optional[str], remainders: [str] = None
    ) -> bool:
        cur_next_comparison = __assess_direction(cur_num, next_num, direction)

        if direction != cur_next_comparison and direction is not None:
            return True  # direction changed, so it's bouncy

        if len(remainders) == 0:
            return False  # no more numbers

        return record_bounce(
            next_num, remainders.pop(), cur_next_comparison, remainders
        )

    num_str = list(number.__str__())
    num_str_len = len(num_str)

    if num_str_len in [1]:
        return False

    num_str.reverse()

    return record_bounce(num_str.pop(), num_str.pop(), None, num_str)


def count_bouncy_numbers(numbers: [int]) -> int:
    bouncy_nums = list(filter(lambda n: is_number_bouncy(n), numbers))
    return len(bouncy_nums)


if __name__ == "__main__":
    for n in [134468, 66420, 155349]:
        is_number_bouncy(n)
