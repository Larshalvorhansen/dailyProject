# 30-Day Python Challenge: From Basics to Agent-Based Modeling

---

## Week 1: Python Fundamentals & Data Structures

### Day 1: Compound Interest Calculator

Write a function that calculates compound interest over time with configurable rates and periods. Include options for different compounding frequencies (daily, monthly, yearly).

### Day 2: Text Analysis Tool

Create a program that analyzes text files to find word frequency distributions and export results to CSV. Include functionality to find the most common words and basic statistics.

### Day 3: Budget Tracker

Build a simple budget tracker that categorizes expenses and generates monthly summaries. Allow users to add transactions and view spending by category.

### Day 4: Matrix Calculator

Implement a matrix calculator that can add, multiply, and transpose matrices without using NumPy. Focus on understanding the underlying algorithms.

### Day 5: Contact Management System

Create a contact management system using dictionaries with search, add, update, and delete functions. Include the ability to save and load contacts from a file.

### Day 6: Dice Rolling Simulator

Write a program that simulates rolling multiple dice and plots the frequency distribution of outcomes. Visualize how the distribution changes with different numbers of dice.

### Day 7: Expression Calculator

Build a simple calculator that can parse and evaluate mathematical expressions with operator precedence (e.g., "3 + 4 \* 2").

---

## Week 2: Algorithms & Object-Oriented Programming

### Day 8: Sorting Algorithm Comparison

Implement merge sort and quicksort algorithms, then benchmark them on different data sizes. Plot the performance comparison.

### Day 9: Bank Account Class

Create a `BankAccount` class with deposit, withdrawal, and interest calculation methods. Add transaction history tracking and balance inquiry features.

### Day 10: Inventory Management System

Build a simple inventory management system using classes for products, warehouses, and orders. Implement stock tracking and low-stock alerts.

### Day 11: Graph Pathfinding

Implement a breadth-first search algorithm to find the shortest path in a graph represented as an adjacency list. Visualize the graph and the path found.

### Day 12: Population Dynamics

Create a `Population` class that models demographic changes over time with birth rates, death rates, and age structure. Plot population growth over multiple generations.

### Day 13: Monte Carlo Pi Estimation

Write a Monte Carlo simulation to estimate π by randomly throwing darts at a square containing a circle. Visualize the convergence as sample size increases.

### Day 14: Simple Market Simulation

Build a simple market simulation where price fluctuates based on random supply and demand shocks. Track price history and basic market statistics.

---

## Week 3: Introduction to Game Theory

### Day 15: Prisoner's Dilemma

Implement the Prisoner's Dilemma game and simulate different strategy pairs (always cooperate, always defect, random). Display payoff matrices and outcomes.

### Day 16: Nash Equilibrium Finder

Create a function that finds Nash equilibria in 2x2 normal-form games using payoff matrices. Test it on various classic games (Prisoner's Dilemma, Battle of the Sexes, etc.).

### Day 17: Iterated Prisoner's Dilemma

Build an iterated Prisoner's Dilemma simulator where two agents play multiple rounds and track cumulative scores. Experiment with memory and learning.

### Day 18: Strategy Tournament

Implement the "Tit-for-Tat" strategy and pit it against other strategies (always defect, grudger, random, generous tit-for-tat) in a tournament format. Rank strategies by performance.

### Day 19: Rock-Paper-Scissors AI

Create a Rock-Paper-Scissors simulator with multiple AI strategies: random, pattern-matching, frequency-based prediction, and adaptive learning.

### Day 20: Tragedy of the Commons

Model the Tragedy of the Commons with multiple agents deciding how much to extract from a shared resource. Observe how individual rationality leads to collective depletion.

### Day 21: Auction Simulator

Implement an auction simulator comparing first-price and second-price sealed-bid auctions with different bidding strategies (truthful, shade, aggressive).

---

## Week 4: Agent-Based Modeling

### Day 22: Random Walk Agents

Create a simple grid-based world where agents move randomly and track their positions over time. Visualize agent trajectories and spatial distributions.

### Day 23: Schelling's Segregation Model

Build Schelling's segregation model where agents prefer neighbors similar to themselves and relocate if unhappy. Observe emergent segregation patterns from mild preferences.

### Day 24: Predator-Prey Dynamics

Implement a predator-prey model (Lotka-Volterra style) with agents on a grid that hunt, reproduce, and die. Plot population dynamics over time and observe cycles.

### Day 25: Epidemic Spread (SIR Model)

Create an epidemic spread model (Susceptible-Infected-Recovered) where susceptible agents become infected through contact with infected neighbors. Vary infection rates and observe outbreak dynamics.

### Day 26: Heterogeneous Market

Build a market simulation with heterogeneous agents having different strategies for buying and selling based on price signals. Include fundamentalists, chartists, and noise traders.

### Day 27: Opinion Dynamics

Implement a voting behavior model where agents influence each other's opinions through social networks. Model consensus formation, polarization, or fragmentation.

### Day 28: Traffic Flow Simulation

Create a traffic flow simulation where agents (cars) follow simple rules (acceleration, braking, lane changing). Observe emergent traffic jams and stop-and-go waves.

### Day 29: Evolutionary Game Theory

Build an evolutionary game theory simulation where agents with different strategies reproduce based on their success (replicator dynamics). Model the evolution of cooperation or other social behaviors.

### Day 30: Custom ABM Project

Design a custom agent-based model combining elements from previous days. Suggestions:

- Information cascade model in social networks
- Bank run simulation with herd behavior
- Cooperation evolution with punishment mechanisms
- Spatial public goods game
- Cultural transmission and drift

---

## Tips for Success

### Tools & Libraries

- Use `matplotlib` for visualizations starting from Day 6
- Consider using `NumPy` from Day 13 onward for efficiency
- From Day 22, think about modular design with `Agent` and `Environment` classes
- Optional: Use `mesa` library for more advanced ABM from Day 25+

### Best Practices

- Save your code in a GitHub repository to track progress
- Write docstrings and comments for complex functions
- For Days 22-30, visualize your simulations with animated plots or heatmaps
- Keep a coding journal noting what you learned each day
- Don't hesitate to research concepts you're unfamiliar with

### Debugging & Testing

- Test edge cases for each challenge
- Use `assert` statements to verify expected behavior
- Profile your code for performance bottlenecks in simulation days
- Compare your results with known analytical solutions when possible

### Extension Ideas

- Add GUI interfaces using `tkinter` or web interfaces with `Flask`
- Optimize simulations using `numba` or `cython`
- Implement parallel processing for large-scale simulations
- Export simulation data and create interactive visualizations
- Write blog posts explaining the game theory concepts you implement

---

## Resources

### Game Theory

- "The Evolution of Cooperation" by Robert Axelrod
- "Thinking Strategically" by Avinash Dixit and Barry Nalebuff
- Stanford's Game Theory course on Coursera

### Agent-Based Modeling

- "Think Complexity" by Allen Downey (free online)
- NetLogo models library for inspiration
- Mesa ABM documentation and tutorials

### Python Programming

- "Fluent Python" for advanced techniques
- Real Python tutorials
- Python's official documentation

---
