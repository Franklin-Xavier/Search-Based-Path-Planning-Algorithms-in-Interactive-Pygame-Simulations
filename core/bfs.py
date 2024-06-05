from collections import deque


def breadth_first_search(graph, start, goal):
    # Initialize the frontier with the starting node
    frontier = deque([start])
    came_from = {}
    came_from[start] = None

    # Explore nodes in the frontier
    while frontier:
        current = frontier.popleft()
        if current == goal:
            break
        # Explore neighbors of the current node
        for next in graph.neighbors(current):
            if next not in came_from:
                frontier.append(next)
                came_from[next] = current
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
