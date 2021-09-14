# реализация графа {'start': {'a': 2, 'b': 2}, 'a': {'fin': 1}, 'b': {'a': 3, 'fin': 5}, 'fin': {}}

graf = dict()
graf["start"] = {}
graf["start"]["a"] = 6
graf["start"]["b"] = 2

graf["a"] = {}
graf["a"]["fin"] = 1
graf["b"] = {}
graf["b"]["a"] = 3
graf["b"]["fin"] = 5
graf["fin"] = {}

#  Таблица стоимости {'a': 6, 'b': 2, 'fin': inf}
infinity = float("inf")
costs = dict()
costs["a"]=6
costs["b"]=2
costs["fin"] = infinity

#  Таблица родителей {'a': 'start', 'b': 'start', 'in': None}
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["in"] = None

#  массив для обработки обработанных узлов
processed = []


def find_lowest_cost_node(costs: dict) -> str:
    """находим узел с наименьшей стоимостью"""
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # перебираем все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:  # если узел с наименьшей стоимостью из уже виденных и не был
            lowest_cost = cost                            # еще обработан
            lowest_cost_node = node
    return lowest_cost_node  # возвращаем узел с наименьшей стоимостью


node = find_lowest_cost_node(costs)  # находим узел с наименьшей стоимостью


while node is not None:
    cost = costs[node]
    neighbors = graf[node]
    for n in neighbors.keys():       # перебрать всех соседей текущего узла
        print('n=', n)
        new_cost = cost+neighbors[n]
        if costs[n] > new_cost:      # если через этот узел быстрее добраться
            costs[n] = new_cost
            print(costs[n])
            parents[n] = node        # этот узел становится новым родителем
            print('parent=', node)
    processed.append(node)
    print(processed)
    node = find_lowest_cost_node(costs)  # находим узел с наименьшей стоимостью




