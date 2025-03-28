# Graph Traversal Algorithms: BFS and DFS Implementation in Python 🚀

[![Python 3.11](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Code Style: PEP8](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen)](https://peps.python.org/pep-0008/)

A Python implementation of Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms for graph traversal, featuring an interactive command-line interface and visualization.

## Table of Contents
- [Overview](#-overview)
- [Features](#features)
- [Installation](#️-installation)
- [Usage](#-usage)
- [Examples](#-examples)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#author)
- [Acknowledgments](#acknowledgments)

## 📖 Overview
This project implements graph traversal algorithms with visualization features:
- **Graph Structure**: Adjacency list implementation (O(V + E) space)
- **Algorithms**: BFS and DFS with O(V + E) time complexity
- **Visualization**: ASCII-art graph representation with color
- **Interface**: Interactive CLI with input validation

## Features
- **Core Functionality**:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Shortest Path Finding
  - Cycle Detection
- **Advanced Features**:
  - Graph density calculation
  - Connectivity checking
  - Path visualization
  - Performance metrics
- **Developer Tools**:
  - Type hints
  - Comprehensive tests
  - Documentation
  - Example graphs

## ⚙️ Installation

### Prerequisites
- Python 3.7+
- pip package manager

### Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Eddy-nio/graph-traversal.git
   cd graph-traversal
   ```

2. Create virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### Quick Start
```bash
python main.py
```

### Example Code
```python
from graph_traversal import Graph

# Create and populate graph
g = Graph()
g.add_edge('A', 'B')
g.add_edge('B', 'C')

# Run algorithms
bfs_path = g.bfs('A')  # ['A', 'B', 'C']
shortest = g.shortest_path('A', 'C')  # ['A', 'B', 'C']

# Visualize
print(g.visualize_graph())
```


## 📚 Documentation
- [API Reference](docs/API.md)
- [Algorithm Details](docs/ALGORITHMS.md)
- [Examples](docs/EXAMPLES.md)

## 🤝 Contributing
1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License
Distributed under the MIT License. See [LICENSE](LICENSE.md) for more information.

Crafted with clarity and efficiency for educational and practical use. 🧠🔍

## Author

Eddy-Nio - [ebecerra@ucompensar.edu.co](mailto:ebecerra@ucompensar.edu.co)

## Acknowledgments

- Data Structures course at Universidad Compensar
- Python community for excellent documentation