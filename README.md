# Final Project Proposal: Theory Graph

## Optimizing Taxi Assignment with the Hungarian Algorithm

**Date:** December 9, 2025
**Group:** 4

**Team Members:**

* Fawwaz Reynardio Ednansyah (5025241167)

* Ramasyamsi Ahmad Shabri (5025241008)

* Muhammad Umar Rusjanto (5025231176)

### 1. Introduction
A taxi driver has several drivers in different locations. Each driver has different travel times or costs to reach each location point because of the distance from the starting location to the destination. Since taxi orders do not come after another order finishes, they need to utilize their driver to assign each of their driver to the closest customer at the same time.

### 2. Theoretical Framework

#### 2.1 Graph Theory Application

To solve the dispatching problem mathematically, we model the scenario as a **Weighted Bipartite Graph**. This structure is ideal for visualizing relationships between two distinct, disjoint sets of vertices.

* **Set A (Drivers):** taxi fleet

* **Set B (Customers):** passenger

* **Edges:** potential pickup of driver to customer.

* **Weights:** edge is assigned a number for the cost or travel distance

By making the problem this way, it transforms into a "Assignment Problem" finding a perfect matching that minimizes the sum of the cost to travel.

### 3. Solution

To solve this, we use of the **Hungarian Algorithm**
#### 3.1 Flowchart
<img width="1662" height="941" alt="image" src="https://github.com/user-attachments/assets/a905b1a3-7f38-4372-8ce3-b1ab713d700e" />



### 4. Case Study: 3x3 Matrix Scenario

this is example for the hungarian algorithm test

| Source \\ Dest | Customer 1 | Customer 2 | Customer 3 | 
 | ----- | ----- | ----- | ----- | 
| **Taxi 1** | 4 | 7 | 3 | 
| **Taxi 2** | 6 | 5 | 8 | 
| **Taxi 3** | 9 | 2 | 6 | 

#### 4.1 The Greedy vs. optimize

A simple greedy approach might immediately assign Taxi 1 to Customer 3 because the cost (3) is the lowest in the first row. This might force Taxi 2 and Taxi 3 into highly inefficient routes.
The Hungarian Algorithm evaluates the matrix holistically. By processing the reductions, it identifies assignments that might look sub-optimal individually but result in the lowest **total** system cost.

### 5. Code
```
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

```
#### 3.1 Code Explanation



### 6. Result
```
3
4 7 3
6 5 8
9 2 6
```
<img width="391" height="314" alt="image" src="https://github.com/user-attachments/assets/7724679f-1878-4f48-82c4-986acc365a87" />


```
3
10 19 8
10 18 7
13 16 9
```
<img width="404" height="284" alt="image" src="https://github.com/user-attachments/assets/a1cb1a94-5412-4cf3-bd91-78a9d729e3fe" />


```
4
90 75 75 80
35 85 55 65
125 95 90 105
45 110 95 115
```
<img width="382" height="388" alt="image" src="https://github.com/user-attachments/assets/858373a1-d6e5-41d6-94ee-19b399c0e449" />


```
5
10 12 19 11 20
10 5 10 15 30
15 16 12 8 15
18 20 22 25 10
14 12 18 16 20
```
<img width="390" height="444" alt="image" src="https://github.com/user-attachments/assets/4bdc16b9-e141-4926-b2e7-83d79ae12952" />


it show the smallest cost and ensure fair assignment for all customer to get the fastest pickup

result of using this algorithm for this example:

1. **Reduced Wait Times:** Optimized routing ensures that the waiting time for all customers is minimized.

2. **Fuel & Cost Savings:** By minimizing total distance traveled, the fleet consumes less fuel used.

3. **Operational Efficiency:** removes human error and bias from the taxi pickup process, allowing for instant decision-making even during peak hours.

### 7. Conclusion

This project demonstrates that efficient taxi dispatching is not a matter of intuition, but of mathematical optimization. By applying the Hungarian Algorithm to a weighted bipartite graph model, we can guarantee the most efficient one-to-one matching between drivers and customers, satisfying our goal of minimizing total travel cost.
