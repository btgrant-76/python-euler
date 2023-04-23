from py_euler import thirteen as test_me

ANSWER = "5537376230"
TOTAL = "5537376230390876637302048746832985971773659831892672"


def test_sum_numbers() -> None:
    assert TOTAL == test_me.sum_numbers(test_me.NUMBERS)


def test_solve_problem() -> None:
    assert ANSWER == test_me.solve_problem(test_me.NUMBERS)
