import random


def calc_target(solution, flow, distance):
    return sum(flow[i][j] * distance[k][l] * solution[i][k] * solution[j][l] for i in range(n) for j in range(n) for k in range(n) for l in range(n))

# hyperparameters
n = 4
flow = [[random.randint(1,50) for _ in range(n)] for _ in range(n)] # przepływ pomiędzy zakładami
distance = [[random.randint(1,50) for _ in range(n)] for _ in range(n)]  # odległość pomiędzy zakładami
solution = [[0 for j in range(n)] for i in range(n)]

print('a')