graph={}

def add_node(node):
    if node not in graph:
        graph[node]=[]

def add_edges(node1,node2):
    add_node(node1)
    add_node(node2)

    graph[node1].append(node2)
    graph[node2].append(node1)

def display_graph():
    print("Adjacency list:\n")

    for node in graph:
        print(node,"=>",graph[node])

add_edges("A","B")
add_edges("B","C")
add_edges("C","A")
add_edges("B","D")
add_edges("C","D")
add_edges("D","E")
add_edges("D","F")
add_edges("E","F")
add_edges("E","G")
add_edges("F","G")

display_graph()