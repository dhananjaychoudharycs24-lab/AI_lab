import heapq

# Initial and goal states
initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Calculate Manhattan Distance
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            # Current position
            x1 = i // 3
            y1 = i % 3

            # Goal position
            goal_index = goal.index(state[i])
            x2 = goal_index // 3
            y2 = goal_index % 3

            distance += abs(x1 - x2) + abs(y1 - y2)

    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    # Up, Down, Left, Right
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)

            # Swap empty space with adjacent tile
            new_state[zero], new_state[new_pos] = (
                new_state[new_pos], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def astar(start):
    pq = []

    # (f, g, state, path)
    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):

            if neighbor not in visited:
                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None


# Display the board
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


# Main program
print("Initial State:")
display(initial)

solution = astar(initial)

if solution:
    print("Solution Found!")
    print("Total Moves:", len(solution) - 1)

    for step, state in enumerate(solution):
        print("Step", step)
        display(state)

else:
    print("No solution exists.")
