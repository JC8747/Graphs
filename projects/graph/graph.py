"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}
        self.visited = set()
        self.path = []

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph!")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)

        visited = set()

        while q.size() > 0:

            vertex = q.dequeue()

            if vertex not in visited:
                print(vertex)
                visited.add(vertex)
                for neighbor in self.get_neighbors(vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)

        visited = set()


        while s.size() > 0:
            vertex = s.pop()

            if vertex not in visited:
                print(vertex)
                visited.add(vertex)

                for neighbor in self.get_neighbors(vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        visited = {}

        for i in self.vertices:
            visited[i] = False

        def recurse(vert_id, visited):
            print(vert_id)
            visited[vert_id] = True

            if False not in visited.values():
                return
            else:
                for neighbor in self.get_neighbors(vert_id):
                    if visited[neighbor] == False:
                        recurse(neighbor, visited)

        recurse(starting_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            path = q.dequeue()
            last = path[-1]
            if last not in visited:
                if last == destination_vertex:
                    return path
                visited.add(last)
                for neighbor in self.get_neighbors(last):
                    new_path = [*path]
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])

        visited = set()

        while s.size() > 0:
            path = s.pop()
            last = path[-1]

            if last not in visited:
                if last == destination_vertex:
                    return path

                visited.add(last)

                for neighbor in self.get_neighbors(last):
                    new_path = [*path]
                    new_path.append(neighbor)
                    s.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        if visited == None:
            visited = set()

        if path == None:
            path = []


        visited.add(starting_vertex)
        new_path = [*path, starting_vertex]

        if new_path[-1] == destination_vertex:
            return new_path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, new_path)
                if neighbor_path:
                    return neighbor_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))