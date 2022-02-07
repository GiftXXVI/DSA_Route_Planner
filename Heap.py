class MinHeap(object):
    def __init__(self, size) -> None:
        self.heap = [None for i in range(size)]
        self.size = 0

    def extend(self):
        length = len(self.heap)
        arr = [self.heap[i] for i in range(length)]
        self.heap = [None for i in range(2*length)]
        for i in range(length):
            self.heap[i] = arr[i]

    def get_parent(self, index) -> tuple:
        parent_index = index//2
        return self.heap[parent_index], parent_index

    def get_left_child(self, index) -> tuple:
        left_index = 2*index
        return self.heap[left_index], left_index

    def has_left_child(self, index) -> bool:
        left_index = 2*index
        if self.heap[left_index] is not None:
            return True
        return False

    def get_right_child(self, index) -> tuple:
        right_index = 2*index+1
        return self.heap[right_index], right_index

    def has_right_child(self, index) -> bool:
        right_index = 2*index+1
        if self.heap[right_index] is not None:
            return True
        return False

    def find_min(self) -> Node:
        return self.heap[1]

    def insert(self, node) -> None:
        if self.size == 0:
            self.heap[1] = node
            self.size = 1
            return
        index = self.size + 1
        self.heap[index] = node
        parent, parent_index = self.get_parent(index)
        while node[1] < parent[1]:
            temp = parent
            self.heap[parent_index] = node
            self.heap[index] = parent
            index = parent_index
            if parent_index > 1:
                parent, parent_index = self.get_parent(index)
            else:
                break
        self.size += 1
        if self.size == len(self.heap) - 1:
            self.extend()
        return

    def heapify(self, index):
        self._heapify(index)

    def _heapify(self, index):
        if self.heap[index] is not None:
            if self.has_left_child(index):
                left, left_index = self.get_left_child(index)
                if self.heap[index][1] > left[1]:
                    temp = self.heap[index]
                    self.heap[index] = left
                    self.heap[left_index] = temp
                    self._heapify(left_index)

            if self.has_right_child(index):
                right, right_index = self.get_right_child(index)
                if self.heap[index][1] > right[1]:
                    temp = self.heap[index]
                    self.heap[index] = right
                    self.heap[right_index] = temp
                    self._heapify(right_index)

        return

    def extract_min(self) -> Node:
        node = self.find_min()
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.heapify(1)
        self.size -= 1
        return node

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.get_size() == 0

    def __repr__(self) -> str:
        return str(self.heap)

    def __str__(self) -> str:
        return str(self.heap)