import marimo

__generated_with = "0.16.5"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Graphs""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout("Disclaimer: no AI tools were used to create this notebook.")
    return


@app.cell
def _():
    import networkx as nx, matplotlib.pyplot as plt, numpy as np
    return nx, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Task 1
    Modify the adjacency list, edge list, and adjacency matrix below to obtain the given graph // had issues with file reading so coded the data structures
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 1. Adjacency list:""")
    return


@app.cell
def _(nx):
    adj_list_dict = {
        '0': ['1', '2', '5'],
        '1': ['0', '3', '4'],
        '2': ['0', '4'],
        '3': ['1', '4'],
        '4': ['1', '2', '3', '5'],
        '5': ['0', '4']
    }
    
    G = nx.Graph()
    for _node, _neighbors in adj_list_dict.items():
        for _neighbor in _neighbors:
            G.add_edge(_node, _neighbor)
    
    return (G,)


@app.cell
def _(G):
    G.edges()
    return


@app.cell
def _(G, nx, plt):
    nx.draw(G, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 2. Edge list:""")
    return


@app.cell
def _(nx):
    edge_list = [
        ('0', '1'), ('0', '2'), ('0', '5'),
        ('1', '3'), ('1', '4'), ('2', '4'),
        ('3', '4'), ('4', '5')
    ]
    
    H = nx.Graph()
    H.add_edges_from(edge_list)
    return (H,)


@app.cell
def _(H, nx, plt):
    nx.draw(H, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""#### 3. Adjacency Matrix""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now create a 2D numpy.array that defines the adjacency matrix""")
    return


@app.cell
def _(np):
    A = np.array([
        [0, 1, 1, 0, 0, 1],
        [1, 0, 0, 1, 1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0]
    ])
    return (A,)


@app.cell
def _(A, nx, plt):
    G_1 = nx.from_numpy_array(A)
    nx.draw(G_1, with_labels=True)
    plt.show()
    return (G_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Task 2 - Depth-first search""")
    return


@app.cell
def _():
    def DFS(source_node, adj_list):
        visited = [False] * len(adj_list)
        DFS_rec(source_node, visited, adj_list)

    def DFS_rec(n, visited, adj_list):
        visited[n] = True
        print(n, end=' ')
        for neighbor in adj_list[n]:
            if not visited[neighbor]:
                DFS_rec(neighbor, visited, adj_list)
    
    return DFS, DFS_rec


@app.cell
def _(DFS):
    adj = [[1, 2, 5], [0, 4, 3], [0, 4], [1, 4], [1, 2, 3, 5], [4, 0]]
    DFS(3, adj)
    return (adj,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Task 3 - Breadth-first search""")
    return


@app.cell
def _():
    def BFS(source_node, adjacency_list):
        visited = [False] * len(adjacency_list)
        queue = [source_node]
        visited[source_node] = True
        
        while queue:
            node = queue.pop(0)
            print(node, end=' ')
            for neighbor in adjacency_list[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    return (BFS,)


@app.cell
def _(BFS, adj):
    BFS(4, adj)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Task 4 - Dijkstra's Algorithm""")
    return


@app.cell
def _():
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    return (graph,)


@app.cell
def _():
    def dijkstra(g, source):
        n = len(g)
        dist = [10000] * n
        visited = [False] * n
        dist[source] = 0
        
        for _ in range(n):
            u = minDistance(dist, visited, g)
            visited[u] = True
            for v in range(n):
                if g[u][v] > 0 and not visited[v] and dist[v] > dist[u] + g[u][v]:
                    dist[v] = dist[u] + g[u][v]
        
        print("Vertex \t Distance from Source")
        for node in range(n):
            print(f"{node} \t\t {dist[node]}")

    def minDistance(dist, visited, g):
        minDist = 10000
        min_index = 0
        for v in range(len(g)):
            if dist[v] < minDist and not visited[v]:
                minDist = dist[v]
                min_index = v
        return min_index
    
    return dijkstra, minDistance


@app.cell
def _(dijkstra, graph):
    dijkstra(graph, 0)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Final Task - Graph Traversal Visualization""")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    # UI elements
    algo_select = mo.ui.dropdown(["BFS", "DFS"], value="BFS", label="Algorithm")
    start_select = mo.ui.dropdown([0, 1, 2, 3, 4, 5], value=0, label="Start Node")
    step_slider = mo.ui.slider(0, 10, value=0, label="Step", show_value=True)
    
    mo.vstack([
        mo.md("**Controls:**"),
        algo_select,
        start_select,
        step_slider
    ])
    return algo_select, start_select, step_slider


@app.cell
def _(A, algo_select, mo, nx, plt, start_select, step_slider):
    from collections import deque
    
    # Build adjacency list
    _n = A.shape[0]
    _adj = {i: [] for i in range(_n)}
    for _i in range(_n):
        for _j in range(_n):
            if A[_i, _j] != 0:
                _adj[_i].append(_j)
    
    # BFS traversal
    def _bfs(s):
        _vis = set([s])
        _order = []
        _q = deque([s])
        while _q:
            _u = _q.popleft()
            _order.append(_u)
            for _v in _adj[_u]:
                if _v not in _vis:
                    _vis.add(_v)
                    _q.append(_v)
        return _order
    
    # DFS traversal
    def _dfs(s):
        _vis = set()
        _order = []
        def _rec(u):
            _vis.add(u)
            _order.append(u)
            for v in _adj[u]:
                if v not in _vis:
                    _rec(v)
        _rec(s)
        return _order
    
    # Get order
    if algo_select.value == "BFS":
        _trav = _bfs(start_select.value)
    else:
        _trav = _dfs(start_select.value)
    
    # Get current step 
    _step = min(step_slider.value, len(_trav) - 1)
    _curr = _trav[_step]
    _visited = set(_trav[:_step + 1])
    
    # Draw graph
    _g = nx.from_numpy_array(A)
    _pos = nx.spring_layout(_g, seed=42)
    
    _colors = []
    for _node in _g.nodes():
        if _node == _curr:
            _colors.append('orange')
        elif _node in _visited:
            _colors.append('lightgreen')
        else:
            _colors.append('lightblue')
    
    _fig, _ax = plt.subplots(figsize=(8, 6))
    nx.draw(_g, _pos, node_color=_colors, with_labels=True,
            node_size=700, font_size=16, font_weight='bold', ax=_ax)
    _ax.set_title(f"{algo_select.value} Traversal - Step {_step + 1}/{len(_trav)}", 
                  fontsize=14, fontweight='bold')
    plt.tight_layout()
    
    mo.vstack([
        mo.md(f"**Traversal Order:** {_trav}"),
        mo.md(f"**Current Node:** {_curr}"),
        mo.md(f"**Visited Nodes:** {sorted(_visited)}"),
        mo.md("**Legend:** 🟠 Orange = Current | 🟢 Green = Visited | 🔵 Blue = Unvisited"),
        mo.as_html(_fig)
    ])
    return deque,


if __name__ == "__main__":
    app.run()