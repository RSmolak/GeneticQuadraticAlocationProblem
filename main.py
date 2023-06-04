import random
import numpy as np


def calc_target(solution, flow, distance):
    n = len(solution)
    return sum(flow[solution[i]][solution[j]] * distance[i][j] for i in range(n) for j in range(n))

def breed(parent1, parent2):
    cut_indices = sorted(random.sample(range(len(parent1)),2))
    cut_indices.append(len(parent1))

    segment1 = [parent1[i] for i in range(cut_indices[0], cut_indices[1])]
    segment2 = [parent2[i] for i in range(cut_indices[0], cut_indices[1])]

    child1, child2 = [],[]
    iterator1 = 0
    iterator2 = 0
    for i in range(len(parent1)):
        while parent1[iterator1] in segment2 and iterator1 < len(parent1):
            iterator1+=1
        while parent2[iterator2] in segment1 and iterator2 < len(parent1):
            iterator2+=1
        if cut_indices[0] <= i < cut_indices[1]:
            child1.append(parent2[i])
            child2.append(parent1[i])
        else :
            child1.append(parent1[iterator1])
            child2.append(parent2[iterator2])
            iterator1+=1
            iterator2+=1
    # print(child1,child2)
    return child1, child2

def mutate(solution):
    if random.randint(1,20) == 1:
        index1, index2 = random.choices(range(len(solution)), k=2)
        solution[index1], solution[index2] = solution[index2], solution[index1]

def test():
    # hyperparameters
    n = 10
    num_solutions = 10
    num_pairs = num_solutions//2
    num_epochs = 1000
    display_ratio = 100

    flow = [[random.randint(1,50) for _ in range(n)] for _ in range(n)] # przepływ pomiędzy zakładami
    distance = [[random.randint(1,50) for _ in range(n)] for _ in range(n)]  # odległość pomiędzy zakładami
    solutions = [np.random.permutation(n) for _ in range(num_solutions)]

    for i in range(num_epochs + 1):
        if i % (num_epochs//display_ratio) == 0:
            print("Epoch", i)
        children = []
        for j in range(num_pairs):
            parents = random.choices(sorted(solutions,
                                            key=lambda solution : calc_target(solution, flow, distance),
                                            reverse=True),
                                     weights=[i + 1 for i in range(len(solutions))],
                                     k=2)
            children.extend(breed(parents[0], parents[1]))
            mutate(children[-1])
            mutate(children[-2])
        solutions = children
        if i % (num_epochs//display_ratio) == 0:
            print([calc_target(solution, flow, distance) for solution in sorted(solutions,
                                                                                key=lambda solution: calc_target(solution,
                                                                                                                 flow,
                                                                                                                 distance),
                                                                                reverse=True)])

test()