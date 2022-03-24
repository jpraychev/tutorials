from classes import Tree

if __name__ == '__main__':
    
    tree = Tree()

    nodes = [50,70,60,80,30,20,40]

    for node in nodes:
        tree.add(node)

    tree.add(65)
    tree.remove(50)
    tree.xprint()
    # tree.xprint()
    # print(f'Min value: {tree.find_min()}\nMax value: {tree.find_max()}')
    # print(f'Left height: {tree.left_height()}')
    # print(f'Right height: {tree.right_height()}')

    

#       50 
#     /    \
#   30      70
#  /  \    /  \
# 20  40  60  80