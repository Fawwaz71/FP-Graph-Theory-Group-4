# Final Project Proposal: Theory Graph

## Optimizing Taxi Assignment with the Hungarian Algorithm

**Date:** December 9, 2025
**Group:** 4

**Team Members:**

* Fawwaz Reynardio Ednansyah (5025241167)

* Ramasyamsi Ahmad Shabri (5025241008)

* Muhammad Umar Rusjanto (5025231176)

### 1. Introduction

#### 1.1 The Challenge: Efficient Dispatch

In the modern logistics and transportation industry, taxi fleets face a critical operational challenge: assigning multiple drivers located at various coordinates to waiting customers in the most efficient manner possible.

The core of this problem is not merely finding the nearest driver for a single customer, but rather finding a global optimum where the total travel cost (or time) for the entire fleet is minimized. This is complicated by the constraint that orders are often concurrent, requiring a strict 1-to-1 matching where one driver serves exactly one customer.

#### 1.2 Objective

The primary goal of this project is to model the taxi dispatch scenario using Graph Theory and implement the Hungarian Algorithm to minimize the aggregate cost of travel.

### 2. Theoretical Framework

#### 2.1 Graph Theory Application

To solve the dispatching problem mathematically, we model the scenario as a **Weighted Bipartite Graph**. This structure is ideal for visualizing relationships between two distinct, disjoint sets of vertices.

* **Set A (Drivers):** Represents the available taxi fleet.

* **Set B (Customers):** Represents the passengers waiting for pickup.

* **Edges:** Represent the potential assignment of a specific driver to a specific customer.

* **Weights:** Each edge is assigned a numerical weight representing the "cost" of that assignment. This cost typically correlates to travel distance or estimated time of arrival (ETA).

By representing the problem this way, the logistical challenge transforms into a standard "Assignment Problem"—finding a perfect matching in a weighted bipartite graph that minimizes the sum of weights.

### 3. Proposed Solution: The Hungarian Algorithm

To solve this combinatorial optimization problem efficiently, we propose the use of the **Hungarian Algorithm**. This algorithm solves the assignment problem in polynomial time, making it significantly faster than brute-force permutation methods for larger datasets.

#### 3.1 Algorithm Process

The algorithm proceeds in two main phases consisting of six distinct steps:

**Phase 1: Reduction**

1. **Initialization:** We begin with a square Cost Matrix ($C$), where $C_{ij}$ represents the cost for Driver $i$ to reach Customer $j$.

2. **Row Reduction:** For every row in the matrix, identify the minimum value and subtract it from all elements in that specific row. This ensures every row has at least one zero.

3. **Column Reduction:** Repeat the process vertically. Identify the minimum value in each column of the reduced matrix and subtract it from all elements in that column.

**Phase 2: Optimization and Assignment**
4.  **Cover Zeros:** We attempt to cover all zeros in the matrix using the minimum number of horizontal and vertical lines ($k$).
5.  **Optimality Check:**
\* If the number of lines ($k$) equals the dimension of the matrix ($n$), an optimal assignment is possible.
\* If $k < n$, we must adjust the matrix. We find the smallest uncovered value, subtract it from all uncovered elements, and add it to elements at the intersection of lines. We then repeat the covering step.
6.  **Assignment:** Once optimality is reached, we select a set of zeros such that there is exactly one selected zero in each row and column. These positions represent the optimal driver-customer pairings.

### 4. Case Study: 3x3 Matrix Scenario

To illustrate the effectiveness of the algorithm, we consider a scenario with 3 Taxis and 3 Customers with the following cost matrix (time in minutes):

| Source \\ Dest | Customer 1 | Customer 2 | Customer 3 | 
 | ----- | ----- | ----- | ----- | 
| **Taxi 1** | 4 | 7 | 3 | 
| **Taxi 2** | 6 | 5 | 8 | 
| **Taxi 3** | 9 | 2 | 6 | 

#### 4.1 The "Greedy" Pitfall vs. Global Optimization

A simple "greedy" approach might immediately assign **Taxi 1 to Customer 3** because the cost (3) is the lowest in the first row. However, this might force Taxi 2 and Taxi 3 into highly inefficient routes (e.g., forcing Taxi 3 to take a route costing 9).

The Hungarian Algorithm evaluates the matrix holistically. By processing the reductions, it identifies assignments that might look sub-optimal individually but result in the lowest **total** system cost.

### 5. Expected Benefits

Implementing this algorithmic approach yields three primary benefits for the fleet operator:

1. **Reduced Wait Times:** Optimized routing ensures that the aggregate waiting time for all customers is minimized, directly improving customer satisfaction.

2. **Fuel & Cost Savings:** By minimizing total distance traveled, the fleet consumes less fuel and incurs less vehicle wear-and-tear.

3. **Operational Efficiency:** Automated mathematical assignment removes human error and bias from the dispatching process, allowing for instant decision-making even during peak hours.

### 6. Conclusion

This project demonstrates that efficient taxi dispatching is not a matter of intuition, but of mathematical optimization. By applying the Hungarian Algorithm to a weighted bipartite graph model, we can guarantee the most efficient one-to-one matching between drivers and customers, satisfying our goal of minimizing total travel cost.
