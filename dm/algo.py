import networkx as nx

#algo vu en cours réecris pour networkx

#non informe

def breadth_first_graph_search(G, start, goal):
    if start == goal:
        return [start]
        
    queue = [(start, [start])]
        
    while queue:
        node, path = queue.pop(0)
            
        if node == goal:
            return path
            
        neighbors = list(G.neighbors(node))
            
        for neighbor in neighbors:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
        
    return None

def depth_first_graph_search(G, start, goal):
    visited = set()
    stack = [(start, [start])]
        
    while stack:
        node, path = stack.pop()
            
        if node == goal:
            return path
            
        if node not in visited:
            visited.add(node)
            neighbors = list(G.neighbors(node))
            for neighbor in neighbors:
                stack.append((neighbor, path + [neighbor]))
        
    return None   

def uniform_cost_search(G, start, goal):
    if start == goal:
        return [start]
        
    queue = [(start, [start], 0)]
        
    while queue:
        node, path, cost = queue.pop(0)
            
        if node == goal:
            return path
            
        neighbors = list(G.neighbors(node))
            
        for neighbor in neighbors:
            if neighbor not in path:
                new_cost = cost + G[node][neighbor]['weight']
                queue.append((neighbor, path + [neighbor], new_cost))
            
        queue.sort(key=lambda x: x[2])
        
    return None

#informé

def astar_search(G, start, goal, heuristic):
    if start == goal:
        return [start]
                
    queue = [(start, [start], 0)]
            
    while queue:
        node, path, cost = queue.pop(0)
                
        if node == goal:
            return path
                
        neighbors = list(G.neighbors(node))
                
        for neighbor in neighbors:
            if neighbor not in path:
                new_cost = cost + G[node][neighbor]['weight']
                h_cost = heuristic(neighbor, goal)
                total_cost = new_cost + h_cost
                queue.append((neighbor, path + [neighbor], total_cost))
                
        queue.sort(key=lambda x: x[2])
            
    return None

def recursive_best_first_search(G, start, goal, heuristic):
    if start == goal:
        return [start]
                
    def recursive_search(node, path, cost):
        if node == goal:
            return path
                    
        neighbors = list(G.neighbors(node))
        neighbors_with_costs = [(neighbor, G[node][neighbor]['weight']) for neighbor in neighbors]
        neighbors_with_costs.sort(key=lambda x: heuristic(x[0], goal))
                    
        for neighbor, neighbor_cost in neighbors_with_costs:
            if neighbor not in path:
                new_cost = cost + neighbor_cost
                new_path = path + [neighbor]
                result = recursive_search(neighbor, new_path, new_cost)
                if result is not None:
                    return result
                    
    return recursive_search(start, [start], 0)

def greedy_best_first_graph_search(G, start, goal, heuristic):
    if start == goal:
        return [start]
                    
    queue = [(start, [start])]
                    
    while queue:
        node, path = queue.pop(0)
                        
        if node == goal:
            return path
                        
        neighbors = list(G.neighbors(node))
        neighbors_with_costs = [(neighbor, heuristic(neighbor, goal)) for neighbor in neighbors]
        neighbors_with_costs.sort(key=lambda x: x[1])
                        
        for neighbor, _ in neighbors_with_costs:
            if neighbor not in path:
                queue.append((neighbor, path + [neighbor]))
                    
    return None

def heuristic(node, goal):
    if isinstance(node, int):
        node = (node, 0) 
    if isinstance(goal, int):
        goal = (goal, 0) 
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)
