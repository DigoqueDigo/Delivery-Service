from veiculos.veiculo import Veiculo
from veiculos.carro import Carro
from veiculos.mota import Mota
from veiculos.bicicleta import Bicicleta
from grafo.grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt
from itertools import product

"""

def generate_distributions(N, M):
    colors = ['Color1', 'Color2', 'Color3']  # Add your actual color names or identifiers here
    balls = [f'Ball{i + 1}' for i in range(N)]
    boxes = [f'Box{i + 1}' for i in range(M)]

    # Generate all possible combinations
    all_distributions = list(product(boxes, repeat=N))

    # Map the combinations to boxes
    distributions_in_boxes = []
    for distribution in all_distributions:
        distribution_in_boxes = {box: [] for box in boxes}
        for ball, box in zip(balls, distribution):
            distribution_in_boxes[box].append(ball)
        distributions_in_boxes.append(distribution_in_boxes)

    # Remove duplicate distributions
    unique_distributions = [dict((key, tuple(value)) for key, value in dist.items()) for dist in distributions_in_boxes]

    return unique_distributions

# Example usage
N = 3  # Number of colored balls
M = 3  # Number of boxes
distributions = generate_distributions(N, M)

# numero de caixas elevado ao numero de bolas

# Print the unique distributions
for idx, distribution in enumerate(distributions, start=1):
    print(f'Distribution {idx}: {distribution}')

"""


elements = ['A','B','C']

# Generate all possible pairs
combinations = list(product(elements, repeat=2))

# Print the result
for case, combination in enumerate(combinations, start=1):
    print(f"case{case} -> {list(combination)}")