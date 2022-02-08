# Britannica, The Editors of Encyclopaedia. "distance formula". Encyclopedia Britannica, 29 Jan. 2015, #https://www.britannica.com/science/distance-formula. Accessed 7 February 2022.
# Square root of√(a − c)2 + (b − d)2
import math
from multiprocessing.dummy import current_process
import Heap


class Node(object):
    def __init__(self, index, cost):
        self.index = index
        self.cost = cost

    def __repr__(self):
        return f'<Node {self.index}-->{self.cost}>'


def distance(origin, destination):
    delta_x = (origin[0] - destination[0])**2
    delta_y = (origin[1] - destination[1])**2
    return math.sqrt(delta_x + delta_y)


def build_path(priors, current, start):
    result = list()
    curr = current.index
    result.append(curr)
    while curr != start:
        result.append(priors[curr])
        curr = priors[curr]

    return result


def shortest_path(M, start, goal):
    keys = M.intersections.keys()
    o_set = Heap.MinHeap(len(keys))

    priors = dict()

    c_function = {key: math.inf for key in keys}
    c_function[start] = 0

    h_function = {key: math.inf for key in keys}
    h_function[start] = distance(M.intersections[start], M.intersections[goal])

    # check if heuristic/cost function to be used here
    n_start = Node(start, c_function[start] + h_function[start])
    o_set.insert(n_start)

    while o_set.get_size() > 0:
        current = o_set.extract_min()  # heuristic/cost function choice critical here
        if current.index == goal:
            return build_path(priors, current, start)

        for neighbor in range(len(M.roads[current.index])):
            nb_index = M.roads[current.index][neighbor]
            cost = c_function[current.index] + \
                distance(M.intersections[current.index], M.intersections[nb_index])
            if cost < c_function[nb_index]:
                priors[nb_index] = current.index
                c_function[nb_index] = cost
                h_function[nb_index] = distance(
                    M.intersections[nb_index], M.intersections[goal])
                if neighbor not in o_set.keys:
                    # heuristic/cost function choice critical here
                    n_neighbor = Node(
                        nb_index,
                        c_function[nb_index] +
                        h_function[nb_index])
                    o_set.insert(n_neighbor)

    return []
