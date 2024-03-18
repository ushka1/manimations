# pylint: disable=C0114, C0115, C0116, C0301


def get_available_configurations(
        m: int,
        n: int,
        forbidden_squares: list[tuple[int, int]],
        size: int,
):
    return get_available_configurations_helper(
        0,
        0,
        m,
        n,
        forbidden_squares,
        [],
        [],
        size,
    )


def get_available_configurations_helper(
        i: int,
        j: int,
        m: int,
        n: int,
        forbidden_squares: list[tuple[int, int]],
        reserved_rows: list[int],
        reserved_cols: list[int],
        size: int,
) -> list[list[tuple[int, int]]] | None:
    # configuration of given size found
    if size == 0:
        return []

    # configuration of given size cannot be found
    if i >= m:
        return None

    next_i = i
    next_j = (j + 1) % n
    if next_j == 0:
        next_i += 1

    # skip forbidden squares and reserved rows and columns
    if i in reserved_rows or j in reserved_cols or (i, j) in forbidden_squares:
        return get_available_configurations_helper(
            next_i,
            next_j,
            m,
            n,
            forbidden_squares,
            reserved_rows,
            reserved_cols,
            size,
        )

    res = []

    # include current square
    if size == 1:
        res = [[(i, j)]]
    else:
        included = get_available_configurations_helper(
            next_i,
            next_j,
            m,
            n,
            forbidden_squares,
            reserved_rows + [i],
            reserved_cols + [j],
            size - 1,
        )

        if included is not None:
            for conf in included:
                res.append([(i, j)] + conf)

    # exclude current square
    excluded = get_available_configurations_helper(
        next_i,
        next_j,
        m,
        n,
        forbidden_squares,
        reserved_rows,
        reserved_cols,
        size,
    )

    if excluded is not None:
        res += excluded

    return res
