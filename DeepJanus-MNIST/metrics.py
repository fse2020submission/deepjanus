import numpy as np

from properties import EXPECTED_LABEL
from utils import reshape


def get_mindist_seed(solution, dataset):
    # Calculate the distance between each misclassified digit and the seed (mindist metric)
    min_distances = list()
    for ind in solution:
        #get seed
        seed = reshape(dataset[int(ind.seed)])

        # get misclassified member
        if ind.member1.predicted_label != EXPECTED_LABEL:
            misclassified_member = ind.member1.purified
        else:
            misclassified_member = ind.member2.purified
        dist = np.linalg.norm(misclassified_member - seed)
        min_distances.append(dist)
    mindist = np.mean(min_distances)
    return mindist


def get_diameter(solution):
    # Calculate the distance between each misclassified digit and the farthest element of the solution (diameter metric)
    max_distances = list()
    for d1 in solution:
        maxdist = float(0)
        for d2 in solution:
            if d1 != d2:
                dist = np.linalg.norm(d1.purified - d2.purified)
                if dist > maxdist:
                    maxdist = dist
        max_distances.append(maxdist)
    diameter = np.mean(max_distances)
    return diameter
