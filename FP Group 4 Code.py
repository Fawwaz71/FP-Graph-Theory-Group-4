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


# input
n = int(input("number of taxi and customers: "))
print("\ncosts taxi to customers: ")

cost = []

for taxi in range(n):
    row = list(map(int, input(f"Taxi {taxi+1}: ").split()))
    cost.append(row)

assignment, total = hungarian(cost)


# output
print("\ntaxi assignment:")
for taxi in range(len(assignment)):
    customer = assignment[taxi]
    print(f"Taxi {taxi + 1} = Customer {customer + 1} (cost={cost[taxi][customer]})")

print("\nsmallest cost:", total)
