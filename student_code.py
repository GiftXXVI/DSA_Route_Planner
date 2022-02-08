import math
import Heap


class Node(object):
    def __init__(self, index, cost):
        self.index = index
        self.cost = cost

    def __repr__(self) -> str:
        return f'<Node {self.index}-->{self.cost}>'

# From https://www.britannica.com/science/distance-formula. Accessed 7
# February 2022.


def distance(origin, destination) -> float:
    delta_x = (origin[0] - destination[0])**2
    delta_y = (origin[1] - destination[1])**2
    return math.sqrt(delta_x + delta_y)

# From https://en.wikipedia.org/wiki/A*_search_algorithm. Accessed 7
# February 2022.


def build_path(priors, current, start) -> list:
    result = list()
    curr = current.index
    result.append(curr)
    while curr != start:
        result.append(priors[curr])
        curr = priors[curr]
    result.reverse()
    return result


def shortest_path(M, start, goal) -> list:
    keys = M.intersections.keys()
    o_set = Heap.MinHeap(len(keys))

    priors = dict()

    # c_function is short for cost function - distance from start
    c_function = {key: math.inf for key in keys}
    c_function[start] = 0

    # h_function is short for heuristic function - estimated distance to goal
    h_function = {key: math.inf for key in keys}
    h_function[start] = distance(M.intersections[start], M.intersections[goal])

    n_start = Node(start, c_function[start] + h_function[start])
    o_set.insert(n_start)

    solutions = dict()

    while o_set.get_size() > 0:
        current = o_set.extract_min()
        if current.index == goal:
            cost = c_function[current.index]
            solutions[cost] = build_path(priors, current, start)
            # return build_path(priors, current, start)
        else:
            for neighbor in range(len(M.roads[current.index])):
                # nb_index is short for neighbor index
                nb_index = M.roads[current.index][neighbor]
                cost = c_function[current.index] + distance(
                    M.intersections[current.index], M.intersections[nb_index])
                if cost < c_function[nb_index]:
                    priors[nb_index] = current.index
                    c_function[nb_index] = cost
                    h_function[nb_index] = distance(
                        M.intersections[nb_index], M.intersections[goal])
                    if nb_index not in o_set.keys:
                        n_neighbor = Node(
                            nb_index,
                            c_function[nb_index] +
                            h_function[nb_index])
                        o_set.insert(n_neighbor)
    minimum = min(solutions.keys())
    print(solutions)
    return solutions[minimum]
