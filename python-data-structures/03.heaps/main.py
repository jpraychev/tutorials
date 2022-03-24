class Heap():

    def __init__(self):
        self.heap = [0]
        self.size = 0

    def add(self, data):
        try:
            if isinstance(data, str) or data < 1:
                raise ValueError('Function accepts only positive numbers!')
            else:
                self.heap.append(data)
                self.size += 1
                self._float(self.size)
        except ValueError as err:
            print(err)
    
    def _float(self, current):

        parent = current // 2

        if self.heap[current] > self.heap[parent]:
            return
        self._swap(current, parent)
        self._float(parent)

    def pop(self):

        try:
            self._swap(self.size, 1)
            last_element = self.heap.pop(self.size)
            self.size -= 1
            self._pop(1)
            return last_element

        except Exception:
            print(f'No items have been added to the heap!')

    def _pop(self, current_index):

        left = current_index * 2
        right = current_index * 2 + 1

        # We have no left children. Return.
        if left > self.size:
            return
        # We have not right child.
        elif right > self.size:
            index = left
        elif self.heap[left] > self.heap[right]:
            index = right
        else:
            index = left

        if self.heap[current_index] > self.heap[index]:
            self._swap(current_index, index)
            self._pop(index)
        return

    def _swap(self, f_index, s_index):
        self.heap[f_index], self.heap[s_index] = self.heap[s_index], self.heap[f_index] 
    
    def peek(self):
        return self.heap[1]

    def xprint(self):
        print(self.heap[1:])

heap = Heap()

heap.add(5)
heap.add(7)
heap.add(7)
heap.add(10)
heap.add(11)
heap.add(9)

print(heap.pop())

heap.xprint()


lists = [1, 'adasd', '-1']

print(lists)
