"""
Answer Sheet
@author: Alireza Kadivar
@author: Aryan Ahadinia
@author: Roxana Khbbaz-Zadeh Moghaddam
"""

import random

##############################################

# 1. Immediate Action


def to_seconds(time: str):
    h, m, s = map(int, time.split(':'))
    return (h * 60 * 60) + (m * 60) + s


def time_calculate(times: list):
    if to_seconds(times[1]) - to_seconds(times[0]) < 7 * 60:
        return 0
    return 1


##############################################

# 2. Graph (a)


def visit_nodes(edges: list, current_node: str, visited_nodes: set):
    for edge in edges:
        if current_node in edge:
            if edge[0] == current_node:
                if edge[1] not in visited_nodes:
                    visited_nodes.add(edge[1])
                    visited_nodes = visit_nodes(edges, edge[1], visited_nodes)
            else:
                if edge[0] not in visited_nodes:
                    visited_nodes.add(edge[0])
                    visited_nodes = visit_nodes(edges, edge[0], visited_nodes)
    return visited_nodes


def node_sets(edges: list):
    nodes = set()
    for e in edges:
        for n in e:
            nodes.add(n)
    return nodes


def is_connected(edges: list):
    return len(visit_nodes(edges, edges[0][0], set())) == len(node_sets(edges))


# 2. Graph (b)


def get_degree(edges: list, node: str):
    connected_vertexes = set()
    for e in edges:
        if node in e:
            connected_vertexes.add(e[0])
            connected_vertexes.add(e[1])
    return len(connected_vertexes) - 1


def remove_redundant_edges(edges: list):
    edges_set = set()
    for e in edges:
        if e not in edges_set and (e[1], e[0]) not in edges_set:
            edges_set.add(e)
    return list(edges_set)


def is_feasible(edges: list):
    edges = remove_redundant_edges(edges) # Arbitary
    if not is_connected(edges):
        return False
    for node in node_sets(edges):
        if get_degree(edges, node) % 2 != 0:
            return False
    return True


## 2. Graph (c)


def a_complete_circuit_recursive(virgin_edges: list, visited_nodes: list,
                                 current_node: str):
    for e in virgin_edges:
        if current_node in e:
            another_node = e[0]
            if e[0] == current_node:
                another_node = e[1]
            new_virgin = virgin_edges[:]
            new_visited = visited_nodes[:]
            new_virgin.remove(e)
            new_visited.append(another_node)
            after_vigin, after_visited = a_complete_circuit_recursive(
                new_virgin, new_visited, another_node)
            if len(after_vigin) == 0:
                return [], after_visited
    return virgin_edges, visited_nodes


def a_complete_circuit(edges: list):
    if not is_feasible(edges):
        return []
    edges = remove_redundant_edges(edges)  # Arbitary
    _, circut = a_complete_circuit_recursive(edges, [], edges[0][0])
    circut.append(circut[0])
    return circut


###############################################

# 3. Sale Estimation


def sale_simulate(pref_morning, pref_evening, unit_price):
    dist_morning = 5
    dist_evening = 2
    N = 700
    TotalSale = []
    for j in range(N):
        sale = {}
        for item in unit_price:
            sale[item] = 0
        total_sale = 0
        itemset_morning = []
        for item in pref_morning:
            for _ in range(pref_morning[item]):
                itemset_morning.append(item)
        itemset_evening = []
        for item in pref_evening:
            for _ in range(pref_evening[item]):
                itemset_evening.append(item)
        for _ in range(30):
            time = 0
            while time <= 6 * 60:
                time += random.random() * dist_morning
                sale[random.choice(itemset_morning)] += 1
            time = 0
            while time <= 6 * 60:
                time += random.random() * dist_evening
                sale[random.choice(itemset_evening)] += 1
        for item in unit_price:
            total_sale += sale[item] * unit_price[item]
        # print(str(round(100 * j / N, 1)) + '%')
        TotalSale.append(total_sale)
    return sum(TotalSale) / len(TotalSale)


###############################################

# 4. Covid19


def to_float(val: str):
    return float(val.replace('/', '.'))


def test_result(test: dict):
    c = 0
    if test['PCR'] == 'positive':
        c += 1
    if to_float(test['IgM']) >= 1.1:
        c += 1
    if to_float(test['IgG']) >= 1.1:
        c += 1
    return c >= 2


def model_accuracy(tests: dict):
    e = 0
    for k in tests.keys():
        if test_result(tests[k]) ^ (tests[k]['trueStatus'] == 'Carrier'):
            e += 1
    return 1 - (e / len(tests))
