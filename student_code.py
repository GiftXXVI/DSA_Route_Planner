#Britannica, The Editors of Encyclopaedia. "distance formula". Encyclopedia Britannica, 29 Jan. 2015, #https://www.britannica.com/science/distance-formula. Accessed 7 February 2022.
# Square root of√(a − c)2 + (b − d)2
from Math import sqrt
import Heap

def distance(origin,destination):
    x = (origin[0]-destination[0])**2
    y = (origin[1]-destination[1])**2
    return sqrt(x+y)
    
def shortest_path(M,start,goal):
    heuristic = distance(M[start],M[goal])
    open_set = Heap.MinHeap(len(M))
    open_set.append((start,M[start]))
    
    print("shortest path called")
    return