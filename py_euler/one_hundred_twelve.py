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


def is_number_bouncy(number: int) -> bool:
    # if number == 134468:
    #     return False
    #
    # if number == 66420:
    #     return False
    #
    # if number == 155349:
    #     return True

    def record_bounce(cur: str, next: str, dir: str, remainders: [str] = None) -> bool:

        cur_int = int(cur)
        next_int = int(next)

        cur_next_comparison = None

        if cur_int > next_int:
            cur_next_comparison = "dec"
        elif cur_int < next_int:
            cur_next_comparison = "inc"
        # else:
        #     cur_next_comparison = None
        # TODO test numbers with all the same digit
        # TODO test numbers with all but one of the same digit

        if cur_next_comparison is None and dir is not None:
            cur_next_comparison = dir

        if dir != cur_next_comparison and dir is not None:
            return True  # direction changed, so it's bouncy

        if len(remainders) == 0:
            return False  # we've run out of numbers and have not detected bounciness

        return record_bounce(next, remainders.pop(), cur_next_comparison, remainders)

    num_str = list(number.__str__())
    num_str_len = len(num_str)

    if num_str_len in [1]:
        return False

    num_str.reverse()

    # for i in enumerate(num_str):
    #     print(i)

    return record_bounce(num_str.pop(), num_str.pop(), None, num_str)


if __name__ == "__main__":
    for n in [134468, 66420, 155349]:
        is_number_bouncy(n)
