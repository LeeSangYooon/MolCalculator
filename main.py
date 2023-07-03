from typing import Dict
from Node import Node, make_node, get_value

nodes: Dict[str,Node] = {}
W = make_node(nodes, 'W', ['m*n', 'V*D'])   # 질량
m = make_node(nodes, 'm', ['W/n'])          # 분자량
n = make_node(nodes, 'n', ['W/m', 'M*V/t'])   # 몰 수
M = make_node(nodes, 'M', ['n/V*t'])        # 몰 농도
V = make_node(nodes, 'V', ['n/M*t', 'W/D'])   # 부피
D = make_node(nodes, 'D', ['W/V'])          # 밀도
t = make_node(nodes, 'T', [], 1000)         # 1000 (상수)

d = {'질량': W, '분자량': m, '몰수':n, '몰농도':M, '부피':V, '밀도':D}
l = input('변수 입력: ').split()
for i in range(0, len(l), 2):
    key = l[i]
    value = float(l[i+1])
    d[key].value = value

for key in d.keys():
    v = get_value(d[key], nodes)
    print(f'{key}: {v if v is not None else "알 수 없음"}')