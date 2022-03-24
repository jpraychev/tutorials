class Node():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)

class Tree():

    def __init__(self):
        self.root = None

    def add(self, data):
        # If tree is empty
        if self.root == None:
            self.root = Node(data)
        else:
            self._add(self.root, data)

    def _add(self, current_node, data):
        if data > current_node.data:
            if current_node.right == None:
                current_node.right = Node(data)
                current_node.right.parent = current_node
            else:
                self._add(current_node.right, data)
        elif data < current_node.data:
            if current_node.left == None:
                current_node.left = Node(data)
                current_node.left.parent = current_node
            else:
                self._add(current_node.left, data)
        else:
            print('Item already in tree') 

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, current_node):
        if current_node.left == None:
            return current_node
        return self._find_min(current_node.left)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, current_node):
        if current_node.right == None:
            return current_node
        return self._find_max(current_node.right)

    def left_height(self):
        if self.root == None:
            return 0
        return self._left_height(self.root, 0)
    
    def _left_height(self,current_node,current_height):
        if current_node == None: 
            return current_height
        return self._left_height(current_node.left,current_height + 1)

    def right_height(self):
        if self.root == None:
            return 0
        return self._right_height(self.root, 0)
    
    def _right_height(self,current_node,current_height):
        if current_node == None: 
            return current_height
        return self._right_height(current_node.right,current_height + 1)        

    def search(self, data):
        if self.root == None:
            return None
        return self._search(self.root, data)

    def _search(self, current_node, data):

        if current_node.data == data:
            return current_node
        elif current_node.data < data and current_node.right != None:
            return self._search(current_node.right, data)
        elif current_node.data > data and current_node.left != None:
            return self._search(current_node.left, data)            

    def remove(self, data):
        node = self.search(data)
        parent = node.parent

        # Case 0 - node has no children
        if node.left == None and node.right == None:
            if parent.left == node: 
                parent.left = None
            elif parent.right == node:
                parent.right = None
                
        # Case 1 - node has two children
        elif node.left != None and node.right != None:
            min_node = self._find_min(node.right)
            parent_min_node = min_node.parent
            node.data = min_node.data
            if min_node.left == None and min_node.right == None:
                if parent_min_node.left == min_node:
                    parent_min_node.left = None
                elif parent_min_node.right == min_node:
                    parent_min_node.right = None
            elif parent_min_node.left == min_node:
                parent_min_node.left = min_node.right
            elif parent_min_node.right == min_node:
                parent_min_node.right = min_node.right

        # Case 2 - node has only one child
        else:
            if parent.left == node:
                if node.left:
                    parent.left = node.left
                elif node.right:
                    parent.left = node.right
                node = None
            elif parent.right == node:
                if node.left:
                    parent.right = node.left
                elif node.right:
                    parent.right = node.right
                node = None 
                
    def invert_tree(self):
        return self._invert_tree(self.root)

    def _invert_tree(self, root):
        # Base case
        if not root.left or root.right:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self._invert_tree(root.left)
        self._invert_tree(root.right)
    
    def xprint(self):
        self._xprint(self.root)

    def _xprint(self, current_node):
        if current_node is None:
            return
        self._xprint(current_node.left)
        print(current_node)
        self._xprint(current_node.right)
        

# tree = Tree()

# tree.add(1)
# tree.add(2)


# print(tree.right_height())
# tree.add(50)
# tree.add(30) 
# tree.add(20) 
# tree.add(40) 
# tree.add(70) 
# tree.add(60) 
# tree.add(80)
# tree.add(90)
# tree.add(100)
# tree.add(110)
# tree.add(35)
# tree.add(95)
# tree.add(15)
# tree.add(85)
# tree.add(96)
# tree.add(36)


