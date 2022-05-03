from py_euler import thirteen

ANSWER = "5537376230"
TOTAL = "5537376230390876637302048746832985971773659831892672"


def test_sum_numbers() -> None:
    assert TOTAL == thirteen.sum_numbers(thirteen.NUMBERS)


def test_solve_problem() -> None:
    assert ANSWER == thirteen.solve_problem(thirteen.NUMBERS)
