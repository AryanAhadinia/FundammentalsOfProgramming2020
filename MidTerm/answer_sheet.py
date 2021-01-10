import random
"""
Answer Sheet

@author: Alireza Kadivar
@author: Aryan Ahadinia
@author: Roxana Khbbaz-Zadeh Moghaddam
"""

##############################################

# 1. Immediate Action


def to_seconds(time: str):
    h, m, s = map(int, time.split(':'))
    return (h * 60 * 60) + (m * 60) + s


def time_calculate(times: list):
    if to_seconds(times[1]) - to_seconds(times[0]) < 7 * 60:
        return 0
    return 1


## function argument example

times = ['20:13:03', '20:19:53']
print(time_calculate(times))  # expected: 0

times = ['20:13:03', '20:22:53']
print(time_calculate(times))  # expected: 1

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


def is_feasible(edges: list):
    if not is_connected(edges):
        return False
    for node in node_sets(edges):
        if get_degree(edges, node) % 2 != 0:
            return False
    return True


## 2. Graph (c)


def remove_redundant_edges(edges: list):
    edges_set = set()
    for e in edges:
        if e not in edges_set and (e[1], e[0]) not in edges_set:
            edges_set.add(e)
    return list(edges_set)


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
    edges = remove_redundant_edges(edges)
    _, circut = a_complete_circuit_recursive(edges, [], edges[0][0])
    circut.append(circut[0])
    return circut


# function argument example

edges = [('b', 'c'), ('c', 'e'), ('a', 'c'), ('c', 'e'), ('f', 'a'),
         ('b', 'd'), ('h', 'e'), ('d', 'c'), ('h', 'c'), ('f', 'c')]
print(is_connected(edges))  # expected: True
print(is_feasible(edges))  # expected: True
print(a_complete_circuit(edges))  # expected: A CIRCUT

edges = [('b', 'c'), ('c', 'e'), ('a', 'c'), ('c', 'e'), ('f', 'a'),
         ('b', 'd'), ('h', 'e'), ('d', 'c'), ('h', 'c'), ('f', 'c'),
         ('d', 'h')]
print(is_connected(edges))  # expected: True
print(is_feasible(edges))  # expected: False
print(a_complete_circuit(edges))  # expected: []

edges = [('c', 'e'), ('a', 'c'), ('c', 'e'), ('f', 'a'), ('b', 'd'),
         ('h', 'e'), ('h', 'c'), ('f', 'c')]
print(is_connected(edges))  # expected: False
print(is_feasible(edges))  # expected: False
print(a_complete_circuit(edges))  # expected: []

edges = [('a', 'c'), ('a', 'b'), ('b', 'c'), ('b', 'd')]
print(is_connected(edges))  # expected: True
print(is_feasible(edges))  # expected: False
print(a_complete_circuit(edges))  # expected: []

###############################################

# 3. Sale Estimation


def get_estimated_customer_count(bound: int, time: int):
    timer = 0
    c = 0
    while True:
        next_customer = random.uniform(0, bound)
        timer += next_customer
        if timer <= time:
            c += 1
        else:
            break
    return c


def get_total(pref: dict):
    total = 0
    for k in pref.keys():
        total += pref[k]
    return total


def get_sell(customers_count: int, pref: dict, prices: dict):
    sell = 0
    total = get_total(pref)
    for k in pref.keys():
        sell += (pref[k] / total) * customers_count * prices[k]
    return sell


def sale_simulate(pref_morning: dict, pref_evening: dict, unit_price: dict):
    days = 1000  # Accuracity
    sell = 0
    for _ in range(days):
        sell += get_sell(get_estimated_customer_count(5, 360), pref_morning,
                         unit_price)
        sell += get_sell(get_estimated_customer_count(2, 360), pref_evening,
                         unit_price)
    return sell * 30 / days


# function argument example

pref_morning = {'A': 3, 'B': 2, 'C': 1, 'D': 1}
pref_evening = {'A': 1, 'B': 2, 'C': 2, 'D': 3}
unit_price = {'A': 12000, 'B': 10000, 'C': 8000, 'D': 9000}
print(sale_simulate(pref_morning, pref_evening,
                    unit_price))  # expected: ~150000000

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


# function argument example

test_results = {
    'p2146': {
        'PCR': 'positive',
        'IgM': "2/07",
        'IgG': "5/10",
        'trueStatus': 'Carrier'
    },
    'p2187': {
        'PCR': 'positive',
        'IgM': "0/70",
        'IgG': "0/10",
        'trueStatus': 'notCarrier'
    },
    'p2143': {
        'PCR': 'negative',
        'IgM': "0/87",
        'IgG': "1/80",
        'trueStatus': 'Carrier'
    },
    'p2142': {
        'PCR': 'negative',
        'IgM': "0/15",
        'IgG': "5/10",
        'trueStatus': 'notCarrier'
    },
    'p2119': {
        'PCR': 'positive',
        'IgM': "2/13",
        'IgG': "3/20",
        'trueStatus': 'Carrier'
    },
    'p2157': {
        'PCR': 'positive',
        'IgM': "9/71",
        'IgG': "0/30",
        'trueStatus': 'notCarrier'
    },
    'p2135': {
        'PCR': 'negative',
        'IgM': "1/07",
        'IgG': "0/18",
        'trueStatus': 'notCarrier'
    },
    'p4657': {
        'PCR': 'negative',
        'IgM': "1/67",
        'IgG': "0/10",
        'trueStatus': 'notCarrier'
    },
    'p4646': {
        'PCR': 'negative',
        'IgM': "0/27",
        'IgG': "0/60",
        'trueStatus': 'notCarrier'
    },
    'p2134': {
        'PCR': 'negative',
        'IgM': "0/75",
        'IgG': "0/09",
        'trueStatus': 'notCarrier'
    },
    'p5348': {
        'PCR': 'negative',
        'IgM': "2/20",
        'IgG': "0/80",
        'trueStatus': 'Carrier'
    },
    'p5341': {
        'PCR': 'negative',
        'IgM': "0/60",
        'IgG': "0/20",
        'trueStatus': 'notCarrier'
    },
    'p5334': {
        'PCR': 'negative',
        'IgM': "0/67",
        'IgG': "1/01",
        'trueStatus': 'notCarrier'
    },
    'p5378': {
        'PCR': 'positive',
        'IgM': "0/07",
        'IgG': "1/11",
        'trueStatus': 'Carrier'
    },
    'p5345': {
        'PCR': 'positive',
        'IgM': "2/17",
        'IgG': "2/10",
        'trueStatus': 'Carrier'
    },
    'p3183': {
        'PCR': 'negative',
        'IgM': "3/07",
        'IgG': "1/00",
        'trueStatus': 'Carrier'
    },
    'p3114': {
        'PCR': 'negative',
        'IgM': "0/88",
        'IgG': "0/55",
        'trueStatus': 'notCarrier'
    },
    'p3123': {
        'PCR': 'positive',
        'IgM': "2/55",
        'IgG': "1/12",
        'trueStatus': 'Carrier'
    },
    'p3115': {
        'PCR': 'negative',
        'IgM': "0/35",
        'IgG': "0/20",
        'trueStatus': 'notCarrier'
    },
    'p3162': {
        'PCR': 'negative',
        'IgM': "0/50",
        'IgG': "0/40",
        'trueStatus': 'notCarrier'
    }
}

print(model_accuracy(test_results))  # expected: 0.8
