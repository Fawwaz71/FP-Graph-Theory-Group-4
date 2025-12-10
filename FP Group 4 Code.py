from math import inf

def hungarian(cost):
    n = len(cost)
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minv = [inf] * (n + 1)
        used = [False] * (n + 1)

        while True:
            used[j0] = True
            i0 = p[j0]
            delta = inf
            j1 = 0

            for j in range(1, n + 1):
                if not used[j]:
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            j0 = j1
            if p[j0] == 0:
                break

        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    assignment = [-1] * n
    for j in range(1, n + 1):
        assignment[p[j] - 1] = j - 1

    total_cost = sum(cost[i][assignment[i]] for i in range(n))
    return assignment, total_cost

cost1 = [
    [10, 19, 8], 
    [10, 18, 7], 
    [13, 16, 9]
]
cost2 = [
    [90, 75, 75, 80], 
    [35, 85, 55, 65], 
    [125, 95, 90, 105], 
    [45, 110, 95, 115]
]

cost3 = [
    [10, 0, 20, 15], 
    [15, 25, 0, 10], 
    [0, 15, 30, 20], 
    [20, 10, 15, 0]
]

cost4 = [
    [10, 12, 18, 25, 20], 
    [15, 22, 14, 28, 18], 
    [20, 18, 16, 24, 22], 
    [25, 28, 24, 12, 10], 
    [18, 20, 22, 15, 16]
]

cost5 = [
    [5, 8, 7, 6, 9, 4], 
    [8, 6, 9, 7, 5, 8], 
    [7, 9, 6, 8, 4, 7], 
    [6, 7, 8, 5, 9, 6], 
    [9, 5, 4, 9, 6, 5], 
    [4, 8, 7, 6, 5, 9]
]

all_datasets = [cost1, cost2, cost3, cost4, cost5]

# Loop through and print results for each
for i, cost in enumerate(all_datasets):
    assignment, total = hungarian(cost)

    print(f"\n test {i + 1}")

    print("\ntaxi assignment:")
    for taxi in range(len(assignment)):
        customer = assignment[taxi]
        print(f"Taxi {taxi + 1} = Customer {customer + 1} (cost={cost[taxi][customer]})")

    print("\nsmallest cost:", total)
