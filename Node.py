from typing import List, Dict

class Edges:
    def __init__(self, variables, operators) -> None:
        self.variables: List[Node] = variables
        self.operators: List[int] = operators

class Node:
    def __init__(self, name, edgeses, value=None) -> None:
        self.name:str = name
        self.edgeses: List[Edges] = edgeses
        self.value: float | None = value
        self.visited = False

def dfs(target: Node) -> float | None:
    if target.value is not None:
        return target.value
    value = None
    for edges in target.edgeses:
        able = True
        found_values = []
        for variable in edges.variables:
            if variable.visited:
                able = False
                break

            found_value = dfs(variable)
            if found_value is None:
                able = False
                break
            found_values.append(found_value)

        if able:
            value = found_values[0]
            i = 1
            for op in edges.operators:
                if op == '+': value += found_values[i]
                if op == '-': value -= found_values[i]
                if op == '*': value *= found_values[i]
                if op == '/': value /= found_values[i]
                i+=1
            break

    return value

def get_value(target: Node, nodes: Dict[str,Node]) -> float | None:
    if target.value is not None:
        return target.value
    
    value = None
    for edges in target.edgeses:
        for node in nodes.values(): # dfs에서 빼기
            node.visited = False

        target.visited = True

        able = True
        found_values = []
        for variable in edges.variables:
            if variable.visited:
                able = False
                break

            found_value = dfs(variable)
            if found_value is None:
                able = False
                break
            found_values.append(found_value)

        if able:
            value = found_values[0]
            i = 1
            for op in edges.operators:
                if op == '+': value += found_values[i]
                if op == '-': value -= found_values[i]
                if op == '*': value *= found_values[i]
                if op == '/': value /= found_values[i]
                i+=1
            break

    return value
    
def find_node(name:str, nodes:Dict[str,Node]):
    if nodes.get(name) is None:
        nodes[name] = Node(name, [])
    return nodes[name]

def make_node(nodes:Dict[str,Node], name:str, expressions: List[str], value = None) -> Node:
    exps = []
    for expression in expressions:
        variables= []
        operators = []
        for c in expression:
            if c.isalpha(): variables.append(find_node(c, nodes))
            else: operators.append(c)
        exps.append(Edges(variables, operators))

    if nodes.get(name) is None:
        node = Node(name, exps, value)
        nodes[name] = node
        return node
    else:
        node: Node = nodes[name]
        node.edgeses = exps
        node.value = value
        return node