from py_euler import twenty_two as test_me

PARSED_NAMES = [
    "MARY",
    "PATRICIA",
    "LINDA",
    "BARBARA",
    "ELIZABETH",
    "JENNIFER",
    "MARIA",
]

SORTED_NAMES = [
    "BARBARA",
    "ELIZABETH",
    "JENNIFER",
    "LINDA",
    "MARIA",
    "MARY",
    "PATRICIA",
]


def test_score_name() -> None:
    assert 49714 == test_me.score_name("COLIN", 938)


def test_char_vals() -> None:
    assert 1 == test_me.CHAR_VALS.index("A")
    assert 26 == test_me.CHAR_VALS.index("Z")


def test_parse_input() -> None:
    input: str = '"MARY","PATRICIA","LINDA","BARBARA",' '"ELIZABETH","JENNIFER","MARIA"'

    assert PARSED_NAMES == test_me.parse_input(input)


def test_sort_names() -> None:
    assert SORTED_NAMES == test_me.sort_names(PARSED_NAMES)


def test_score_names() -> None:
    scored = [43, 176, 243, 160, 210, 342, 539]

    assert scored == test_me.score_names(SORTED_NAMES)


def test_solve() -> None:
    solution = test_me.solve(test_me.load_names(f"./py_euler/{test_me.INPUT_FILE}"))
    assert solution == 871198282
