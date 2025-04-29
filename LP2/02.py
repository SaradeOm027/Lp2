from copy import deepcopy

def print_board(state):
    for i in range(9):
        if i % 3 == 0:
            print()
        print("_" if state[i] == -1 else state[i], end=" ")
    print("\n")

def is_solvable(puzzle):
    inv = 0
    flat_puzzle = [x for x in puzzle if x != -1]
    for i in range(len(flat_puzzle)):
        for j in range(i + 1, len(flat_puzzle)):
            if flat_puzzle[i] > flat_puzzle[j]:
                inv += 1
    return inv % 2 == 0

def manhattan_distance(current, goal):
    distance = 0
    for num in range(1, 9):
        current_index = current.index(num)
        goal_index = goal.index(num)
        distance += abs(current_index // 3 - goal_index // 3)
        distance += abs(current_index % 3 - goal_index % 3)
    return distance

def get_neighbors(state):
    neighbors = []
    index = state.index(-1)
    row, col = divmod(index, 3)

    def swap_and_add(new_idx):
        new_state = state[:]
        new_state[index], new_state[new_idx] = new_state[new_idx], new_state[index]
        neighbors.append(new_state)

    if col > 0:
        swap_and_add(index - 1)  # left
    if col < 2:
        swap_and_add(index + 1)  # right
    if row > 0:
        swap_and_add(index - 3)  # up
    if row < 2:
        swap_and_add(index + 3)  # down

    return neighbors

def solve(start, goal):
    from heapq import heappush, heappop

    visited = set()
    heap = []
    heappush(heap, (manhattan_distance(start, goal), 0, start, []))  # (f, g, state, path)

    while heap:
        f, g, current, path = heappop(heap)
        state_tuple = tuple(current)

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if current == goal:
            full_path = path + [current]
            for step in full_path:
                print_board(step)
            print(f"Solved in {len(full_path) - 1} moves.")
            return

        for neighbor in get_neighbors(current):
            if tuple(neighbor) not in visited:
                heappush(heap, (manhattan_distance(neighbor, goal) + g + 1, g + 1, neighbor, path + [current]))

    print("No solution found.")

def main():
    print("Enter the start state (use -1 for empty):")
    start = [int(input(f"Position {i+1}: ")) for i in range(9)]

    print("Enter the goal state (use -1 for empty):")
    goal = [int(input(f"Position {i+1}: ")) for i in range(9)]

    print("\nStart State:")
    print_board(start)

    if not is_solvable(start):
        print("This puzzle configuration is not solvable.")
        return

    print("Solving...\n")
    solve(start, goal)

if __name__ == "__main__":
    main()
