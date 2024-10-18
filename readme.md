# Smart City Response to Homelessness

This project leverages computer heuristic algorithms to tackle the complex problem of assigning homeless individuals to housing based on their unique characteristics and the nature of available services. We developed eight distinct algorithms to create optimal assignment solutions, each aimed at balancing individual needs and service constraints.

## Key Features
- **Heuristic Algorithms**: Eight algorithms designed to generate effective homeless-to-housing assignments.
- **Optimal Solution Comparison**: Each algorithm’s result is compared with the optimal solution obtained from the ILP solver (IBM ILOG CPLEX Optimization Studio).
- **Performance Metrics**: We analyze the differences in calculation time and solution quality.
- **Fairness Assessment**: Assignments are evaluated using the Jane Fairness formula to assess the fairness of each housing assignment.

## Project Overview

The importance of this project stems from the fact that when constraints exist in an assignment process, the number of possible assignment sets increases exponentially. For instance, if we have 15 homeless individuals and 15 shelters, each with only one bed available, there are **1,307,674,368,000** possible assignments.

Our goal is to maximize the "goodness-of-fit" for each assignment, ensuring that we find a solution that best matches individuals with services.

### Approach
- **Brute Force Limitation**: While brute-forcing the solution is theoretically possible, it would take an infeasible amount of time.
- **Greedy Algorithms**: We implement simple mathematical operations to get closer to an optimal solution.
- **Local Search Algorithms**: After the greedy method finds a sub-optimal solution, the local search algorithm attempts to further refine the solution by exploring the local space around it.

Further details on the algorithm and its intricacies are available in the project’s published paper. 

## Published Paper
This project has been published in [IEEE Xplore](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8955816).
