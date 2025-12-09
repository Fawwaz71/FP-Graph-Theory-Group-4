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

To solve this, we use of the **Hungarian Algorithm**.

#### 3.1 Algorithm Process

#### **1. Initialization**
* **Input:** Determine the number of drivers/customers (n).
* **Input Cost Matrix:** Create matrix C[i][j], where each element represents the travel cost or time from Driver i to Customer j.
* **Backup:** Store a copy of this original matrix (to compute the final total cost later).

#### **2. Row Reduction**
* **For each row i:**
    * Find the minimum value in that row.
    * Subtract this minimum from every element in that row.

#### **3. Column Reduction**
* **For each column j:**
    * Find the minimum value in that column.
    * Subtract this minimum from every element in that column.

#### **4. Cover Zeros**
* **Action:** Cover all zeros in the matrix using the **minimum** number of horizontal and vertical lines.
* **Count:** Let the number of lines = k.

#### **5. Optimality Check (Is k == n? )**

**(If k < n):**
1.  **Find m:** Identify the smallest element that is *not* covered by any line.
2.  **Adjust Matrix:**
    * Subtract m from every uncovered element.
    * Add m to every element located at the intersection of two lines.
3.  **Loop:** Return to **Step 4 (Cover Zeros)**.

**(If k == n):**
* Proceed to next step.

#### **6. Assignment**
* **Selection:** From the final zero matrix, choose a set of zeros such that there is exactly **one** selected zero per row and per column.
* **Record:** These positions represent the optimal Driver-to-Customer pairings (i, j).

#### **7. Compute Total Cost**
* **Summation:** For each assigned pair (i, j):
    * Retrieve the cost from the *original* matrix (C_{original}[i][j]).
    * Add this to the `TotalCost`.

#### **8. Output**
* **Optimal Assignment:** Display which driver is assigned to which customer.
* **Minimum Total Cost:** Display the final calculated sum.

### 4. Case Study: 3x3 Matrix Scenario

this is example for the hungarian algorithm test

| Source \\ Dest | Customer 1 | Customer 2 | Customer 3 | 
 | ----- | ----- | ----- | ----- | 
| **Taxi 1** | 4 | 7 | 3 | 
| **Taxi 2** | 6 | 5 | 8 | 
| **Taxi 3** | 9 | 2 | 6 | 

#### 4.1 The "Greedy" Pitfall vs. Global Optimization

A simple "greedy" approach might immediately assign **Taxi 1 to Customer 3** because the cost (3) is the lowest in the first row. However, this might force Taxi 2 and Taxi 3 into highly inefficient routes (e.g., forcing Taxi 3 to take a route costing 9).

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

### 6. Result
<img width="391" height="314" alt="image" src="https://github.com/user-attachments/assets/7724679f-1878-4f48-82c4-986acc365a87" />
it show the smallest cost and ensure fair assignment for all customer to get the fastest pickup

result of using this algorithm for this example:

1. **Reduced Wait Times:** Optimized routing ensures that the waiting time for all customers is minimized.

2. **Fuel & Cost Savings:** By minimizing total distance traveled, the fleet consumes less fuel used.

3. **Operational Efficiency:** removes human error and bias from the taxi pickup process, allowing for instant decision-making even during peak hours.

### 7. Conclusion

This project demonstrates that efficient taxi dispatching is not a matter of intuition, but of mathematical optimization. By applying the Hungarian Algorithm to a weighted bipartite graph model, we can guarantee the most efficient one-to-one matching between drivers and customers, satisfying our goal of minimizing total travel cost.
