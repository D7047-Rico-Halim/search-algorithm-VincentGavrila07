# test_algorithms.py
from graphs import bfs, dfs, ucs, greedy_bfs, a_star

# Define the graph and heuristics to be used in tests
graph = {
    'S': [('A', 2), ('B', 1), ('C', 2)],
    'A': [('D', 2)],
    'B': [('D', 1), ('F', 1)],
    'C': [('F', 1)],
    'D': [('H', 1), ('G', 5)],
    'F': [('G', 6), ('J', 1)],
    'H': [('G', 2), ('I', 1)],
    'G': [('I', 1)],
    'J': [('G', 3)],
    'I': []
}

heuristics = {
    'A': 8,
    'B': 9,
    'C': 7,
    'D': 5,
    'F': 4,
    'H': 2,
    'G': 0,
    'I': 1,
    'J': 3,
    'S': 0
}

def test_bfs():
    assert bfs(graph, 'S', 'G') == ['S', 'B', 'D', 'H', 'G']

def test_dfs():
    assert dfs(graph, 'S', 'G') == ['S', 'C', 'F', 'J', 'G']

def test_ucs():
    assert ucs(graph, 'S', 'G') == ['S', 'B', 'D', 'H', 'G']

def test_greedy_bfs():
    assert greedy_bfs(graph, heuristics, 'S', 'G') == ['S', 'C', 'F', 'G']

def test_a_star():
    assert a_star(graph, heuristics, 'S', 'G') == ['S', 'B', 'D', 'H', 'G']
