
def test_insert_edge():
    from Graphs.Graph import Graph
    stu = Graph(iterable=[])
    gen = ['0 1', '0 2', '0 3', '0 4', '1 2', '1 3', '1 4', '2 3', '2 4', '3 4']
    for e in gen:
        s, d = e.split()
        stu.insert_edge(int(s), int(d))
    # Try inserting duplicate edge
    stu.insert_edge(0, 1)

    print("Your Graph structure:")
    print('\n'.join(str(i) for i in stu.matrix))

    solution = [
                [None, 1, 2, 3, 4],
                [None, None, 2, 3, 4],
                [None, None, None, 3, 4],
                [None, None, None, None, 4],
                [None, None, None, None, None]
            ]

    print("\nSolution Graph structure:")
    print('\n'.join(str(i) for i in solution))

    assert solution == stu.matrix

def test_construction():
    from Graphs.Graph import Graph, Generate_edges
    connectedness = 1
    gen = Generate_edges(10, connectedness)
    stu = Graph(iterable=gen)
    print("Your Graph structure:")
    print('\n'.join(str(i) for i in stu.matrix))

    solution = [
                [None, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                [None, None, 2, 3, 4, 5, 6, 7, 8, 9],
                [None, None, None, 3, 4, 5, 6, 7, 8, 9],
                [None, None, None, None, 4, 5, 6, 7, 8, 9],
                [None, None, None, None, None, 5, 6, 7, 8, 9],
                [None, None, None, None, None, None, 6, 7, 8, 9],
                [None, None, None, None, None, None, None, 7, 8, 9],
                [None, None, None, None, None, None, None, None, 8, 9],
                [None, None, None, None, None, None, None, None, None,9],
                [None, None, None, None, None, None, None, None, None, None]
            ]
    print("\nSolution Graph structure:")
    print('\n'.join(str(i) for i in solution))

    assert solution == stu.matrix

def test_construction_from_file():
    from Graphs.Graph import Graph

    fp = open("Graphs/test_construction_simple.txt", 'r')

    stu = Graph(iterable=fp)

    print("Your Graph structure:")
    print('\n'.join(str(i) for i in stu.matrix))

    solution = [
        [None, 1, 4, 5, 8, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, 1, None, None, None, 44, 50, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, 4, None, None, None, None, None, None, 10, None, None, 26, 47, 59, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 385, 2159, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, 10, 175, 313, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 30, 34, 35],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 7, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, 10, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
    ]

    print("\nCorrect Graph structure:")
    print('\n'.join(str(i) for i in solution))

    assert solution == stu.matrix

def test_bfs():
    from Graphs.Graph import Graph

    filename = open("Graphs/test_search_simple.txt", 'r')

    stu = Graph(iterable=filename)

    path = stu.bfs(1, 9, [])

    print("Your Path: ", path)
    all_paths = [[1, 3, 5, 6, 9], [1, 3, 6, 9]]

    assert path in all_paths

def test_dfs():
    from Graphs.Graph import Graph
    filename = open("Graphs/test_search_simple.txt", 'r')

    stu = Graph(iterable=filename)

    path = stu.dfs(1, 9)
    print("Your Path: ", path)
    all_paths = [[1, 3, 5, 6, 9], [1, 3, 6, 9]]

    assert path in all_paths

def test_k_away():
    from Graphs.Graph import find_k_away
    gen = [
        "100 99 ",
        "99  98 ",
        "98  97 ",
        "99  20 ",
        "100 97",
        "97  1",
        "97  98",
        "98  100"
    ]
    assert find_k_away(2, gen, 100) == {1, 98, 20}

    gen = open("Graphs/test_construction_simple.txt")
    assert find_k_away(3, gen, 3) == {26, 59, 4, 47}

def test_k_away_bigger():
    from Graphs.Graph import find_k_away
    gen = open("Graphs/test_construction_simple.txt")
    assert find_k_away(0, gen, 7) == {7}
    gen = [
        "1 2",
        "2 5",
        "2 4",
        "4 5",
        "5 1",
        "5 6",
        "6 1"
    ]

    for i, j in enumerate([{1}, {2}, {4, 5}, {5, 6}, {6}, set()]):
        assert (find_k_away(i, gen, 1) == j)

    assert (find_k_away(3, gen, -1) == set())

def main():
    test_insert_edge()
    test_construction()
    test_construction_from_file()
    test_bfs()
    test_dfs()
    test_k_away()
    test_k_away_bigger()
    
    print("Graph Functions All Passed!")
    
main()
