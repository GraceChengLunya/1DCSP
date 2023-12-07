# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 19:40:10 2023

@author: Grace
"""

import gurobipy as gp
from gurobipy import GRB

def solve_assortment_problem(items, profits, costs, budget):
    # Create a new Gurobi model
    model = gp.Model("AssortmentProblem")

    # Decision variables: binary variable for each item
    x = model.addVars(items, vtype=GRB.BINARY, name="x")

    # Objective function: maximize total profit
    model.setObjective(sum(profits[i] * x[i] for i in items), sense=GRB.MAXIMIZE)

    # Constraint: stay within the budget
    model.addConstr(sum(costs[i] * x[i] for i in items) <= budget, "BudgetConstraint")

    # Optimize the model
    model.optimize()

    # Display the selected items
    selected_items = [i for i in items if x[i].x > 0.5]
    print("Selected items:", selected_items)

    # Display the total profit
    total_profit = sum(profits[i] for i in selected_items)
    print("Total profit:", total_profit)

if __name__ == "__main__":
    # Example data
    items = ["Item1", "Item2", "Item3", "Item4"]
    profits = {"Item1": 10, "Item2": 8, "Item3": 6, "Item4": 4}
    costs = {"Item1": 2, "Item2": 3, "Item3": 1, "Item4": 2}
    budget = 7

    # Solve the assortment problem
    solve_assortment_problem(items, profits, costs, budget)
