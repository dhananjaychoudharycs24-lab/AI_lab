def dfs(start, goal):
    stack = [(start, [])]
    visited = set()

    while stack:
        state, path = stack.pop()

        if state == goal:
            return path + [state]

        state_tuple = tuple(state)

        if state_tuple in visited:
            continue

        visited.add(state_tuple)

        blank = state.index(0)
        row, col = divmod(blank, 3)

        moves = []

        if row > 0:
            moves.append(blank - 3)   # Up
        if row < 2:
            moves.append(blank + 3)   # Down
        if col > 0:
            moves.append(blank - 1)   # Left
        if col < 2:
            moves.append(blank + 1)   # Right

        for new_blank in moves:
            new_state = state.copy()

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            stack.append((new_state, path + [state]))

    return None


# Initial state
start = [
    1, 2, 3,
    4, 00, 6,
    7, 5, 8
]

# Goal state
goal = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
]

solution = dfs(start, goal)

if solution:
    print("DFS Solution:")
    print("Number of moves:", len(solution) - 1)
    print()

    for i, state in enumerate(solution):
        print("Step", i)
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()
else:
    print("No solution found.")
