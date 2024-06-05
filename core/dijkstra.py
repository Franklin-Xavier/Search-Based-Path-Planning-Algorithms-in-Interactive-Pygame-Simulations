import heapq


class PriorityQueue:
    def __init__(self):
    # Initialize an empty list to store elements with their priorities
        self.elements = []

    def empty(self):
    # Check if the priority queue is empty
        return len(self.elements) == 0

    def put(self, item, priority):
    # Add an item with its priority to the priority queue using heapq
        heapq.heappush(self.elements, (priority, item))

    def get(self):
    # Remove and return the item with the highest priority from the priority queue
        return heapq.heappop(self.elements)[1]


def dijkstra(graph, start, goal):
    # Initialize the frontier, dictionaries to store came_from and cost_so_far
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    # Explore nodes in the frontier
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        # Explore neighbors of the current node
        for next_node in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next_node)
            # Update if a lower-cost path to 'next' is found
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost
                frontier.put(next_node, priority)
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
