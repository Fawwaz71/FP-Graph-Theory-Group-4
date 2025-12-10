# Final Project Proposal: Theory Graph

## Optimizing Taxi Assignment with the Hungarian Algorithm

**Date:** December 9, 2025
**Group:** 4

**Team Members:**

* Fawwaz Reynardio Ednansyah (5025241167)

* Ramasyamsi Ahmad Shabri (5025241008)

* Muhammad Umar Rusjanto (5025231176)

**https://colab.research.google.com/drive/1SPulBlzAGD6ggW7R-_5z47iaxNc6UYEX?usp=sharing**

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
    # n = The size of the matrix
    n = len(cost)

    # u, v: used to modify costs
    # p:    The matchin array. p[j] stores which Row is matched to Column j.
    # way:  Stores the path so we can backtrack.
    u = [0] * (n + 1)
    v = [0] * (n + 1)
    p = [0] * (n + 1)
    way = [0] * (n + 1)

    for i in range(1, n + 1):
        p[0] = i       # Place the current row 'i' into a temp variable
        j0 = 0         # Start searching from the temp column 0
        
        # minv: Stores the smallest cost found so far for the current path scan
        # used: Keeps track of which columns we have looked at in this step
        minv = [inf] * (n + 1)
        used = [False] * (n + 1)

        # --- 3. FIND AUGMENTING PATH (While loop) ---
        # This part searches for the best available column to assign.
        while True:
            used[j0] = True     # Mark current column as visited
            i0 = p[j0]          # Get the row currently assigned to this column
            delta = inf         # delta tracks how much we need
            j1 = 0              # j1 will store the next column to move

            # Check every column j to see if it's a good match
            for j in range(1, n + 1):
                if not used[j]:
                    # Calculate Cost = original - potential
                    cur = cost[i0 - 1][j - 1] - u[i0] - v[j]
                    
                    # Update the minimum cost found in this column
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0  # Remember we came from j0 (for backtracking)
                    
                    # Find the smallest difference to the next step
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j

            # If we are stuck, we change the u and v potentials using 'delta'.
            # This find new edgess that were previously too high.
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minv[j] -= delta

            # Move to the next column
            j0 = j1
            
            # If p[j0] is 0, it means we found a free column! We are done searching.
            if p[j0] == 0:
                break

        # bactrack
        # path found, now we follow the way array backwards to assign the rows to the columns.
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

    # Convert the array into a Python list
    assignment = [-1] * n
    for j in range(1, n + 1):
        assignment[p[j] - 1] = j - 1

    # Sum up the actual costs from the original matrix based on assignment
    total_cost = sum(cost[i][assignment[i]] for i in range(n))
    return assignment, total_cost


# input the number of cost per driver customer
n = int(input("number of taxi and customers: "))
print("\ncosts taxi to customers: ")

cost = []
for taxi in range(n):
    row = list(map(int, input(f"Taxi {taxi+1}: ").split()))
    cost.append(row)

# run the funciton
assignment, total = hungarian(cost)

# output
print("\ntaxi assignment:")
for taxi in range(len(assignment)):
    customer = assignment[taxi]
    print(f"Taxi {taxi + 1} = Customer {customer + 1} (cost={cost[taxi][customer]})")

print("\nsmallest cost:", total)

```

### 6. Result

<img width="361" height="346" alt="image" src="https://github.com/user-attachments/assets/7c0d0716-cd94-4045-b0c4-90f32027a3bc" />


<img width="364" height="387" alt="image" src="https://github.com/user-attachments/assets/b65e92e9-4c48-4393-ab7a-c78fdb0bac88" />


<img width="371" height="444" alt="image" src="https://github.com/user-attachments/assets/98c8159a-40e2-4df9-b7cb-5407321135b0" />


<img width="361" height="441" alt="image" src="https://github.com/user-attachments/assets/c11e7688-7eb1-4cd0-a438-e00faa0b36cb" />


it show the smallest cost and ensure fair assignment for all customer to get the fastest pickup

result of using this algorithm for this example:

1. **Reduced Wait Times:** Optimized routing ensures that the waiting time for all customers is minimized.

2. **Fuel & Cost Savings:** By minimizing total distance traveled, the fleet consumes less fuel used.

3. **Operational Efficiency:** removes human error and bias from the taxi pickup process, allowing for instant decision-making even during peak hours.

### 7. Conclusion

This project demonstrates that efficient taxi dispatching is not a matter of intuition, but of mathematical optimization. By applying the Hungarian Algorithm to a weighted bipartite graph model, we can guarantee the most efficient one-to-one matching between drivers and customers, satisfying our goal of minimizing total travel cost.
