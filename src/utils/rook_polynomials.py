# pylint: disable=C0114, C0115, C0116, C0301


def get_available_rook_configs(
        rows: int,
        cols: int,
        forbidden_positions: list[tuple[int, int]],
        rooks_count: int,
):
    """
    This function returns all available configurations of rooks on an m x n board
    for a given number of rooks and a list of forbidden squares.
    """

    return _get_available_rook_configs_helper(
        0,
        0,
        rows,
        cols,
        forbidden_positions,
        [],
        [],
        rooks_count,
    )


def _get_available_rook_configs_helper(
        i: int,
        j: int,
        rows: int,
        cols: int,
        forbidden_positions: list[tuple[int, int]],
        reserved_rows: list[int],
        reserved_cols: list[int],
        rooks_count: int,
) -> list[list[tuple[int, int]]] | None:
    # configuration of given size found
    if rooks_count == 0:
        return []

    # configuration of given size cannot be found
    if i >= rows:
        return None

    next_i = i
    next_j = (j + 1) % cols
    if next_j == 0:
        next_i += 1

    # skip forbidden squares and reserved rows and columns
    if i in reserved_rows or j in reserved_cols or (i, j) in forbidden_positions:
        return _get_available_rook_configs_helper(
            next_i,
            next_j,
            rows,
            cols,
            forbidden_positions,
            reserved_rows,
            reserved_cols,
            rooks_count,
        )

    res = []

    # include current square
    if rooks_count == 1:
        res = [[(i, j)]]
    else:
        included = _get_available_rook_configs_helper(
            next_i,
            next_j,
            rows,
            cols,
            forbidden_positions,
            reserved_rows + [i],
            reserved_cols + [j],
            rooks_count - 1,
        )

        if included is not None:
            for conf in included:
                res.append([(i, j)] + conf)

    # exclude current square
    excluded = _get_available_rook_configs_helper(
        next_i,
        next_j,
        rows,
        cols,
        forbidden_positions,
        reserved_rows,
        reserved_cols,
        rooks_count,
    )

    if excluded is not None:
        res += excluded

    return res
