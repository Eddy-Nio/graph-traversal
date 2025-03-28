#!/usr/bin/env python3
"""
graph_traversal.py

This module implements a Graph class with methods for adding nodes and edges,
performing Breadth-First Search (BFS) and Depth-First Search (DFS) traversals.
The program accepts terminal input to choose the algorithm and starting node.
"""

from collections import deque
from typing import Dict, List, TypeVar, Any, Optional, Set, Tuple
from colorama import init, Fore, Style

T = TypeVar('T', str, int, tuple)  # Restrict to common hashable types

class Graph:
    """
    Graph implementation using adjacency list.
    
    Supports:
    - Adding/removing nodes and edges
    - BFS/DFS traversal
    - Path finding
    - Graph analysis (connectivity, cycles)
    
    Example:
        >>> g = Graph()
        >>> g.add_edge('A', 'B')
        >>> g.add_edge('B', 'C')
        >>> print(g.shortest_path('A', 'C'))
        ['A', 'B', 'C']
    """

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.adj_list: Dict[T, List[T]] = {}

    def add_node(self, node: T) -> None:
        """
        Add a node to the graph.

        Args:
            node: A hashable object representing the node.
        """
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, from_node: T, to_node: T, bidirectional: bool = True) -> None:
        """
        Add an edge between two nodes.

        Args:
            from_node: Source node
            to_node: Destination node
            bidirectional: If True, creates edges in both directions

        Raises:
            ValueError: If nodes are invalid or if creating a self-loop
            TypeError: If nodes are not hashable
        """
        if not (isinstance(from_node, (int, str, tuple)) and isinstance(to_node, (int, str, tuple))):
            raise TypeError("Nodes must be hashable types")
        if from_node == to_node:
            raise ValueError("Self loops are not allowed")
            
        self.add_node(from_node)
        self.add_node(to_node)
        
        if to_node not in self.adj_list[from_node]:
            self.adj_list[from_node].append(to_node)
            
        if bidirectional and from_node not in self.adj_list[to_node]:
            self.adj_list[to_node].append(from_node)

    def get_neighbors(self, node: T) -> List[T]:
        """
        Return the list of neighbors for a given node.

        Args:
            node: The node whose neighbors are to be returned.

        Returns:
            List[T]: List of adjacent nodes.
        """
        return self.adj_list.get(node, [])

    def remove_node(self, node: T) -> None:
        """
        Remove a node and all its edges from the graph.

        Args:
            node: The node to remove
        """
        if node in self.adj_list:
            for other_node in self.adj_list:
                if node in self.adj_list[other_node]:
                    self.adj_list[other_node].remove(node)
            del self.adj_list[node]

    def has_path(self, start: T, end: T) -> bool:
        """
        Check if there exists a path between start and end nodes.

        Args:
            start: Starting node
            end: Destination node

        Returns:
            bool: True if path exists, False otherwise
        """
        return end in bfs(self, start)

    def is_connected(self) -> bool:
        """Check if the graph is connected."""
        if not self.adj_list:
            return True
        start = next(iter(self.adj_list))
        visited = set(bfs(self, start))
        return len(visited) == len(self.adj_list)

    def shortest_path(self, start: T, end: T) -> List[T]:
        """Find shortest path between two nodes using BFS."""
        if start not in self.adj_list or end not in self.adj_list:
            return []
            
        queue = deque([(start, [start])])
        visited = {start}
        
        while queue:
            vertex, path = queue.popleft()
            if vertex == end:
                return path
                
            for neighbor in self.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return []

    @property
    def size(self) -> int:
        """Number of nodes in the graph."""
        return len(self.adj_list)

    @property
    def edge_count(self) -> int:
        """Number of edges in the graph."""
        return sum(len(neighbors) for neighbors in self.adj_list.values()) // 2

    @property
    def density(self) -> float:
        """Calculate graph density."""
        n = self.size
        if n <= 1:
            return 0.0
        return (2 * self.edge_count) / (n * (n - 1))

    @property
    def is_cyclic(self) -> bool:
        """Check if graph contains cycles."""
        def dfs_cycle(node: T, parent: T, visited: set) -> bool:
            visited.add(node)
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    if dfs_cycle(neighbor, node, visited):
                        return True
                elif neighbor != parent:
                    return True
            return False
            
        visited = set()
        for node in self.adj_list:
            if node not in visited:
                if dfs_cycle(node, node, visited):
                    return True
        return False

    def __str__(self) -> str:
        return "\n".join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())

    def visualize_graph(self) -> str:
        """
        Returns a more visual ASCII representation of the graph.
        """
        if not self.adj_list:
            return "Empty Graph"
            
        result = [f"{Fore.CYAN}Graph Structure ({self.size} nodes, {self.edge_count} edges):{Style.RESET_ALL}"]
        for node in sorted(self.adj_list.keys()):
            neighbors = sorted(self.adj_list[node])
            edges = " ".join(f"{Fore.GREEN}--->{Style.RESET_ALL} {n}" for n in neighbors)
            result.append(f"{Fore.YELLOW}{node}{Style.RESET_ALL} {edges}")
        return "\n".join(result)


def bfs(graph: 'Graph', start: T) -> List[T]:
    """
    Perform Breadth-First Search (BFS) on the graph starting from 'start' node.

    Args:
        graph: Instance of Graph.
        start: Starting node for BFS.

    Returns:
        List[T]: List of nodes in the order they were visited.
    """
    visited = set()
    order = []
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in graph.get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order


def dfs(graph, start, visited=None, order=None):
    """
    Perform Depth-First Search (DFS) on the graph starting from 'start' node.

    Args:
        graph: Instance of Graph.
        start: Starting node for DFS.
        visited: Set of visited nodes (for recursive calls).
        order: List of nodes in the order they were visited.

    Returns:
        List of nodes in the order they were visited.
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph.get_neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)

    return order


def build_sample_graph():
    """
    Build and return a sample graph for demonstration purposes.

    Returns:
        An instance of Graph with predefined nodes and edges.
    """
    g = Graph()
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("E", "F"),
        ("F", "G")
    ]
    for from_node, to_node in edges:
        g.add_edge(from_node, to_node)
    return g


def print_menu():
    """Display a colorful menu interface."""
    print(f"\n{Fore.CYAN}=== Graph Traversal Algorithm ===={Style.RESET_ALL}")
    print(f"\n{Fore.YELLOW}Available Operations:{Style.RESET_ALL}")
    print("1 - Breadth-First Search (BFS)")
    print("2 - Depth-First Search (DFS)")
    print("3 - View Graph Structure")
    print("4 - Exit")


def validate_node(node: str, graph: Graph) -> bool:
    """
    Validate if a node exists in the graph.
    
    Args:
        node: Node to validate
        graph: Graph instance
    
    Returns:
        bool: True if node is valid
    """
    if not node:
        print(f"{Fore.RED}Error: Node cannot be empty!{Style.RESET_ALL}")
        return False
    if node not in graph.adj_list:
        print(f"{Fore.RED}Error: Node '{node}' not found in graph!{Style.RESET_ALL}")
        return False
    return True


def main():
    """Enhanced main function with better UI."""
    init()
    graph = build_sample_graph()
    
    while True:
        print_menu()
        choice = input(f"\n{Fore.GREEN}Enter your choice (1-4): {Style.RESET_ALL}").strip()
        
        if choice == "4":
            print(f"\n{Fore.YELLOW}Goodbye!{Style.RESET_ALL}")
            break
            
        if choice == "3":
            print(f"\n{graph.visualize_graph()}")
            continue
            
        if choice not in ["1", "2"]:
            print(f"{Fore.RED}Invalid option! Please try again.{Style.RESET_ALL}")
            continue
            
        start_node = input(f"\n{Fore.GREEN}Enter starting node (A-G): {Style.RESET_ALL}").strip().upper()
        
        if not validate_node(start_node, graph):
            continue

        if choice == "1":
            traversal_order = bfs(graph, start_node)
            print(f"\n{Fore.CYAN}BFS Traversal Order:{Style.RESET_ALL}")
        else:
            traversal_order = dfs(graph, start_node)
            print(f"\n{Fore.CYAN}DFS Traversal Order:{Style.RESET_ALL}")
            
        print(f"{Fore.YELLOW}{' -> '.join(traversal_order)}{Style.RESET_ALL}")


if __name__ == '__main__':
    main()
