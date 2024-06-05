def depth_first_search(graph, start, goal):
    # Initialize the stack with the starting node
    stack = [start]
    visited = set()
    came_from = {}

    # Explore nodes in the stack
    while stack:
        current = stack.pop()
        if current == goal:
            break
        if current not in visited:
            visited.add(current)

            # Explore neighbors of the current node
            for next_node in graph.neighbors(current):
                if next_node not in visited:
                    stack.append(next_node)
                    came_from[next_node] = current

    return came_from


def reconstruct_path(came_from, start, goal):
    # Reconstruct the path from the goal to the start
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.append(start)
    # Reverse the path to get it from start to goal
    path.reverse()
    return path
