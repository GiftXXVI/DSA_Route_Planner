# Britannica, The Editors of Encyclopaedia. "distance formula". Encyclopedia Britannica, 29 Jan. 2015, #https://www.britannica.com/science/distance-formula. Accessed 7 February 2022.
# Square root of√(a − c)2 + (b − d)2
import math
from multiprocessing.dummy import current_process
import Heap


class Node(object):
    def __init__(self, index, cost):
        self.index = index
        self.cost = cost


def distance(origin, destination):
    delta_x = (origin[0] - destination[0])**2
    delta_y = (origin[1] - destination[1])**2
    return math.sqrt(delta_x + delta_y)


def build_path(priors, current):
    keys = set(priors.keys())
    values = set(priors.values())
    diff = keys.difference(values)
    find = diff.pop()
    result = list()
    while priors[find]:
        result.append(find)
        find = priors[find]

    return result


def shortest_path(M, start, goal):
    h_function = dict()
    h_function[start] = distance(M.intersections[start], M.intersections[goal])

    o_set = Heap.MinHeap(len(M.intersections))
    # check if heuristic/cost function to be used here
    n_start = Node(start, h_function[start])
    o_set.insert(n_start)

    priors = dict()

    c_function = {key: math.inf for key in M.roads}
    c_function[start] = 0

    while o_set.get_size() > 0:
        current = o_set.extract_min()  # heuristic/cost function choice critical here
        if current == goal:
            return build_path(priors, current)

        for neighbor in range(len(M.roads[current])):
            cost = c_function[current] + \
                distance(M.intersections[current], M.intersections[neighbor])
            if cost < c_function[neighbor]:
                priors[neighbor] = current
                c_function[neighbor] = cost
                h_function[neighbor] = c_function[neighbor] + \
                    distance(M.intersections[neighbor], M.intersections[goal])
                if neighbor not in o_set.keys:
                    # heuristic/cost function choice critical here
                    n_neighbor = Node(neighbor, h_function[neighbor])
                    o_set.insert(n_neighbor)

    return []
