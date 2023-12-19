from itertools import product, combinations_with_replacement

class Combiner:

    def __init__(self):
        pass


    def generateDistribution(elements,repeats):
        return list(combinations_with_replacement(elements,repeats))


    def generateBoxDistributions(NBoxes,elements):

        boxes = [f'{i}' for i in range(NBoxes)]

        all_distributions = list(product(boxes, repeat=len(elements)))
        distributions_in_boxes = []

        for distribution in all_distributions:

            distribution_in_boxes = {box: [] for box in boxes}

            for ball, box in zip(elements, distribution):
                distribution_in_boxes[box].append(ball)

            distributions_in_boxes.append(distribution_in_boxes)

        unique_distributions = [dict((key, tuple(value)) for key, value in dist.items()) for dist in distributions_in_boxes]

        return unique_distributions