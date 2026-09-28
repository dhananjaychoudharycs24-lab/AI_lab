def depth_limited_search(state, goal, limit, path):

    if state == goal:
        return path + [state]

    if limit == 0:
        return None

    blank = state.index(0)
    row, col = divmod(blank, 3)

    moves = []

    if row > 0:
        moves.append(blank - 3)      # Up

    if row < 2:
        moves.append(blank + 3)      # Down

    if col > 0:
        moves.append(blank - 1)      # Left

    if col < 2:
        moves.append(blank + 1)      # Right

    for new_blank in moves:

        new_state = state.copy()

        # Move blank
        new_state[blank], new_state[new_blank] = \
            new_state[new_blank], new_state[blank]

        # Avoid states already in current path
        if new_state not in path:

            result = depth_limited_search(
                new_state,
                goal,
                limit - 1,
                path + [state]
            )

            if result is not None:
                return result

    return None


def ids(start, goal):

    depth = 0

    while True:

        print("Searching at depth:", depth)

        result = depth_limited_search(
            start,
            goal,
            depth,
            []
        )

        if result is not None:
            return result

        depth += 1


# Initial state
start = [
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
]

# Goal state
goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

solution = ids(start, goal)

print("\nIDS Solution")
print("Number of moves:", len(solution) - 1)

for i, state in enumerate(solution):

    print("\nStep", i)

    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])
