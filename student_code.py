# Britannica, The Editors of Encyclopaedia. "distance formula". Encyclopedia Britannica, 29 Jan. 2015, #https://www.britannica.com/science/distance-formula. Accessed 7 February 2022.
# Square root of√(a − c)2 + (b − d)2
from math import sqrt
import Heap


def distance(origin, destination):
    delta_x = (origin[0] - destination[0])**2
    delta_y = (origin[1] - destination[1])**2
    return sqrt(delta_x + delta_y)


def shortest_path(M, start, goal):
    h_function = dict()
    h_function[start] = distance(M[start], M[goal])

    o_set = Heap.MinHeap(len(M))
    o_set.append((start, M[start]))

    path = dict()

    c_function = dict()
    c_function[start] = 0

    while o_set.get_size() > 0:
        pass

    print("shortest path called")
    return
