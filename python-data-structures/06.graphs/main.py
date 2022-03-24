from classes import Queue 


def breadth_first_search(graph, root):

    main_queue = Queue()
    visited_nodes = list()
    main_queue.enqueue(root)
    visited_nodes.append(root)
    current_node = root
    
    while main_queue.size > 0:
        current_node = main_queue.dequeue()
        adj_nodes = graph[current_node]
        remaining_elements = sorted(set(adj_nodes) - set(visited_nodes))

        if len(remaining_elements) > 0:
            for element in remaining_elements:
                visited_nodes.append(element)
                main_queue.enqueue(element)
    
    return visited_nodes

if __name__ == '__main__':
    
    graph = dict()

    graph['A'] = ['B', 'G', 'D']
    graph['B'] = ['A', 'F', 'E']
    graph['C'] = ['F', 'H']
    graph['D'] = ['F', 'A']
    graph['E'] = ['B', 'G']
    graph['F'] = ['B', 'D', 'C']
    graph['G'] = ['A', 'E']
    graph['H'] = ['C']

    print(breadth_first_search(graph, 'A'))
