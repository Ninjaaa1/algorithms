graph = {
    "A": {"B": 2, "D": 4},
    "B": {"C": 5, "D": 1},
    "C": {"E": 1},
    "D": {"C": 3, "E": 3},
    "E": {}
} # You can type your own graph here.

def get_the_cheappest_node(costs_dict, the_list_of_parsed_nodes):
    the_cheappest_cost = float("inf")
    the_cheappest_key = None
    for name, cost in costs_dict.items():
        if name not in the_list_of_parsed_nodes and cost < the_cheappest_cost:
            the_cheappest_cost = cost
            the_cheappest_key = name
    return the_cheappest_key

costs = {}
parents = {}
for node in graph.keys():
    costs[node] = float("inf")

parsed_nodes = []
parsing_node = "A"
costs[parsing_node] = 0
parents[parsing_node] = None

while parsing_node:
    for neighbour in graph[parsing_node]:
        if costs[neighbour] > costs[parsing_node] + graph[parsing_node][neighbour]:
            costs[neighbour] = costs[parsing_node] + graph[parsing_node][neighbour]
            parents[neighbour] = parsing_node

    parsed_nodes.append(parsing_node)
    parsing_node = get_the_cheappest_node(costs, parsed_nodes)

for direction,direction_cost in costs.items():
    print(f"Koszt dla {direction} wynosi {direction_cost}.")

    current_direction = direction
    while parents[current_direction]:
        print(current_direction)
        current_direction = parents[current_direction]
    else:
        print(current_direction)