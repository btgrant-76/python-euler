INPUT_FILE = "p022_names.txt"

CHAR_VALS = [
    "",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def solve(input_string: str) -> int:
    parsed_names = parse_input(input_string)
    sorted_names = sort_names(parsed_names)
    name_scores = score_names(sorted_names)

    return sum(name_scores)


def parse_input(names_input: str) -> [str]:
    split_names = names_input.split('","')

    # clean up the remaining quotes
    split_names[0] = split_names[0].lstrip('"')
    split_names[-1] = split_names[-1].rstrip('"')

    return split_names


def sort_names(names: [str]) -> [str]:
    return sorted(names)


def score_names(names: [str]) -> [int]:
    enumerated_names = enumerate(names)

    scored_names = map(lambda x: score_name(x[1], x[0] + 1), enumerated_names)

    return list(scored_names)


def score_name(name: str, name_position) -> int:
    char_scores: [int] = list(map(lambda c: CHAR_VALS.index(c), name))

    return sum(char_scores) * name_position


def load_names(file: str) -> str:
    with open(file, encoding="utf8", mode="r") as names:
        return names.readline()


if __name__ == "__main__":
    print(solve(load_names(INPUT_FILE)))
