import heapq


class BidirectionalPriorityQueue:
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
    
def reconstruct_bidirectional_path(forward_came_from, backward_came_from, start, goal, intersection_node):
    # Reconstruct the bidirectional path from start to goal through the intersection node
    forward_path = []
    current = intersection_node
    while current != start:
        forward_path.append(current)
        current = forward_came_from[current]

    backward_path = []
    current = intersection_node
    while current != goal:
        backward_path.append(current)
        current = backward_came_from[current]

    forward_path.reverse()
    path = [start] + forward_path + backward_path + [goal]
    return path

def heuristic(a, b):
    # Calculate and return the Manhattan distance heuristic between two points
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def bidirectional_a_star_search(graph, start, goal):
    # Initialize the forward and backward frontiers, dictionaries to store forward, backward came_from and forward, backward cost_so_far
    forward_frontier = BidirectionalPriorityQueue()
    backward_frontier = BidirectionalPriorityQueue()
    forward_frontier.put(start, 0)
    backward_frontier.put(goal, 0)
    forward_came_from = {start: None}
    backward_came_from = {goal: None}
    forward_cost_so_far = {start: 0}
    backward_cost_so_far = {goal: 0}
    intersection_node = None

    # Continue the search until one of the frontiers becomes empty or an intersection is found
    while not forward_frontier.empty() and not backward_frontier.empty():
        forward_current = forward_frontier.get()
        backward_current = backward_frontier.get()

        if forward_current in backward_came_from:
            intersection_node = forward_current
            break

        # Explore neighbors in the forward direction
        for next_node in graph.neighbors(forward_current):
            new_cost = forward_cost_so_far[forward_current] + graph.cost(forward_current, next_node)
            if next_node not in forward_cost_so_far or new_cost < forward_cost_so_far[next_node]:
                forward_cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(next_node, goal)
                forward_frontier.put(next_node, priority)
                forward_came_from[next_node] = forward_current

        if backward_current in forward_came_from:
            intersection_node = backward_current
            break

        # Explore neighbors in the backward direction
        for prev_node in graph.neighbors(backward_current):
            new_cost = backward_cost_so_far[backward_current] + graph.cost(prev_node, backward_current)
            if prev_node not in backward_cost_so_far or new_cost < backward_cost_so_far[prev_node]:
                backward_cost_so_far[prev_node] = new_cost
                priority = new_cost + heuristic(prev_node, start)
                backward_frontier.put(prev_node, priority)
                backward_came_from[prev_node] = backward_current

    return forward_came_from, backward_came_from, intersection_node

