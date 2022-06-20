import heapq

def dijkstra(graph, starting_vertex, endpoint_vertext):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbour, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(pq, (distance, neighbour))
    
    return distances[endpoint_vertext]

# Client
graph = {
    'A': {'B': 2, 'C': 6, 'D': 1},
    'B': {'D': 5},
    'C': {'D': 8},
    'D': {'A': 9},
}

dijkstra(graph, 'A', 'D')